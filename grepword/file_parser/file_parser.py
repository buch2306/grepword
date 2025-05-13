import collections
import glob


# Responsible for reading files from a directory and storing their content.
class FileParser:
    def __init__(self, path):
        self.path = path
        self.files_to_content_mapping = self.load_files()

    # Loads all files matching the glob pattern and reads their content.
    def load_files(self):
        file_to_content = collections.defaultdict()
        files = glob.glob(self.path)
        for file in files:
            cleaned_file = file.split("/")[-1]
            file_to_content[cleaned_file] = self.read_file(file)
        return file_to_content

    # Reads the content of a single file and returns it as a string.
    def read_file(self, file):
        actual_file = None
        with open(file, "r") as file_object:
            actual_file = file_object.read()
        return actual_file
