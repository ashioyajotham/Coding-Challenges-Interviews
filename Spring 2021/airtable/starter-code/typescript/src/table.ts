import {ColumnDef, SqlValue} from './model';

export class Table {
    columns: Array<ColumnDef>;
    rows: Array<Array<SqlValue>>;
    constructor(columns: Array<ColumnDef>, rows: Array<Array<SqlValue>>) {
        this.columns = columns;
        this.rows = rows;
    }
}
