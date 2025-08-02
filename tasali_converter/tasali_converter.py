from xword_converter import Puzzle


class Word:
    def __init__(self, word, clue, direction, column, row):
        self.word = word
        self.clue = clue
        self.direction = direction
        self.column = column
        self.row = row

    @staticmethod
    def from_json(nrows, ncols, json_data):
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
        nrows = json_data.get("nrows", 0)
        ncols = json_data.get("ncols", 0)

        return TasaliCrossword(
            nrows,
            ncols,
            [Word.from_json(nrows, ncols, word) for word in json_data.get("words", [])],
        )

    def to_xpuzzle(self):
        grid = [""] * self.nrows * self.ncols
        for word in self.words:
            if word.direction == "row":
                for i in range(len(word.word)):
                    grid[word.row * self.ncols + (word.column + i)] = word.word[i]
            elif word.direction == "column":
                for i in range(len(word.word)):
                    grid[(word.row + i) * self.ncols + word.column] = word.word[i]

        # fill empty squares with "."
        for i in range(len(grid)):
            if grid[i] == "":
                grid[i] = "."

        across_clues = [
            self.word_to_xpuzzle(word) for word in self.words if word.direction == "row"
        ]

        down_clues = [
            self.word_to_xpuzzle(word)
            for word in self.words
            if word.direction == "column"
        ]

        dimensions = [self.nrows, self.ncols]

        return {
            "grid": grid,
            "across_clues": across_clues,
            "down_clues": down_clues,
            "dimensions": dimensions,
        }

    def word_to_xpuzzle(self, word):
        # generate row squares
        squares = range(
            self.ncols * word.row + word.column,
            self.ncols * word.row + word.column + len(word.word),
        )

        if word.direction == "column":
            squares = range(
                self.ncols * word.row + word.column,
                self.ncols * len(word.word) + word.row + 1,
                self.ncols,
            )

        return {
            "x": word.row,
            "y": word.column,
            "clue": word.clue,
            "word": word.word,
            "squares": list(squares),
        }


class TasaliConverter:
    def __init__(self):
        pass
