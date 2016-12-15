# json-csv-converter

Command-line tool for converting JSON file to CSV file or vice-versa. You can give a local file path or an URL, whichever you prefer, as input to this program. 

```
usage: converter.py [-h] [-f] [-u] {csv,json} filepath

positional arguments:
  {csv,json}  The type of input
  filepath    Path or URL of the input file

optional arguments:
  -h, --help  show this help message and exit
  -f, --file  If filepath is a local file path
  -u, --url   If filepath is an URL
  ```
