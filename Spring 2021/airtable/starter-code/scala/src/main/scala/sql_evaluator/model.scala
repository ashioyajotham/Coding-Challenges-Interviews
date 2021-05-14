package sql_evaluator

object model {
  case class Query(
    select: Seq[Selector],  // non-empty
    from: Seq[TableDecl],  // non-empty
    where: Seq[Comparison],
  )

  case class Selector(
    name: String,  // filled in by 'sql-to-json' from the 'AS' or the 'source'
    source: ColumnRef,
  )

  case class TableDecl(
    name: String,  // filled in by 'sql-to-json' from the 'AS' or the 'source'
    source: String,  // the file to load (without the ".table.json" extension)
  )

  case class Comparison(
    op: ComparisonOp,
    left: Term,
    right: Term,
  )

  sealed abstract class ComparisonOp(val symbol: String)
  object ComparisonOp {
    case object Eq extends ComparisonOp("=")
    case object Ne extends ComparisonOp("!=")
    case object Gt extends ComparisonOp(">")
    case object Ge extends ComparisonOp(">=")
    case object Lt extends ComparisonOp("<")
    case object Le extends ComparisonOp("<=")
  }

  sealed trait Term
  object Term {
    case class Column(ref: ColumnRef) extends Term
    case class Literal(value: SqlValue) extends Term
  }

  case class ColumnRef(
    name: String,
    table: Option[String],  // is set for fully-qualified ColumnRefs ("table1.column2")
  )

  sealed abstract class SqlType(val name: String)
  object SqlType {
    case object Str extends SqlType("str")
    case object Int extends SqlType("int")
  }

  sealed trait SqlValue
  object SqlValue {
    case class Str(value: String) extends SqlValue
    case class Int(value: scala.Int) extends SqlValue
  }

  case class ColumnDef(name: String, typ: SqlType)

  case class Table(columns: Seq[ColumnDef], rows: Seq[Seq[SqlValue]])


  // circe Encoder and Decoder implementations for the types above
  object codec {
    import io.circe.syntax.EncoderOps  // for .asJson
    import io.circe.generic.semiauto.deriveCodec
    import io.circe.{HCursor, Json, Decoder, Encoder, Codec, DecodingFailure, JsonObject, JsonNumber}
    import io.circe.Decoder.Result

    implicit val queryCodec: Codec[Query] = deriveCodec
    implicit val selectorCodec: Codec[Selector] = deriveCodec
    implicit val tableDeclCodec: Codec[TableDecl] = deriveCodec
    implicit val comparisonCodec: Codec[Comparison] = deriveCodec
    implicit val columnRefCodec: Codec[ColumnRef] = deriveCodec

    implicit val comparisonOpEncoder: Encoder[ComparisonOp] = value => Json.fromString(value.symbol)
    implicit val comparisonOpDecoder: Decoder[ComparisonOp] = (c: HCursor) => c.value.asString match {
      case Some("=") => Right(ComparisonOp.Eq)
      case Some("!=") => Right(ComparisonOp.Ne)
      case Some(">") => Right(ComparisonOp.Gt)
      case Some(">=") => Right(ComparisonOp.Ge)
      case Some("<") => Right(ComparisonOp.Lt)
      case Some("<=") => Right(ComparisonOp.Le)
      case _ => Left(DecodingFailure("expecting of six comparison operators", c.history))
    }

    implicit val sqlValueEncoder: Encoder[SqlValue] = {
      case SqlValue.Str(raw) => Json.fromString(raw)
      case SqlValue.Int(raw) => Json.fromInt(raw)
    }
    implicit val sqlValueDecoder: Decoder[SqlValue] = (c: HCursor) =>
      c.value.foldWith(new Json.Folder[Decoder.Result[SqlValue]] {
        override def onNull: Result[SqlValue] = Left(DecodingFailure("expecting string or integer", c.history))
        override def onBoolean(value: Boolean): Result[SqlValue] = Left(DecodingFailure("expecting string or integer", c.history))
        override def onArray(value: Vector[Json]): Result[SqlValue] = Left(DecodingFailure("expecting string or integer", c.history))
        override def onObject(value: JsonObject): Result[SqlValue] = Left(DecodingFailure("expecting string or integer", c.history))
        override def onNumber(value: JsonNumber): Result[SqlValue] = value.toInt match {
          case Some(i) => Right(SqlValue.Int(i))
          case None => Left(DecodingFailure("number is out of range", c.history))
        }
        override def onString(value: String): Result[SqlValue] = Right(SqlValue.Str(value))
      })

    implicit val sqlTypeEncoder: Encoder[SqlType] = value => Json.fromString(value.name)
    implicit val sqlTypeDecoder: Decoder[SqlType] = (c: HCursor) => c.value.asString match {
      case Some("str") => Right(SqlType.Str)
      case Some("int") => Right(SqlType.Int)
      case _ => Left(DecodingFailure("expecting \"str\" or \"int\"", c.history))
    }

    implicit val columnDefEncoder: Encoder[ColumnDef] = Encoder[(String, SqlType)].contramap(v => (v.name, v.typ))
    implicit val columnDefDecoder: Decoder[ColumnDef] = Decoder[(String, SqlType)].map(ColumnDef.tupled)

    implicit val termEncoder: Encoder[Term] = {
      case Term.Column(ref) => Json.obj(("column", ref.asJson))
      case Term.Literal(value) => Json.obj(("literal", value.asJson))
    }
    implicit val termDecoder: Decoder[Term] = taggedUnionDecoder({
      case "column" => Some(Decoder[ColumnRef].map(Term.Column))
      case "literal" =>  Some(Decoder[SqlValue].map(Term.Literal))
      case _ => None
    })

    private def taggedUnionDecoder[T](options: String => Option[Decoder[T]]): Decoder[T] = (c: HCursor) => {
      c.value.asObject match {
        case Some(obj) =>
          obj.toList match {
            case List((fieldName, fieldValue)) => options(fieldName) match {
              case None => Left(DecodingFailure("unknown field name", c.history))
              case Some(decoder) => decoder.decodeJson(fieldValue)
            }
            case pairs =>
              Left(DecodingFailure("expecting exactly one field, got " + pairs.length, c.history))
        }
        case _ =>
          Left(DecodingFailure("expecting object", c.history))
      }
    }

    implicit val tableEncoder: Encoder[Table] = (table: Table) => {
      val columns = table.columns.asJson
      val rows = table.rows.map(_.asJson)
      Json.arr(List(columns) ++ rows: _*)
    }
    implicit val tableDecoder: Decoder[Table] = (c: HCursor) => {
      c.value.asArray match {
        case Some(elements) =>
          if (elements.isEmpty) {
            Left(DecodingFailure("array must have at least one element", c.history))
          } else {
            val first = elements(0)
            val rest = elements.drop(1)
            for {
              columns <- first.as[Vector[ColumnDef]]
              rows <- Json.arr(rest: _*).as[Vector[Vector[SqlValue]]]
            } yield Table(columns, rows)
          }
        case _ => Left(DecodingFailure("expecting an array", c.history))
      }
    }
  }
}
