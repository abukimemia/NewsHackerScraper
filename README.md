# Building a web scraper using Beautiful Soup python library
## Overview
**Web scraping** is the process of gathering information from the Internet.

## Dependencies
The only dependency is [Pandoc](http://pandoc.org/). Optional functionality to watch the file system and rebuild on changes requires [Watchman](https://facebook.github.io/watchman/). Optional functionality to serve and preview the files locally uses [Python 3](https://docs.python.org/3/library/http.server.html).

- [Pandoc](http://pandoc.org/), a universal document converter
- [Watchman](https://facebook.github.io/watchman/), a file watching service
- [Python 3](https://docs.python.org/3/library/http.server.html), for `http.server`

Installation instructions vary depending on your system. See the linked websites for more information.


## Usage
1. First, we will create a folder in the terminal called `MarkDown`:
   ```batchfile 
   $ mkdir MarkDown
   ```
then enter that folder:
   ```batchfile
   $ cd MarkDown
   ```
Copy these files in your `MarkDown` folder.

2. Write your content in `index.md`

   * Be sure to adjust the information like the `title` and `author` at the top of the file
   * Start a new slide with `#`

3. Run `make watch` to build the site and watch for changes.

**NB: If you just want to preview it and don't want to install Watchman, run `python -m http.server` in `src/`.**

4. View the presentation at 
```
http://127.0.0.1:8000.
```
## Credits
This work is a result of following @jez on [Github](https://github.com/jez).

For more information and resources on markdown templates, please check out his work at [pandoc-starter](https://github.com/jez/pandoc-starter)

Thank you @jez!!

