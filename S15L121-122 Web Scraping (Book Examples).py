
# We used to grab 1 Obj at a time.
# More realistic tasks: grabbing multiple Obj-s / elements,  across multiple Pages.

# The website: https://toscrape.com/index.html
# is specifically designed for web-scraping.

# Let's try to get the title of every book that has a 2-star rating,
# and have a Python list with all their titles.


import requests
import bs4

# We need to find a way to loop through all pages.
# [page-2] part can be modified in this case.

'https://books.toscrape.com/catalogue/page-2.html'

# Home page should be cheked for [page-1]

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

page_num = 10
base_url.format(page_num)
# 'https://books.toscrape.com/catalogue/page-10.html'


# Next we figure out how to scrape every page in this catalogue,
# using that loop and find what tag & class we need.

# [product_pod] holding all info about Obj
# We gonna grab entire [product_pod] for everything on this Web-page
# & filter out by rating


base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format(1))

soup = bs4.BeautifulSoup(res.text,'lxml')
print(soup)


len(soup.select(".product_pod"))
# We found 20 Books on a Page


# This can be done in many ways.
# First: (quick & dirty)
# Lets make it a List for convenience


product = soup.select(".product_pod")

example = product[0]
print(example)

# So we are looking for: <p class="star-rating Two"> & for title
# e.g. title="A Light in the Attic">

str(example)


'star-rating Three' in str(example)
# True

# = - = - = - = - = - = - = - = - = - = - = - = - =
# Second: (more efficient)

#Spaces should be filed with a dot "."
example.select(".star-rating.Three")

# [<p class="star-rating Three">
#  <i class="icon-star"></i>
#  <i class="icon-star"></i>
#  <i class="icon-star"></i>
#  <i class="icon-star"></i>
#  <i class="icon-star"></i>
#  </p>]


example.select(".star-rating.Two")
# []

[] == example.select(".star-rating.Two")
# True


# Next we grab title of a Book:
# We are looking for "<a href"  -tag with  "title" in it.

example.select('a')
# [<a href="a-light-in-the-attic_1000/index.html">
# <img alt="A Light in the Attic" class="thumbnail"
# src="../media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"/></a>,

#  <a href="a-light-in-the-attic_1000/index.html" title="A Light in the Attic">
#  A Light in the ...</a>]


# # We get 2 results above:
# # 1st looks like an image
# # 2nd as a Book title
#
# # They both have links, because we can proceed to the Book page by pressing on Image or Book title.
# # So this means we are going to grab the second link at index [1]

example.select('a')[1]
# <a href="a-light-in-the-attic_1000/index.html" title="A Light in the Attic">
# A Light in the ...</a>


# We can check for 2-stars (string call in, example.select(rating))
# example.select('a')[1]['title']   >>> to grab Book title

#  = - = - = - = - = - = - = - = - = - = - = - = - =
two_star_titles = []

for n in range(1, 51):  # 1-50

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")

    # Alternative way:
    # if 'star-rating Two' in str(book)

    # Better one:
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)





#  If you get no responce Error: Check for Firewall


