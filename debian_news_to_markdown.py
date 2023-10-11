"""This script reads the debian news site found at https://wiki.debian.org/News and converts it to markdown with pandoc"""
import shutil
import subprocess
import shlex

def check_if_pandoc_is_installed():
    """Checks if pandoc is installed or else raises error"""
    pandoc_sys_path = shutil.which('pandoc')
    if pandoc_sys_path is None:
        raise Exception("Pandoc not found. Please install Pandoc as per your system")
    read_debian_news_with_pandoc_and_write_to_markdown()

def read_debian_news_with_pandoc_and_write_to_markdown():
    """
    reads online debian news and writes to markdown
    Should execute only when pandoc is found in system
    """
    pandoc_cmd = "pandoc --from=html --to=markdown_strict https://wiki.debian.org/News --output=News-current.md"
    write_to_markdown = subprocess.run(shlex.split(pandoc_cmd))

    if write_to_markdown.returncode != 0:
        raise Exception("Something unexpected happened. Please try again")
    print("Markdown file of the Debian News has been created. See the News-current.md file")

def main():
    check_if_pandoc_is_installed()

if __name__ == "__main__":
    main()