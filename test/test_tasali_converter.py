import unittest
import os
import json
from tasali_converter import TasaliCrossword


class TestTasaliCrossword(unittest.TestCase):
    def setUp(self):
        pass

    def test_from_json(self):
        json_data = None

        f = open(os.path.dirname(__file__) + "/crossword.json")

        try:
            content = f.read()
            json_data = json.loads(content)
        except FileNotFoundError:
            print(
                "File not found. Please ensure the crossword.json file exists in the correct directory."
            )
        finally:
            f.close()

        crossword = TasaliCrossword.from_json(json_data)

        self.assertIsInstance(crossword, TasaliCrossword)
        self.assertEqual(crossword.nrows, 10)
        self.assertEqual(crossword.ncols, 10)
        self.assertEqual(crossword.words[0].word, "محمودتيمور")
        self.assertEqual(len(crossword.words), 38)
