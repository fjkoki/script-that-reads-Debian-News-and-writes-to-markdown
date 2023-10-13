# script-that-reads-Debian-News-and-writes-to-markdown

This is a python script that reads the [Debian News site page](https://www.debian.org/News/) and converts it to a Markdown file.  
It uses [Pandoc](https://pandoc.org/index.html) which is available on most Linux, Windows and MacOs as shown [here](https://pandoc.org/installing.html).

## Installation and use

To use this script
- ensure that Pandoc is installed in your system if not, install it as per the information [here](https://pandoc.org/installing.html).

- clone this git repo using the command below

```bash
git clone https://github.com/fjkoki/script-that-reads-Debian-News-and-writes-to-markdown.git
```
- move into the directory with the command below
```bash
cd script-that-reads-Debian-News-and-writes-to-markdown
```
- run the python script in the directory with the command below
```python
python3 debian_news_to_markdown.py
```
- if successful, you should see the output below
```bash
Markdown file of the Debian News has been created. See the News-current.md file
```

- if not successful, read the error message raised and act accordingly

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)