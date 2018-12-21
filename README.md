# HTDBM2TXT

## Description

Apache HTTPD has "[httxt2dbm](https://httpd.apache.org/docs/2.4/programs/httxt2dbm.html)" to convert a single txt file containing key value pairs to a dbm database.
You can convert the dbm to txt again using this python script.

## Requirements

- Python 3
- Write permission on the directory you choose for the output file

## Usage

Download [htdbm2txt.py](htdbm2txt.py) and run the command below

```bash
python3 htdbm2txt.py -i input.dbm -o output.txt
```
