mod model;
use self::model::Query;
use self::model::Table;

use std::fs::File;
use std::io;
use std::path::Path;
use std::process;

fn main() {
    let args: Vec<String> = std::env::args().skip(1).collect();
    match main_inner(args) {
        Ok(()) => {}
        Err(message) => {
            eprintln!("{}", message);
            process::exit(1);
        }
    }
}

fn main_inner(args: Vec<String>) -> Result<(), String> {
    if args.len() != 3 {
        return Err("Usage: COMMAND <table-folder> <sql-json-file> <output-file>".to_string());
    }

    let table_folder = Path::new(&args[0]);
    let sql_json_file = &args[1];
    let output_file = &args[2];

    // Load the query JSON.
    let query: Query = load_json_from_file(sql_json_file)
        .map_err(|err| format!("Error loading SQL JSON from \"{}\": {}", sql_json_file, err))?;

    // Load all tables referenced in the "FROM" clause.
    let mut tables: Vec<Table> = Vec::new();
    for table_decl in &query.from {
        let table_source_path = String::from(
            table_folder
                .join(format!("{}.table.json", table_decl.source))
                .to_str()
                .expect("path"),
        );
        let table: Table = load_json_from_file(&table_source_path).map_err(|err| {
            format!(
                "Error loading table JSON from \"{}\": {}",
                table_source_path, err
            )
        })?;
        tables.push(table);
    }

    // TODO: Actually evaluate query.
    // For now, just dump the input back out.
    {
        let map_err = |err| format!("Unable to write to \"{}\": {}", output_file, err);
        let f_out = File::create(output_file).map_err(map_err)?;
        let mut out = io::BufWriter::new(f_out);
        write_json_indented(&mut out, &query).map_err(map_err)?;
        for table in &tables {
            write_table(&mut out, table).map_err(map_err)?;
        }
    }

    Ok(())
}

fn load_json_from_file<T>(path: &str) -> Result<T, String>
where
    for<'de> T: serde::Deserialize<'de>,
{
    let mut file_handle = File::open(path).map_err(|err| format!("Error reading: {}", err))?;
    serde_json::from_reader(&mut file_handle).map_err(|err| format!("Invalid syntax: {}", err))
}

fn write_json_indented<W, T>(mut out: W, value: &T) -> Result<(), io::Error>
where
    W: io::Write,
    T: serde::Serialize + ?Sized,
{
    let formatter = serde_json::ser::PrettyFormatter::with_indent(b"    ");
    let mut ser = serde_json::Serializer::with_formatter(out.by_ref(), formatter);
    value.serialize(&mut ser)?;
    out.write_all(b"\n")
}

fn write_table<W>(mut out: W, table: &Table) -> Result<(), io::Error>
where
    W: io::Write,
{
    out.write_all(b"[\n")?;

    out.write_all(b"    ")?;
    serde_json::to_writer(out.by_ref(), &table.columns)?;

    for row in &table.rows {
        out.write_all(b",\n    ")?;
        serde_json::to_writer(out.by_ref(), row)?;
    }

    out.write_all(b"\n]\n")?;

    Ok(())
}
