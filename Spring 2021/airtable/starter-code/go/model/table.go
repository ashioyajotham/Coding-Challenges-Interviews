package model

// This file contains code for marshaling & unmarshaling the ".table.json" format.

import (
	"encoding/json"
	"errors"
	"fmt"
)

type ColumnType string

const (
	IntColumnType ColumnType = "int"
	StrColumnType ColumnType = "str"
)

type ColumnDef struct {
	Name string
	Type ColumnType
}

// Value represents a value unmarshaled from a row of table values.
// On successful unmarshaling, exactly one field will be non-nil.
type Value struct {
	Int *int64
	Str *string
}

type Row struct {
	Values []Value
}

type Table struct {
	Columns []ColumnDef
	Rows    []Row
}

// Code below this line handles the details of JSON marshaling.  You can probably ignore this.

func (c ColumnDef) MarshalJSON() ([]byte, error) {
	return json.Marshal([]interface{}{c.Name, c.Type})
}

func (v Value) MarshalJSON() ([]byte, error) {
	if v.Int != nil {
		return json.Marshal(*v.Int)
	} else if v.Str != nil {
		return json.Marshal(*v.Str)
	} else {
		return nil, errors.New("Tried to marshal ill-formed value (neither int nor string)")
	}
}

func (r Row) MarshalJSON() ([]byte, error) {
	return json.Marshal(r.Values)
}

func (t *Table) UnmarshalJSON(b []byte) error {
	var v []rowOrHeaderJSON
	err := json.Unmarshal(b, &v)
	if err != nil {
		return err
	}
	tbl := Table{Columns: *v[0].Columns}
	for i := 1; i < len(v); i++ {
		tbl.Rows = append(tbl.Rows, Row{v[i].Row.Values})
	}
	*t = tbl
	return nil
}

func (t Table) MarshalJSON() ([]byte, error) {
	buf := []byte("[")
	marshaledColumns, err := json.Marshal(t.Columns)
	if err != nil {
		return nil, err
	}
	buf = append(buf, marshaledColumns...)
	if len(t.Rows) > 0 {
		for _, row := range t.Rows {
			marshaledRow, err := json.Marshal(row)
			if err != nil {
				return nil, err
			}
			buf = append(buf, byte(','))
			buf = append(buf, marshaledRow...)
		}
	}
	buf = append(buf, byte(']'))
	return buf, nil
}

// rowOrHeaderJSON describes one element of the top-level array in a .table.json.
// On successful unmarshaling, exactly one field will be non-nil.
type rowOrHeaderJSON struct {
	Columns *[]ColumnDef
	Row     *Row
}

func (r *rowOrHeaderJSON) UnmarshalJSON(b []byte) error {
	var v []columnDefOrDataJSON
	err := json.Unmarshal(b, &v)
	if err != nil {
		return err
	}
	var result rowOrHeaderJSON
	for _, col := range v {
		if col.ColumnDef != nil {
			if result.Columns == nil {
				result.Columns = &[]ColumnDef{}
			}
			*result.Columns = append(*result.Columns, *col.ColumnDef)
		} else {
			if result.Row == nil {
				result.Row = &Row{}
			}
			result.Row.Values = append(result.Row.Values, *col.Value)
		}
	}
	if result.Columns != nil && result.Row != nil {
		return fmt.Errorf("Row has invalid mix of data and column defs: %q", b)
	}
	*r = result
	return nil
}

type columnDefOrDataJSON struct {
	// For a valid column def, this will be populated.
	ColumnDef *ColumnDef
	// For a valid data row, this will be populated.
	Value *Value
}

func (r *columnDefOrDataJSON) UnmarshalJSON(b []byte) error {
	var v interface{}
	err := json.Unmarshal(b, &v)
	if err != nil {
		return err
	}
	var result columnDefOrDataJSON
	switch x := v.(type) {
	case string:
		result.Value = &Value{Str: &x}
	case float64:
		i := int64(x) // We are intentionally oblivious to truncation here.
		result.Value = &Value{Int: &i}
	case []interface{}:
		err := unmarshalColumnDef(&result, x)
		if err != nil {
			return err
		}
	default:
		return fmt.Errorf("JSON invalid for a row of table data: %q", b)
	}
	*r = result
	return nil
}

func unmarshalColumnDef(c *columnDefOrDataJSON, def []interface{}) error {
	if len(def) != 2 {
		return errors.New("JSON invalid for a row of table data")
	}
	c.ColumnDef = &ColumnDef{}
	switch name := def[0].(type) {
	case string:
		c.ColumnDef.Name = name
	default:
		return fmt.Errorf("Invalid value for column def (name must be a string): %v", name)
	}
	switch typ := def[1].(type) {
	case string:
		for _, t := range []ColumnType{IntColumnType, StrColumnType} {
			if string(t) == typ {
				c.ColumnDef.Type = t
				return nil
			}
		}
		return fmt.Errorf("Invalid column type: %q", typ)
	default:
		return fmt.Errorf("Invalid value for column def (type must be a string): %v", typ)
	}
}
