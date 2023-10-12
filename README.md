# script-that-converts-html-links-to-markdown-files

This is a python script that can take a list of links as arguments on the command line and and convert them to their respective Markdown files. If a link is not found, it is skipped and the [Debian News site page](https://www.debian.org/News/) will be converted to Markdown as a default.
It uses [Pandoc](https://pandoc.org/index.html) which is available on most Linux, Windows and MacOs as shown [here](https://pandoc.org/installing.html).

## Installation and Usage

To use this script:

- clone this git repo using the command below:

```bash
git clone https://github.com/fjkoki/script-that-reads-Debian-News-and-writes-to-markdown.git
```

- move into the directory with the command below:
```bash
cd script-that-reads-Debian-News-and-writes-to-markdown
```

- checkout into the `debian-html-to-wiki-branch-for-list-of-links ` branch with the command below
```bash
git checkout debian-html-to-wiki-branch-for-list-of-links 

```


- run the python script in the directory, adding your desired links as arguments, like this:

```python
python3 debian_news_to_markdown.py https://www.debian.org/News/2023/20231007 https://www.debian.org/News/link2
```

- if successful, you should see something like this:

```bash
Numerous links found. Will try and convert all of them to markdown
successfully created www.debian.org-News-link1.md from https://www.debian.org/News/link1
Numerous links found. Will try and convert all of them to markdown
successfully created www.debian.org-News-link2.md from https://www.debian.org/News/link2
All done check current folder for all markdown files created
```

- if one of the links is not accessible, you will see an error message that looks like this:

```bash
the link https://www.debian.org/News/link3 is inaccessible
we will skip https://www.debian.org/News/link3.
```

- If you do not pass any arguments, i.e. no link is found, you will see the following output:

```bash
No link found.Will convert https://wiki.debian.org/News to markdown only
Markdown file of the Debian News has been created. See the News-current.md file
```
## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)