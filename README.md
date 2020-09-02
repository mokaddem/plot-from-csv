# plot-from-csv

Script to plot data from a CSV file using the matplotlib library

## Example
```csv
+--- data.csv ---+
| Luxembourg 42  |
| Germany 112    |
| France 392     |
+----------------+
```

```bash
./plot.py data.csv --title 'Country with numbers' --xlabel 'A random amount'
```

## Usage

```
usage: plot.py [-h] [--delimiter DELIMITER] [--quotechar QUOTECHAR]
               [--title TITLE] [--xlabel XLABEL] [--logopath LOGOPATH]
               filename

Plot data from csv. First column is the label, second is the value

positional arguments:
  filename              The CSV file containing the data

optional arguments:
  -h, --help            show this help message and exit
  --delimiter DELIMITER
                        Set the delimiter character when parsing the CSV
  --quotechar QUOTECHAR
                        Set the quote character when parsing the CSV
  --title TITLE         The title of the chart
  --xlabel XLABEL       The label of the x axis
  --logopath LOGOPATH   The path of the logo
```
