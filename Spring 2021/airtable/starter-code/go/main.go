package sql_evaluator

import (
	"bufio"
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"path"

	"sql_evaluator/model"
)

func die(message string) {
	os.Stderr.WriteString(message)
	os.Exit(1)
}

func Main() {
	if len(os.Args) != 4 {
		die(fmt.Sprintf("Usage: %s <table-folder> <sql-json-file> <output-file>\n", os.Args[0]))
	}

	tableFolder := os.Args[1]
	sqlJSONFile := os.Args[2]
	outputFile := os.Args[3]

	var query model.Query
	{
		err := jsonUnmarshalFromFile(sqlJSONFile, &query)
		if err != nil {
			die(fmt.Sprintf("Error reading %q: %s\n", sqlJSONFile, err))
		}
	}

	var tables []model.Table = nil
	for _, tableDecl := range query.From {
		tableSourcePath := path.Join(tableFolder, tableDecl.Source+".table.json")
		var table model.Table
		err := jsonUnmarshalFromFile(tableSourcePath, &table)
		if err != nil {
			die(fmt.Sprintf("Error reading %q: %s\n", tableSourcePath, err))
		}
		tables = append(tables, table)
	}

	// TODO: Actually evaluate query.
	// For now, just dump the input back out.
	{
		fw, err := os.Create(outputFile)
		if err != nil {
			die(fmt.Sprintf("Error opening %q for writing: %s\n", outputFile, err))
		}
		defer fw.Close()

		w := bufio.NewWriter(fw)
		defer w.Flush()

		mustJSONMarshalIndent(w, query)

		for _, table := range tables {
			writeTable(w, table)
		}
	}
}

func writeTable(w *bufio.Writer, table model.Table) {
	w.WriteString("[\n")

	w.WriteString("    ")
	mustJSONMarshal(w, table.Columns)

	for _, row := range table.Rows {
		w.WriteString(",\n    ")
		mustJSONMarshal(w, row)
	}

	w.WriteString("\n]\n")
}

// NOTE: Not using json.Decoder because it doesn't error if there's trailing garbage.
func jsonUnmarshalFromFile(path string, v interface{}) error {
	contents, err := ioutil.ReadFile(path)
	if err != nil {
		return err
	}
	return json.Unmarshal(contents, v)
}

func newJSONEncoder(w io.Writer) *json.Encoder {
	encoder := json.NewEncoder(w)
	// By default, "&", "<", and ">" are escaped, which makes the output harder to read.  Disable that.
	encoder.SetEscapeHTML(false)
	return encoder
}

func mustJSONMarshal(w io.Writer, v interface{}) {
	buffer := &bytes.Buffer{}
	encoder := newJSONEncoder(buffer)
	err := encoder.Encode(v)
	if err != nil {
		panic(fmt.Sprintf("Can't happen: value should remarshal, but got error: %v", err))
	}
	// Ugh, Encode() adds a newline even though Marshal() does not.  Remove it.
	raw := buffer.Bytes()
	end := len(raw) - 1
	if raw[end] != '\n' {
		panic("Last byte written by Encode() wasn't a newline.")
	}
	raw = raw[:end]
	w.Write(raw)
}

func mustJSONMarshalIndent(w io.Writer, v interface{}) {
	encoder := newJSONEncoder(w)
	encoder.SetIndent("", "    ")
	err := encoder.Encode(v)
	if err != nil {
		panic(fmt.Sprintf("Can't happen: value should remarshal, but got error: %v", err))
	}
}
