"""
This script reads links given to it
and converts them to markdown.

If no link given, it defaults to 
reading https://wiki.debian.org/News
and converts it to markdown
"""
from urllib.request import urlopen
import shutil
import subprocess
import shlex
import sys

def number_of_links_parsed():
    """Returns number of links parsed"""
    if len(sys.argv) > 1:
        print("Numerous links found. Will try and convert all of them to markdown")
        return sys.argv
    print("No link found.Will convert https://wiki.debian.org/News to markdown only")
    return None

def check_if_pandoc_is_installed(debian_news_links=None):
    """Checks if pandoc is installed or else raises error"""
    pandoc_sys_path = shutil.which('pandoc')
    if pandoc_sys_path is None:
        raise Exception("Pandoc not found. Please install Pandoc as per your system")

def read_debian_news_with_pandoc_and_write_to_markdown(debian_news_links=None):
    """
    reads online debian news and writes to markdown
    Should execute only when pandoc is found in system
    """

    if debian_news_links is None:
        pandoc_cmd = "pandoc --standalone --read=html https://www.debian.org/News/ -o News-current.md"
        write_to_markdown = subprocess.run(shlex.split(pandoc_cmd))

        if write_to_markdown.returncode != 0:
            raise Exception("Something unexpected happened. Please try again")
        print("Markdown file of the Debian News has been created. See the News-current.md file")

    if debian_news_links is not None:
        for debian_news_link in debian_news_links[1:]:
            try:
                urlopen(debian_news_link)
            except Exception:
                error_message = f"the link {debian_news_link} is inaccessible"
                skip_message = f"we will skip {debian_news_link}."
                print(error_message)
                print(skip_message)
            else:
                try:
                    markdown_file_name = debian_news_link.split('/')[2] + "-" + debian_news_link.split('/')[3] + "-" + debian_news_link.split('/')[4]  + "-" + debian_news_link.split('/')[5] + ".md"
                except IndexError:
                    error_message = f"the link {debian_news_link} does not match expected format"
                    skip_message = f"we will skip {debian_news_link}."
                    print(error_message)
                    print(skip_message)
                else:
                    pandoc_cmd = f"pandoc --standalone --read=html {debian_news_link} --output={markdown_file_name}"
                    write_to_markdown = subprocess.run(shlex.split(pandoc_cmd))

                    if write_to_markdown.returncode != 0:
                        error_message = f"we could not convert {debian_news_link} to markdown"
                        skip_message = f"we will skip {debian_news_link}. Check after you are done"
                        print(error_message)
                        print(skip_message)
                    print(f'successfully created {markdown_file_name} from {debian_news_link}')
        print("All done check current folder for all markdown files created")

def main():
    """start program execution"""
    check_if_pandoc_is_installed()
    custom_debian_news_links = number_of_links_parsed()
    read_debian_news_with_pandoc_and_write_to_markdown(custom_debian_news_links)

if __name__ == "__main__":
    main()