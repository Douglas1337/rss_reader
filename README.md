# RSS Reader using Python 3.10

## Task Description

This Python script functions as a command-line RSS reader. The script parses an RSS (XML) document from a specified URL and provides formatted outputs in JSON and standard output formats. Specifically, it supports the RSS 2.0 format and parses elements such as `<channel>` and `<item>`.

### Features

- Command line parsing to fetch RSS feeds.
- XML parsing to extract data from RSS feeds.
- Output in formatted text and JSON.

## Command Line Arguments
- If the limit is not specified, then the user should get all available feeds.
- If the limit is larger than the feed size, then the user should get all available news.
- The limit argument should also affect JSON generation
- In the case of using the --json argument, your utility should convert the news into the JSON format.


### Command Line Interface

The CLI interface is as follows:

```plaintext
usage: rss_reader.py [-h] [--json] [--limit LIMIT] source

Pure Python command-line RSS reader.

positional arguments:
 source         RSS URL

optional arguments:
 -h, --help     show this help message and exit
 --json         Print result as JSON in stdout
 --limit LIMIT  Limit news topics if this parameter is provided
