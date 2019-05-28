import csv
import argparse


SQL_USE = "USE DMS_TEMPLE;\n"
SQL_INSERT_INTO = "INSERT INTO dematicemsp.DMSInventory"
dyanamic_fields = ["itemNumber", "author", "title", "callNumber"]
static_fields = ["local", "circulationStatus", "audited", "materialType", "storageType", "statisticalCode", "containerId",  "sectorPosition", "binType", "binHeight", "storeDate"]
all_fields = dyanamic_fields + static_fields
SQL_FIELDS = "(" + (", ").join(all_fields) + ")"

failed_items = []

def values(row):
  return " VALUES (" + dynamic_values(row) + ", 'Y', 'Delivered', 'N', '', '', '', '', '', '', 0, '2019-03-01')"


def dynamic_values(row):
  df = [('Item Number', 20), ('Author [Title] *max characters = 37', 37),('Title [Box Number]', 37),('Call Number', 37)]
  return (", ").join(["'{}'".format(field(row, f[0], f[1])) for f in df])


def field(row, field, constraint=37):
  # strip apostrophies    
  value = row[field].replace("'","")
  if len(value) > constraint:
    print validation_check_message(row, field + " exceeded max length of " + str(constraint) )
  return  value


def validation_check_message(row, message):
  return "Record with Item Number " + row["Item Number"] + " failed validation: " + message


def build_sql(input_file, output_file):
  sql = SQL_USE
  with open(input_file, "rb") as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
      insert = SQL_INSERT_INTO + SQL_FIELDS + values(row) + ";\n"
      sql += insert

  with open(output_file, "wb") as output:
    output.write(sql)


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-i","--input-file", help="CSV file to use as basis of SQL")
  parser.add_argument("-o","--output-file", help="Path to output SQL file we are going to create")
  args = parser.parse_args()
  build_sql(args.input_file, args.output_file)
