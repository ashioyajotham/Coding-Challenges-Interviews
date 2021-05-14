package sql_evaluator;

import com.fasterxml.jackson.annotation.*;

/**
 * These appear in the SELECT clause.
 */
public final class Selector extends Node {
    public final String name;  // filled in by 'sql-to-json' from the 'AS' or the 'source'
    public final ColumnRef source;

    @JsonCreator
    public Selector(@JsonProperty("name") String name, @JsonProperty("source") ColumnRef source) {
        if (name == null) throw new IllegalArgumentException("'name' can't be null");
        if (source == null) throw new IllegalArgumentException("'source' can't be null");
        this.name = name;
        this.source = source;
    }
}

