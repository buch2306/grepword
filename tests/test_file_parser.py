from grepword.file_parser.file_parser import FileParser


def test_file_parser():
    file_parser = FileParser("tests/test_data/*.txt")
    assert len(file_parser.files_to_content_mapping) > 0


def test_file_parser_read_file():
    file_parser = FileParser("tests/test_data/sample1.txt")
    content = file_parser.files_to_content_mapping["sample1.txt"]
    assert "hello" in content, "File content doesn't match"
