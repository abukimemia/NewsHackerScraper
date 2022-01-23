# Building a web scraper using Beautiful Soup python library
## Overview
**Web scraping** is the process of gathering information from the Internet. We will implement a python library named [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) to pulling data out of HTML files on a web page. In this project we will be scraping a [n
ews webpage](https://news.ycombinator.com/news) and outputting the following: 
   - A Unique URL link of a news source, 
   - the news title, 
   - the count of votes it has gathered on the news site.

There are challenges faced when scrapping a web page such as:
   - Variety: Every website is different. While you’ll encounter general structures that repeat themselves, each website is unique and will need personal treatment if you want to extract the relevant information.

   - Durability: Websites constantly change. Say you’ve built a shiny new web scraper that automatically cherry-picks what you want from your resource of interest. The first time you run your script, it works flawlessly. But when you run the same script only a short while later, you run into a discouraging and lengthy stack of tracebacks!

## Prerequisites
Please ensure that [Python 3](https://docs.python.org/3/download/) is installed on your development machine. 

Installation instructions vary depending on your system. See the linked website for more information.

## Usage
1. First, we will create a folder in the terminal called `NewsHackerScrap`:
   ```batchfile 
   $ mkdir NewsHackerScrap
   ```
then enter that folder:
   ```batchfile
   $ cd NewsHackerScrap
   ```
2. Clone this repository to this directory

In your terminal, type `git clone`, then paste the URL of this repository i.e.:
   ```shell
   $ git clone https://github.com/abukimemia/NewsHackerScraper.git
   ```

3. Install missing dependencies
Once the code has been cloned into your directory, we will install the missing dependencies onto our project so that it can run successfully. Use the following command in your terminal:
  ```shell 
  $ pip install -r requirements.txt
  ```
 
This process should take a while and once all the dependencies are successfully installed it should be ready to scrape the web page.

4. Run the script
In your terminal in the project's directory, type the following command to run the program:
  ```shell
  $ python3 scrape.py
  ```

This command should scrape the first page of the News Hacker website outputting the results in descending order according to the votes gathered for each news source with the one with the highest votes appearing top of the list.


