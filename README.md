# grepword

A CLI tool to search for words across text files and return filenames and line numbers. The result is a list of filenames sorted by decreasing order in word frequency.

## Project Structure

```
grepword/
├── README.md
├── requirements.txt
├── search_word_cli/
│   ├── __init__.py
│   ├── file_parser/
│   │   ├── __init__.py
│   │   └── file_parser.py
│   ├── indexer/
│   │   ├── __init__.py
│   │   └── inverted_index.py
│   └── main.py
├── setup.sh
└── tests/
    ├── __init__.py
    ├── test_data/
    │   ├── sample1.txt
    │   └── sample2.txt
    ├── test_file_parser.py
    └── test_inverted_index.py
```

## Installation

### Installation

Run the setup script to install the tool:

```bash
./setup.sh
```

This will:
1. Install dependencies
2. Create a global `grepword` command
3. Add the command to your PATH

You may need to reload your shell configuration after installation:

```bash
source ~/.bashrc  # Or your specific config file
```

## Running the Tool

Once installed, you can use the `grepword` command from anywhere:

```bash
grepword --word "your-search-word" --path "/path/to/text/files" --filetype "txt"
```

### Options

- `--word`: The word to search for (required)
- `--path`: Directory path to search in (default: current directory)
- `--filetype`: File extension to filter by (default: "txt")

## Example

Search for the word "python" in all markdown files in the current directory:

```bash
grepword --word "test" --path "."
```

Output:
```list
[
  [
    "shakespeare-combined-works.txt",
    [
      26724,
      69662,
      84634,
      104402
    ]
  ],
  [
    "tempest.txt",
    [
      1886
    ]
  ],
]
```

## How It Works

1. The tool scans files in the specified directory with the given file extension
2. It builds an inverted index of all words found in these files
3. When searching for a word, it looks up the index and returns all occurrences
4. Results include the filename and line numbers in reverse sorted order according to search word freq

## Dependencies

- Python 3.6+
- Standard library modules (json, argparse, glob, collections)

## Development

To run tests:

```bash
pytest
```

## License

MIT