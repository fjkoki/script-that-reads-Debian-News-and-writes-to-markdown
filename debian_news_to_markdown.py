"""This script reads the debian news site found at https://wiki.debian.org/News and converts it to markdown with pandoc"""
import subprocess
import shlex


def read_debian_news_with_pandoc_and_write_to_markdown():
    """
    reads online debian news and writes to markdown
    Should execute only when pandoc is found in system
    """
    pandoc_cmd = "pandoc --standalone --read=html https://www.debian.org/News/ -o News-current.md"
    write_to_markdown = subprocess.run(shlex.split(pandoc_cmd))

    if write_to_markdown.returncode != 0:
        raise Exception("Something unexpected happened. Please try again")
    print("Markdown file of the Debian News has been created. See the News-current.md file")

def main():
    read_debian_news_with_pandoc_and_write_to_markdown()

if __name__ == "__main__":
    main()