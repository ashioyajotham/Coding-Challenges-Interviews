package sql_evaluator;

import com.fasterxml.jackson.core.*;
import com.fasterxml.jackson.databind.JsonMappingException;
import com.fasterxml.jackson.databind.MapperFeature;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.File;
import java.io.IOException;
import java.io.OutputStream;
import java.io.StringWriter;
import java.io.Writer;

public final class JacksonUtil {
    private static final JsonFactory jsonFactory = new JsonFactory()
            .disable(JsonGenerator.Feature.AUTO_CLOSE_TARGET);

    private static final ObjectMapper objectMapper = new ObjectMapper(jsonFactory)
            .disable(
                MapperFeature.AUTO_DETECT_CREATORS,
                MapperFeature.AUTO_DETECT_GETTERS,
                MapperFeature.AUTO_DETECT_IS_GETTERS,
                MapperFeature.AUTO_DETECT_SETTERS);

    public static String toString(Object value) {
        StringWriter sw = new StringWriter();
        try {
            write(sw, value);
        }
        catch (IOException ex) {
            throw new AssertionError("IOException from StringWriter?");
        }
        return sw.getBuffer().toString();
    }

    /** Like {@link #toString}, except with indentation. */
    public static String toStringIndented(Object value) {
        StringWriter sw = new StringWriter();
        try {
            writeIndented(sw, value);
        }
        catch (IOException ex) {
            throw new AssertionError("IOException from StringWriter?");
        }
        return sw.getBuffer().toString();
    }

    public static void write(Writer out, Object value) throws IOException {
        try {
            objectMapper.writer().writeValue(out, value);
        }
        catch (JsonGenerationException|JsonMappingException ex) {
            throw new AssertionError("JSON serialization error", ex);
        }
    }

    /** Like {@link #write(Writer, Object) write()}, except with indentation. */
    public static void writeIndented(Writer out, Object value) throws IOException {
        try {
            objectMapper.writer(new StandardPrettyPrinter()).writeValue(out, value);
        }
        catch (JsonGenerationException|JsonMappingException ex) {
            throw new AssertionError("JSON serialization error", ex);
        }
        out.write('\n');
    }

    public static void write(OutputStream out, Object value) throws IOException {
        try {
            objectMapper.writer().writeValue(out, value);
        }
        catch (JsonGenerationException|JsonMappingException ex) {
            throw new AssertionError("JSON serialization error", ex);
        }
    }

    /** Like {@link #write(Writer, Object) write()}, except with indentation. */
    public static void writeIndented(OutputStream out, Object value) throws IOException {
        try {
            objectMapper.writer(new StandardPrettyPrinter()).writeValue(out, value);
        }
        catch (JsonGenerationException|JsonMappingException ex) {
            throw new AssertionError("JSON serialization error", ex);
        }
        out.write('\n');
    }

    public static <T> T readFromFile(String path, Class<T> cls) throws IOException {
        JsonParser jp = objectMapper.getFactory().createParser(new File(path));
        T value = objectMapper.readValue(jp, cls);
        if (jp.nextToken() != null) {
            throw new JsonParseException(jp, "found unexpected data after entire value was parsed");
        }
        return value;
    }

    // The DefaultPrettyPrinter renders empty arrays and objects with a space: "[ ]" and "{ }".
    // We don't want the space.
    private static final class StandardPrettyPrinter implements PrettyPrinter {
        private int indentationLevel = 0;

        @Override
        public void writeRootValueSeparator(JsonGenerator g) {}

        @Override
        public void writeStartObject(JsonGenerator g) throws IOException {
            g.writeRaw('{');
            indentationLevel++;
        }

        @Override
        public void beforeObjectEntries(JsonGenerator g) throws IOException {
            writeIndentation(g);
        }

        private void writeIndentation(JsonGenerator g) throws IOException {
            g.writeRaw('\n');
            for (int i = 0; i < indentationLevel; i++) {
                g.writeRaw("    ");
            }
        }

        @Override
        public void writeObjectFieldValueSeparator(JsonGenerator g) throws IOException
        {
            g.writeRaw(": ");
        }

        @Override
        public void writeObjectEntrySeparator(JsonGenerator g) throws IOException
        {
            g.writeRaw(',');
            writeIndentation(g);
        }

        @Override
        public void writeEndObject(JsonGenerator g, int nrOfEntries) throws IOException
        {
            indentationLevel--;
            if (nrOfEntries > 0) {
                writeIndentation(g);
            }
            g.writeRaw('}');
        }

        @Override
        public void writeStartArray(JsonGenerator g) throws IOException
        {
            indentationLevel++;
            g.writeRaw('[');
        }

        @Override
        public void beforeArrayValues(JsonGenerator g) throws IOException {
            writeIndentation(g);
        }

        @Override
        public void writeArrayValueSeparator(JsonGenerator g) throws IOException
        {
            g.writeRaw(',');
            writeIndentation(g);
        }

        @Override
        public void writeEndArray(JsonGenerator g, int nrOfValues) throws IOException
        {
            indentationLevel--;
            if (nrOfValues > 0) {
                writeIndentation(g);
            }
            g.writeRaw(']');
        }
    }
}
