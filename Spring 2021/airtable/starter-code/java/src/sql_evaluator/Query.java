package sql_evaluator;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.ArrayList;

/**
 * The top-level node for a query: SELECT ... FROM ... WHERE.
 */
public final class Query extends Node {
    public final ArrayList<Selector> select;  // non-empty
    public final ArrayList<TableDecl> from;  // non-empty
    public final ArrayList<Condition> where;

    @JsonCreator
    public Query(
        @JsonProperty("select") ArrayList<Selector> select,
        @JsonProperty("from") ArrayList<TableDecl> from,
        @JsonProperty("where") ArrayList<Condition> where
    ) {
        if (select == null) throw new IllegalArgumentException("'select' can't be null");
        if (from == null) throw new IllegalArgumentException("'from' can't be null");
        if (where == null) throw new IllegalArgumentException("'where' can't be null");
        if (select.size() == 0) throw new IllegalArgumentException("'select' can't be empty");
        if (from.size() == 0) throw new IllegalArgumentException("'from' can't be empty");
        this.select = select;
        this.from = from;
        this.where = where;
    }
}
