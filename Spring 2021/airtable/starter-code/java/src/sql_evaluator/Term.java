package sql_evaluator;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonSubTypes;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.annotation.JsonValue;
import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.core.JsonParseException;
import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.SerializerProvider;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.databind.deser.std.StdDeserializer;
import com.fasterxml.jackson.databind.jsontype.TypeSerializer;
import com.fasterxml.jackson.databind.ser.std.StdSerializer;

import java.io.IOException;

@JsonTypeInfo(use= JsonTypeInfo.Id.NAME, include=JsonTypeInfo.As.WRAPPER_OBJECT)
@JsonSubTypes({
    @JsonSubTypes.Type(value=Term.Column.class, name="column"),
    @JsonSubTypes.Type(value=Term.Literal.class, name="literal"),
})
public abstract class Term extends Node {
    public static class Column extends Term {
        @JsonValue
        public final ColumnRef ref;

        @JsonCreator(mode=JsonCreator.Mode.DELEGATING)
        public Column(ColumnRef ref) {
            this.ref = ref;
        }
    }

    @JsonDeserialize(using=Literal.Deserializer.class)
    @JsonSerialize(using=Literal.Serializer.class)
    public static final class Literal extends Term {
        @JsonDeserialize(using=Literal.Deserializer.class)
        public final Object value;  // Either a String or Integer object.

        @JsonCreator(mode=JsonCreator.Mode.DELEGATING)
        public Literal(Object value) {
            if (!(value instanceof String || value instanceof Integer)) {
                throw new IllegalArgumentException("'value' must be either a String or an Integer, got " + value.getClass().getCanonicalName());
            }
            this.value = value;
        }

        public static final class Deserializer extends StdDeserializer<Literal> {
            public Deserializer() {
                super(Literal.class);
            }

            @Override
            public Literal deserialize(JsonParser jp, DeserializationContext ctx) throws IOException {
                Object value;
                switch (jp.currentToken()) {
                    case VALUE_STRING:
                        value = jp.getText();
                        break;
                    case VALUE_NUMBER_INT:
                        value = jp.getIntValue();
                        break;
                    default:
                        throw new JsonParseException(jp, "expecting a string or integer");
                }
                return new Literal(value);
            }
        }

        public static final class Serializer extends StdSerializer<Literal> {
            public Serializer() {
                super(Literal.class);
            }

            @Override
            public void serializeWithType(Literal literal, JsonGenerator g, SerializerProvider sp, TypeSerializer typeSer) throws IOException {
                g.writeStartObject();
                g.writeFieldName("literal");
                this.serialize(literal, g, sp);
                g.writeEndObject();
            }

            @Override
            public void serialize(Literal literal, JsonGenerator g, SerializerProvider serializerProvider) throws IOException {
                if (literal.value instanceof String) {
                    g.writeString((String) literal.value);
                } else if (literal.value instanceof Integer) {
                    g.writeNumber((Integer) literal.value);
                } else {
                    throw new AssertionError("bad type: " + literal.value.getClass().getCanonicalName());
                }
            }
        }
    }
}
