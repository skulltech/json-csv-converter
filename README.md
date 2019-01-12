# json-csv-converter

Command-line tool for converting JSON file to CSV file or vice-versa. You can give a local file path or an URL, whichever you prefer, as input to this program. 

## Note
I built this script as a fun personal project around the December of 2016. I'm not planning to continue development on this, so I'll be archiving this. As far as I can see, this script still works, so please use it if you want. If you want to extend it or fix any possible bug // shortcoming, you're welcome to fork it. If you need this repo un-archived, for whatever reason that might be, send me an email.

```console
usage: converter.py [-h] [-f] [-u] {csv,json} filepath

positional arguments:
  {csv,json}  The type of input
  filepath    Path or URL of the input file

optional arguments:
  -h, --help  show this help message and exit
  -f, --file  If filepath is a local file path
  -u, --url   If filepath is an URL
  ```
