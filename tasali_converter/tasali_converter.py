class Word:
    def __init__(self, word, clue, direction, column, row):
        self.word = word
        self.clue = clue
        self.direction = direction
        self.column = column
        self.row = row

    @staticmethod
    def from_json(json_data):
        # Convert JSON data to Word instance
        return Word(
            json_data.get("word", ""),
            json_data.get("clue", ""),
            json_data.get("direction", ""),
            json_data.get("column", 0),
            json_data.get("row", 0),
        )


class TasaliCrossword:
    def __init__(self, nrows, ncols, words):
        self.nrows = nrows
        self.ncols = ncols
        self.words = words
        pass

    @staticmethod
    def from_json(json_data):
        # Convert JSON data to TasaliCrossword instance
        crossword = TasaliCrossword(
            json_data.get("nrows", 0),
            json_data.get("ncols", 0),
            [Word.from_json(word) for word in json_data.get("words", [])],
        )

        # Populate crossword attributes from json_data
        return crossword


class TasaliConverter:
    def __init__(self):
        pass
