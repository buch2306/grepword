import collections


# Builds and stores an inverted index from file content.
class InvertedIndex:
    def __init__(self, files):
        self.inverted_index = self.build_index(files)

    # Cleans a word by removing trailing non-alphanumeric characters.
    # Returns a tuple: (cleaned_word, is_valid)
    def clean_word(self, word):
        index = 0
        found_non_alnum = False
        for index, char in enumerate(word):
            if not char.isalnum():
                found_non_alnum = True
                non_alnum_index = index
                break
        if found_non_alnum:
            for index in range(non_alnum_index + 1, len(word)):
                if word[index].isalnum():
                    return (
                        "",
                        False,
                    )  # Word has internal alphanum after punctuation — discard
            return word[:non_alnum_index], True  # Strip punctuation from end

        return word, True  # Word is clean

    # Sorts occurrences of each word by frequency (descending).
    def sort_inverted_index(self, inverted_index):
        for word in inverted_index:
            inverted_index[word].sort(key=lambda x: x[1], reverse=True)
        return inverted_index

    # Strips frequency information from the index; keeps only filename and line numbers.
    def filter_inverted_index(self, inverted_index):
        for word in inverted_index:
            inverted_index[word] = [
                [filename, line_numbers]
                for filename, _, line_numbers in inverted_index[word]
            ]
        return inverted_index

    # Builds the inverted index: maps words to files and line numbers where they appear.
    def build_index(self, files):
        inverted_index = collections.defaultdict(list)
        for file, file_data in files.items():
            file_data_split_by_lines = file_data.split("\n")
            word_file_dict = collections.defaultdict(
                lambda: [0, []]
            )  # [frequency, [line_numbers]]
            for line_counter, line in enumerate(file_data_split_by_lines):
                word_dict = collections.defaultdict(int)
                words_split = line.split(" ")
                for word in words_split:
                    if word == "":
                        continue
                    cleaned_word, is_clean = self.clean_word(word.lower())
                    if is_clean:
                        word_dict[cleaned_word] += 1
                for word in word_dict:
                    word_file_dict[word][0] += word_dict[word]
                    word_file_dict[word][1].append(line_counter + 1)

            for word in word_file_dict:
                inverted_index[word].append(
                    [file, word_file_dict[word][0], word_file_dict[word][1]]
                )

        sorted_inverted_index = self.sort_inverted_index(inverted_index)
        final_inverted_index = self.filter_inverted_index(sorted_inverted_index)
        return final_inverted_index
