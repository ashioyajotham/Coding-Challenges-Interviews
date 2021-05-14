package sql_evaluator

import sql_evaluator.model._
import sql_evaluator.model.codec._

import scala.collection.mutable.ArrayBuffer
import java.io.{BufferedWriter, File, FileWriter, Writer}

object Main {

  def main(args: Array[String]): Unit = {
    if (args.length != 3) {
      System.err.println("Usage: COMMAND <table-folder> <sql-json-file> <output-file>")
      System.exit(1)
      return
    }

    val tableFolder = args(0)
    val sqlJsonFile = args(1)
    val outputFile = args(2)

    val query = readJsonFromFile[Query](sqlJsonFile) match {
      case Left(err) =>
        Console.err.println("Error loading \"" + sqlJsonFile + "\" as query JSON: " + err)
        System.exit(1); return
      case Right(v) => v
    }


    val tables: ArrayBuffer[Table] = new ArrayBuffer()
    query.from.foreach(tableDecl => {
      val tableSourcePath = tableFolder + File.separator + (tableDecl.source + ".table.json")
      val table: Table = readJsonFromFile[Table](tableSourcePath) match {
        case Left(err) =>
          Console.err.println("Error loading \"" + tableSourcePath + "\" as table JSON: " + err)
          System.exit(1); return
        case Right(v) => v
      }
      tables += table
    })

    // TODO: Actually evaluate query.
    // For now, just dump the input back out.
    val out = new BufferedWriter(new FileWriter(outputFile))
    try {
      writeJsonIndented(out, query)

      tables.foreach(table => {
        writeTable(out, table)
      })
    } finally {
      out.close()
    }
  }

  def readJsonFromFile[T: io.circe.Decoder](path: String): Either[String, T] =
    io.circe.jawn.decodeFile[T](new File(path)).left.map(_.getMessage)

  final val indentedPrinter = io.circe.Printer.spaces4.copy(colonLeft = "", lrbracketsEmpty = "")
  def writeJsonIndented[T: io.circe.Encoder](out: Writer, value: T): Unit = {
    import io.circe.syntax.EncoderOps  // for .asJson
    out.write(indentedPrinter.print(value.asJson))
    out.write("\n")
  }

  def writeTable(out: Writer, table: Table): Unit = {
    import io.circe.syntax.EncoderOps  // for .asJson
    out.write("[\n")

    out.write("    ")
    out.write(table.columns.asJson.noSpaces)

    table.rows.foreach(row => {
      out.write(",\n    ")
      out.write(row.asJson.noSpaces)
    })

    out.write("\n]\n")
  }
}
