import os
import unittest


def analyze_text(filename):
    return 4


class TextAnalysisTests(unittest.TestCase):
    """tests for analyze_text() function."""

    def setUp(self):
        """Fixture that creates a file for text method to use."""
        self.filename = 'sample_file.txt'
        with open(self.filename, 'w') as f:
            f.write("random text ... random text")

    def tearDown(self):  # will run after every test case
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        """Basic test to check if function runs."""
        analyze_text(self.filename)

    def test_line_count(self):
        """Check that line count is correct"""
        self.assertEqual(analyze_text(self.filename), 4)


if __name__ == 'main':
    unittest.main()
