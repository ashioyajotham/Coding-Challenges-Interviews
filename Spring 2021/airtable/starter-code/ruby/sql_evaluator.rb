# frozen_string_literal: true

require "json"

def main
  if ARGV.length != 3
    $stderr.puts "Usage: COMMAND <table-folder> <sql-json-file> <output-file>"
    exit 1
  end

  table_folder, sql_json_file, output_file = ARGV

  # Load the query JSON.
  begin
    query = load_json_from_file(sql_json_file)
  rescue JsonFileLoadError => e
    $stderr.puts "Error loading SQL JSON from #{q(sql_json_file)}: #{e}"
    exit 1
  end

  # Load all the tables referenced in the "FROM" clause.
  tables = []
  query["from"].each do |table_decl|
    table_source_path = File.join(table_folder, "#{table_decl["source"]}.table.json")
    raw_table = load_json_from_file(table_source_path)
    begin
      raw_table = load_json_from_file(table_source_path)
    rescue JsonFileLoadError => e
      $stderr.puts "Error loading table JSON from #{q(sql_json_file)}: #{e}"
      exit 1
    end
    table = Table.new(raw_table[0], raw_table.drop(1))
    tables.push(table)
  end

  # TODO: Actually evaluate query.
  # For now, just dump the input back out.
  File.open(output_file, "w") do |out|
    write_json_indented(out, query)
    tables.each do |table|
      write_table(out, table)
    end
  end
end

class Table
  def initialize(columns, rows)
    @columns = columns
    @rows = rows
  end

  attr_reader :columns, :rows
end

class JsonFileLoadError < StandardError
end

def load_json_from_file(path)
  contents = File.read(path, encoding: "ascii")
  JSON.parse(contents)
rescue SystemCallError, IOError => e
  raise JsonFileLoadError, "Error reading: #{e}"
rescue JSON::ParserError => e
  raise JsonFileLoadError, "Invalid JSON: #{e}"
end

def write_table(out, table)
  out << "[\n"
  out << "    #{JSON.generate(table.columns)}"
  table.rows.each do |row|
    out << ",\n    #{JSON.generate(row)}"
  end
  out << "\n]\n"
end

def write_json_indented(out, value)
  json = JSON.pretty_generate(value, indent: "    ")
  # For readability, remove the newlines and whitespace that Ruby's JSON formatter
  # adds to empty arrays and objects.
  json = json.gsub(/{\n *}/m, "{}").gsub(/\[\n *\n *\]/m, "[]")
  out << json
  out << "\n"
end

# For quoting strings in messages to the user.
def q(s)
  s.to_json
end

if __FILE__ == $PROGRAM_NAME
  main
end
