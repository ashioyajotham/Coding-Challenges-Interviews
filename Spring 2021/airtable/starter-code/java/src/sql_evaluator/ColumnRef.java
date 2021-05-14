package sql_evaluator;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

/**
 * A reference to a column.  May be just "colname" or a fully-qualified "table.colname".
 */
public final class ColumnRef extends Node {
    public final String name;
    public final String table;  // non-null for fully-qualified ColumnRefs ("table1.column2")

    @JsonCreator
    public ColumnRef(@JsonProperty("name") String name, @JsonProperty("table") String table) {
        if (name == null) throw new IllegalArgumentException("'name' cannot be null");
        this.name = name;
        this.table = table;
    }
}

