import pytest
from grepword.indexer.inverted_index import InvertedIndex
from grepword.file_parser.file_parser import FileParser

# First, we need a function that sets up our test data (i.e., the files to be parsed)


@pytest.fixture
def file_parser():
    # This will point to the test data files
    file_parser = FileParser("tests/test_data/*.txt")
    return file_parser


@pytest.fixture
def inverted_index(file_parser):
    # This will build the inverted index from the file_parser's loaded files
    return InvertedIndex(file_parser.files_to_content_mapping)


def test_inverted_index_indexes_words_correctly(inverted_index):
    # Check if the inverted index contains words like 'hello' and 'world'
    assert "hello" in inverted_index.inverted_index, "'hello' should be indexed"
    assert "world" in inverted_index.inverted_index, "'world' should be indexed"
    assert "test" in inverted_index.inverted_index, "'test' should be indexed"


def test_inverted_index_returns_correct_file_and_line(inverted_index):
    # Check if the inverted index returns correct file and line number for a word
    word = "hello"

    # We expect 'hello' to appear in both sample1.txt and sample2.txt
    result = inverted_index.inverted_index.get(word)
    print(result)
    assert (
        len(result) == 2
    ), f"Expected 'hello' to appear in two files, got {len(result)}"

    # Checking if the line numbers match expectations
    assert [
        "sample1.txt",
        [1, 3],
    ] in result, "'hello' should appear in sample1.txt, lines 1 and 3"
    assert [
        "sample2.txt",
        [1],
    ] in result, "'hello' should appear in sample2.txt, line 1"


def test_inverted_index_word_count(inverted_index):
    # Check if the frequency of words is tracked correctly
    word = "test"

    # We expect 'test' to appear once in both files (since 'this is a test' and 'this is another test' are the lines)
    result = inverted_index.inverted_index.get(word)
    print(result)
    assert (
        len(result) == 2
    ), f"Expected 'test' to appear in two files, got {len(result)}"
    assert result[0][1] == [2], "'test' should appear once in sample1.txt, line 2"
    assert result[1][1] == [2], "'test' should appear once in sample2.txt, line 2"


def test_inverted_index_empty_file(inverted_index):
    # Let's add a test for an empty file scenario
    empty_file_data = {"empty.txt": ""}
    empty_file_inverted_index = InvertedIndex(empty_file_data)

    # Since the file is empty, the inverted index should be empty
    assert (
        not empty_file_inverted_index.inverted_index
    ), "Inverted index should be empty for an empty file"
