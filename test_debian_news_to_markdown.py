from debian_news_to_markdown import read_debian_news_with_pandoc_and_write_to_markdown
from unittest import TestCase, main, skipUnless
from unittest.mock import MagicMock
import shutil
from ddt import ddt, data

@ddt
class TestDebianNewsToMarkdown(TestCase):

    @skipUnless(shutil.which('pandoc'), '/usr/bin/pandoc')
    def test_read_debian_news_with_pandoc_and_write_to_markdown_success_with_no_cli_args(self):
        debian_links = None
        actual_return_code = read_debian_news_with_pandoc_and_write_to_markdown(debian_links)
        self.assertIsNone(actual_return_code)
    
    @skipUnless(shutil.which('pandoc'),'/usr/bin/pandoc')
    def test_read_debian_news_with_pandoc_and_write_to_markdown_exception_caused_by_unknown_factor(self):
        read_debian_news_with_pandoc_and_write_to_markdown = MagicMock(side_effect=Exception("Something unexpected happened. Please try again"))
        with self.assertRaises(Exception) as context:
            read_debian_news_with_pandoc_and_write_to_markdown()
        self.assertTrue("Something unexpected happened. Please try again" in str(context.exception))
    
    @skipUnless(shutil.which('pandoc'),'/usr/bin/pandoc')
    @data(["script-name", "https://www.debian.org/News/2023/2023100702", "https://www.debian.org/News/2023/20231007"])
    def test_read_debian_news_with_pandoc_and_write_to_markdown_success_with_expected_list_of_links(self, value):
        self.assertIsNone(read_debian_news_with_pandoc_and_write_to_markdown(value))

    @skipUnless(shutil.which('pandoc'),'/usr/bin/pandoc')
    @data(["script-name", 2, "https://www.debian.org/News/2023/20231007", "www-my-name-is"])
    def test_read_debian_news_with_pandoc_and_write_to_markdown_success_with_random_list_of_links(self, value):
        self.assertIsNone(read_debian_news_with_pandoc_and_write_to_markdown(value))
    
    @skipUnless(shutil.which('pandoc'),'/usr/bin/pandoc')
    @data(["script-name", "https://github.com/", "https://about.gitlab.com/"])
    def test_read_debian_news_with_pandoc_and_write_to_markdown_success_with_unexpected_list_of_links(self, value):
        self.assertIsNone(read_debian_news_with_pandoc_and_write_to_markdown(value))

if __name__ == "__main__":
    main()