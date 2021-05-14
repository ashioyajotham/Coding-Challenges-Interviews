export type Query = {
    select: Array<Selector>;  // non-empty array
    from: Array<TableDecl>;  // non-empty array
    where: Array<Comparison>;
};

export type Selector = {
    name: string;  // filled in by 'sql-to-json' from the 'AS' or the 'source'
    source: ColumnRef;
};

export type TableDecl = {
    name: string;  // filled in by 'sql-to-json' from the 'AS' or the 'source'
    source: string;  // the file to load (without the ".table.json" extension)
};

export type Comparison = {
    op: ComparisonOp;
    left: Term;
    right: Term;
};

export type ComparisonOp = '=' | '!=' | '>' | '>=' | '<' | '<=';

export type Term = {column: ColumnRef} | {literal: SqlValue};

export type ColumnRef = {
    name: string;
    table: string | null;  // non-null for fully-qualified ColumnRefs ("table1.column2")
};

export type ColumnDef = [string, SqlType];

export type SqlType = 'str' | 'int';
export type SqlValue = string | number;
