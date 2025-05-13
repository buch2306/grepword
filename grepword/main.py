import argparse
from grepword.file_parser import file_parser
from grepword.indexer import inverted_index
import json


# Entry point of the CLI tool
def main():
    parser = argparse.ArgumentParser(
        prog="Grep across text files",
        description="Gets the file names and line numbers of a specific word across text files in a directory",
    )
    # Required argument: word to search for
    parser.add_argument(
        "--word",
        help="Search word across text files to get the file names and the line numbers",
        required=True,
    )
    # Required argument: path to the directory containing text files
    parser.add_argument("--path", help="Directory path to text files", required=True)
    # Optional argument: file type to search within (defaults to .txt)
    parser.add_argument(
        "--filetype",
        help="File extension/type to parse (e.g., txt, log, md)",
        default="txt",
    )
    args = parser.parse_args()
    # Construct glob path with file extension filter
    files_path = f"{args.path}/*.{args.filetype}"
    input_word = args.word
    # Read and parse the files
    file_parse = file_parser.FileParser(files_path)
    # Build the inverted index from parsed file content
    lookup_table = inverted_index.InvertedIndex(file_parse.files_to_content_mapping)
    # Print results if word is found; else, notify the user
    if input_word in lookup_table.inverted_index:
        print(json.dumps(lookup_table.inverted_index[input_word], indent=2))
    else:
        print(f"No results found for word: '{input_word}'")


# Script entry point
if __name__ == "__main__":
    main()
