class Table {
    constructor(columns, rows) {
        this.columns = columns;  // Array<ColumnDef>
        this.rows = rows;  // Array<Array<string | number>>>
    }
}

module.exports = Table;
