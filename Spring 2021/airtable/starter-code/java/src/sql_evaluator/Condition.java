package sql_evaluator;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonValue;

/**
 * These appear in the WHERE clause.
 */
public final class Condition extends Node {
    public final Op op;
    public final Term left;
    public final Term right;

    @JsonCreator
    public Condition(@JsonProperty("op") Op op, @JsonProperty("left") Term left, @JsonProperty("right") Term right) {
        if (op == null) throw new IllegalArgumentException("'op' can't be null");
        if (left == null) throw new IllegalArgumentException("'left' can't be null");
        if (right == null) throw new IllegalArgumentException("'right' can't be null");
        this.op = op;
        this.left = left;
        this.right = right;
    }

    public enum Op {
        EQ("="), NE("!="), LT("<"), LE("<="), GT(">"), GE(">=");

        @JsonValue
        public final String symbol;

        Op(String symbol) { this.symbol = symbol; }
    }
}
