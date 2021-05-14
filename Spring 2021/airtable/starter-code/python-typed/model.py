from __future__ import annotations

from typing import List, Optional, Tuple, Union, Literal, TypedDict

# Can't use a 'class'-style declaration because 'from' is a reserved word
Query = TypedDict("Query", {
    "select": List["Selector"],  # non-empty array
    "from": List["TableDecl"],  # non-empty array
    "where": List["Comparison"],
})

class Selector(TypedDict):
    name: str  # filled in by 'sql-to-json' from the 'AS' or the 'source'
    source: ColumnRef

class TableDecl(TypedDict):
    name: str  # filled in by 'sql-to-json' from the 'AS' or the 'source'
    source: str  # the file to load (without the ".table.json" extension)

class Comparison(TypedDict):
    op: ComparisonOp
    left: Term
    right: Term

ComparisonOp = Union[
    Literal["="],
    Literal["!="],
    Literal[">"],
    Literal[">="],
    Literal["<"],
    Literal["<="],
]

class ColumnRefTerm(TypedDict):
    column: ColumnRef

class LiteralTerm(TypedDict):
    literal: SqlValue

Term = Union[ColumnRefTerm, LiteralTerm]

class ColumnRef(TypedDict):
    name: str
    table: Optional[str]  # is set for fully-qualified ColumnRefs ("table1.column2")

SqlType = Union[Literal["str"], Literal["int"]]
SqlValue = Union[str, int]

ColumnDef = Tuple[str, SqlType]
