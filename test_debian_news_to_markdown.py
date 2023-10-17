from debian_news_to_markdown import read_debian_news_with_pandoc_and_write_to_markdown
from unittest import TestCase, main
from unittest.mock import MagicMock

class TestDebianNewsToMarkdown(TestCase):
    def test_read_debian_news_with_pandoc_and_write_to_markdown(self):
        actual_return_code = read_debian_news_with_pandoc_and_write_to_markdown()
        self.assertIsNone(actual_return_code)

    def test_read_debian_news_with_pandoc_and_write_to_markdown_exception(self):
        read_debian_news_with_pandoc_and_write_to_markdown = MagicMock(side_effect=Exception("Something unexpected happened. Please try again"))
        with self.assertRaises(Exception):
            read_debian_news_with_pandoc_and_write_to_markdown()

if __name__ == "__main__":
    main()