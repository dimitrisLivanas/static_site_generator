import unittest
from unittest.mock import patch, mock_open, call
import os
import main

class TestMain(unittest.TestCase):

    @patch('os.path.exists')
    @patch('os.makedirs')
    @patch('os.remove')
    @patch('os.rmdir')
    @patch('os.listdir')
    @patch('os.walk')
    def test_copy_static(self, mock_walk, mock_listdir, mock_rmdir, mock_remove, mock_makedirs, mock_exists):
        # Setup mock behavior
        mock_exists.return_value = True
        mock_walk.return_value = [
            ('public', ['subdir'], ['file1']),
            ('public/subdir', [], ['file2'])
        ]
        mock_listdir.side_effect = [
            ['file1', 'subdir'],  # First call to listdir for src
            ['file2']             # Second call to listdir for subdir
        ]

        # Mock open to handle file read/write
        with patch('builtins.open', mock_open(read_data="data")) as mock_file:
            main.copy_static('static', 'public')

            # Check if the destination directory was cleaned
            mock_remove.assert_has_calls([call('public/file1'), call('public/subdir/file2')])
            mock_rmdir.assert_called_with('public/subdir')
            mock_makedirs.assert_called_with('public', exist_ok=True)

            # Check if files were copied
            mock_file.assert_has_calls([
                call('static/file1', 'rb'),
                call('public/file1', 'wb'),
                call('static/subdir/file2', 'rb'),
                call('public/subdir/file2', 'wb')
            ], any_order=True)

    def test_extract_title(self):
        # Test with a valid h1 header
        markdown = "# Hello\nThis is a markdown file."
        title = main.extract_title(markdown)
        self.assertEqual(title, "Hello")

        # Test with no h1 header
        markdown = "## Hello\nThis is a markdown file."
        with self.assertRaises(Exception) as context:
            main.extract_title(markdown)
        self.assertTrue("No h1 header found" in str(context.exception))

        # Test with multiple lines and an h1 header
        markdown = "Line 1\n# Title\nLine 3"
        title = main.extract_title(markdown)
        self.assertEqual(title, "Title")

if __name__ == "__main__":
    unittest.main()