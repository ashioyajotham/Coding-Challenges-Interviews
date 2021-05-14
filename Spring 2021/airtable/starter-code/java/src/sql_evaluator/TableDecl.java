package sql_evaluator;

import com.fasterxml.jackson.annotation.*;

/**
 * These appear in the FROM clause.
 */
public final class TableDecl extends Node {
    public final String name;  // filled in by 'sql-to-json' from the 'AS' or the 'source'
    public final String source;  // the file to load (without the ".table.json" extension)

    @JsonCreator
    public TableDecl(@JsonProperty("name") String name, @JsonProperty("source") String source) {
        if (name == null) throw new IllegalArgumentException("'name' can't be null");
        if (source == null) throw new IllegalArgumentException("'source' can't be null");
        this.name = name;
        this.source = source;
    }
}
