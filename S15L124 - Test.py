
import requests
import bs4
import lxml


# TASK: Use requests library and BeautifulSoup to connect to
# http://quotes.toscrape.com/ and get the HMTL text from the homepage.

qts_link = requests.get('http://quotes.toscrape.com/')

print(qts_link.text) # normaly returns a string


# - = - = - = - = - = - = - = - = - = - = - = - =

# TASK: Get the NAMES of all the AUTHORS on the first page.

import requests
import bs4

qts_link2 = requests.get('http://quotes.toscrape.com/')
soup2 = bs4.BeautifulSoup(qts_link.text, "lxml") #lxml  is a parsing Engine

soup2.select('.author')
# [<small class="author" itemprop="author">Albert Einstein</small>,
#  <small class="author" itemprop="author">J.K. Rowling</small>,
#  <small class="author" itemprop="author">Albert Einstein</small>,
#  <small class="author" itemprop="author">Jane Austen</small>,
#  <small class="author" itemprop="author">Marilyn Monroe</small>,
#  <small class="author" itemprop="author">Albert Einstein</small>,
#  <small class="author" itemprop="author">André Gide</small>,
#  <small class="author" itemprop="author">Thomas A. Edison</small>,
#  <small class="author" itemprop="author">Eleanor Roosevelt</small>,
#  <small class="author" itemprop="author">Steve Martin</small>]

soup2.select('.author')[0].getText()
# 'Albert Einstein'


authors = set()

for item in soup2.select('.author'):
    authors.add(item.text)

print(authors)
# {'Thomas A. Edison', 'Marilyn Monroe', 'J.K. Rowling', 'Eleanor Roosevelt',
# 'Albert Einstein', 'André Gide', 'Jane Austen', 'Steve Martin'}


# - = - = - = - = - = - = - = - = - = - = - = - =

# TASK: Create a list of all the QUOTES on the first page.

qts_link3 = requests.get('http://quotes.toscrape.com/')
soup3 = bs4.BeautifulSoup(qts_link3.text, "lxml") #lxml  is a parsing Engine

quotes_lst = []

for lmt in soup3.select('.text'):
    quotes_lst.append(lmt.text)

# print(quotes_lst)  >>> in one row

for lmt2 in quotes_lst:
    print(lmt2 + "\n")

# “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
#
# “It is our choices, Harry, that show what we truly are, far more than our abilities.”
#
# “There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
#
# “The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”
#
# “Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”
#
# “Try not to become a man of success. Rather become a man of value.”
#
# “It is better to be hated for what you are than to be loved for what you are not.”
#
# “I have not failed. I've just found 10,000 ways that won't work.”
#
# “A woman is like a tea bag; you never know how strong it is until it's in hot water.”
#
# “A day without sunshine is like, you know, night.”



# - = - = - = - = - = - = - = - = - = - = - = - =

# TASK: Inspect the site and use Beautiful Soup to extract the top ten tags
# from the requests text shown on the top right from the home page
# (e.g Love,Inspirational,Life, etc...).
# HINT: Keep in mind there are also tags underneath each quote, try to find
# a class only present in the top right tags, perhaps check the span.

qts_link4 = requests.get('http://quotes.toscrape.com/')
soup4 = bs4.BeautifulSoup(qts_link4.text, "lxml") #lxml  is a parsing Engine

for i in soup4.select('.col-md-4.tags-box  .tag'):
    print(i.text)

# Dot as a space: .col-md-4.tags-box

# love
# inspirational
# life
# humor
# books
# reading
# friendship
# friends
# truth
# simile



# - = - = - = - = - = - = - = - = - = - = - = - =

# TASK: Notice how there is more than one page, and subsequent pages look like this
# http://quotes.toscrape.com/page/2/
# Use what you know about for loops and string concatenation to loop through all the pages
# and get all the unique authors on the website.
# You will need to figure out how to check that your loop is on the last page with quotes.


# Teacher: (when we know amount of pages)

authors3 = set()
base_url3 = 'https://quotes.toscrape.com/page/'

for web_page in range(1, 10):

    mod_url = base_url3 + str(web_page)  # In order to perform Concatination, convertion to a str needed

    req = requests.get(mod_url)

    miso = bs4.BeautifulSoup(req.text, "lxml")

    for item in miso.select('.author'):
        authors3.add(item.text)

print(authors3)

# - = - = - = - = - = - = - = - = - = - = - = - =

# My Solution:

n = 1
unique_authors = set()
base_url = 'https://quotes.toscrape.com/page/{}/'

change_url = requests.get(base_url.format(1))
soupez = bs4.BeautifulSoup(change_url.text, "lxml")

while len(soupez.select('.author')) != 0:

    change_url = requests.get(base_url.format(n))

    soupez = bs4.BeautifulSoup(change_url.text, "lxml")  # lxml  is a parsing Engine

    for j in soupez.select('.author'):
        unique_authors.add(j.text)

    n = n + 1

for p in unique_authors:
    print(p)
