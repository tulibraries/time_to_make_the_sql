# Time to make the SQL!

THis python script will transform the contents of a particularly structured CSV file and transform it into the SQL needed to insert it into the Dematic MSSQL Server database.

## Example usage
```bash
python time_to_make_the_sql.py -i my_input.csv -o my_output.sql
```

An example of expected CSV and output SQL file are included in this repo.

## Expected structure of CSV

The CSV is expected to have a initial header row containing four required fields

* "Item Number"
* "Author [Title] *max characters = 37" #don't ask
* "Title [Box Number]"
* "Call Number"

A database constraint this script considers is that fields have a maximum length limit of 37 characters, except for "Item Number", which has a maximum length of 20 characters. Any rows with fields exceeding those constraints will print an warning to stdout  