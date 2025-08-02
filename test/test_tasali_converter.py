import unittest
import os
import json
from tasali_converter import TasaliCrossword


class TestTasaliCrossword(unittest.TestCase):
    def setUp(self):
        f = open(os.path.dirname(__file__) + "/crossword.json")

        try:
            content = f.read()
            self.json_data = json.loads(content)
        except FileNotFoundError:
            print(
                "File not found. Please ensure the crossword.json file exists in the correct directory."
            )
        finally:
            f.close()

    def test_from_json(self):
        crossword = TasaliCrossword.from_json(self.json_data)

        self.assertIsInstance(crossword, TasaliCrossword)
        self.assertEqual(crossword.nrows, 10)
        self.assertEqual(crossword.ncols, 10)
        self.assertEqual(crossword.words[0].word, "محمودتيمور")
        self.assertEqual(len(crossword.words), 38)

    def test_word_to_xpuzzle(self):
        crossword = TasaliCrossword.from_json(self.json_data)

        word = crossword.words[0]

        xpuzzle_word = crossword.word_to_xpuzzle(word)

        self.assertIsInstance(xpuzzle_word, dict)
        self.assertEqual(xpuzzle_word["x"], 0)
        self.assertEqual(xpuzzle_word["y"], 0)
        self.assertEqual(xpuzzle_word["word"], "محمودتيمور")
        self.assertEqual(xpuzzle_word["squares"], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

        vword = next(
            (w for w in crossword.words if w.direction == "column"),
            None,
        )

        xpuzzle_word = crossword.word_to_xpuzzle(vword)

        self.assertIsInstance(xpuzzle_word, dict)
        self.assertEqual(xpuzzle_word["x"], 0)
        self.assertEqual(xpuzzle_word["y"], 0)
        # self.assertEqual(xpuzzle_word["word"], "محمودتيمور")
        self.assertEqual(
            xpuzzle_word["squares"], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        )

        vword = next(
            (w for w in crossword.words if w.word == "رمبراندت"),
            None,
        )

        xpuzzle_word = crossword.word_to_xpuzzle(vword)

        self.assertIsInstance(xpuzzle_word, dict)
        self.assertEqual(xpuzzle_word["x"], 0)
        self.assertEqual(xpuzzle_word["y"], 9)
        self.assertEqual(xpuzzle_word["word"], "رمبراندت")
        self.assertEqual(xpuzzle_word["squares"], [9, 19, 29, 39, 49, 59, 69, 79])

    def test_to_xpuzzle(self):
        pass


class TestWord(unittest.TestCase):
    pass
