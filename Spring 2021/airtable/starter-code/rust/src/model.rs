use serde::ser::SerializeSeq;
use serde::{Deserialize, Deserializer, Serialize, Serializer};
use serde_tuple::*;
use std::fmt;

#[derive(Serialize, Deserialize, Debug)]
pub struct Query {
    pub select: Vec<Selector>, // non-empty
    pub from: Vec<TableRef>,   // non-empty
    #[serde(rename = "where")]
    pub where_: Vec<Comparison>,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct Selector {
    pub name: String, // filled in by 'sql-to-json' from the 'AS' or the 'source'
    pub source: ColumnRef,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct TableRef {
    pub name: String, // filled in by 'sql-to-json' from the 'AS' or the 'source'
    pub source: String,
}

#[derive(Serialize, Deserialize, Debug)]
pub struct Comparison {
    pub op: ComparisonOp,
    pub left: Term,
    pub right: Term,
}

#[derive(Serialize, Deserialize, Debug, PartialEq, Eq)]
pub enum ComparisonOp {
    #[serde(rename = "=")]
    Eq,
    #[serde(rename = "!=")]
    Ne,
    #[serde(rename = ">")]
    Gt,
    #[serde(rename = ">=")]
    Ge,
    #[serde(rename = "<")]
    Lt,
    #[serde(rename = "<=")]
    Le,
}

#[derive(Serialize, Deserialize, Debug)]
pub enum Term {
    #[serde(rename = "column")]
    Column(ColumnRef),
    #[serde(rename = "literal")]
    Literal(SqlValue),
}

#[derive(Serialize, Deserialize, Debug)]
pub struct ColumnRef {
    pub name: String,
    pub table: Option<String>,
}

#[derive(Serialize, Deserialize, Debug)]
#[serde(untagged)]
pub enum SqlValue {
    Int(i32),
    Str(String),
}

#[derive(Serialize, Deserialize, Debug)]
pub enum SqlType {
    #[serde(rename = "int")]
    Int,
    #[serde(rename = "str")]
    Str,
}

#[derive(Debug)]
pub struct Table {
    pub columns: Vec<ColumnDef>,
    pub rows: Vec<Vec<SqlValue>>,
}

#[derive(Serialize_tuple, Deserialize_tuple, Debug)]
pub struct ColumnDef {
    pub name: String,
    pub type_: SqlType,
}

impl Serialize for Table {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        let mut seq = serializer.serialize_seq(Some(1 + self.rows.len()))?;
        seq.serialize_element(&self.columns).unwrap();
        for row in &self.rows {
            seq.serialize_element(&row).unwrap();
        }
        seq.end()
    }
}

impl<'de> Deserialize<'de> for Table {
    fn deserialize<D>(deserializer: D) -> Result<Self, D::Error>
    where
        D: Deserializer<'de>,
    {
        struct TableVisitor;

        impl<'de> serde::de::Visitor<'de> for TableVisitor {
            type Value = Table;

            fn expecting(&self, formatter: &mut fmt::Formatter) -> fmt::Result {
                formatter.write_str("an array")
            }

            fn visit_seq<SA>(self, mut seq: SA) -> Result<Self::Value, SA::Error>
            where
                SA: serde::de::SeqAccess<'de>,
            {
                let columns: Vec<ColumnDef> = seq
                    .next_element()?
                    .ok_or_else(|| serde::de::Error::invalid_length(0, &self))?;
                let mut rows: Vec<Vec<SqlValue>> = Vec::new();
                while let Some(row) = seq.next_element()? {
                    rows.push(row);
                }

                Ok(Table { columns, rows })
            }
        }

        deserializer.deserialize_seq(TableVisitor)
    }
}
