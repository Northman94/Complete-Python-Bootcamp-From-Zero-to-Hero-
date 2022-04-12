
# We will grab a table with list of paragraphs + an Individual element.

import requests

# First get the request
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')


import bs4      #(will be at the page top)

soup = bs4.BeautifulSoup(res.text, "lxml")


print(soup.select('.toctext'))
# [<span class="toctext">Early life and education</span>,
#  <span class="toctext">Career</span>,
#  <span class="toctext">World War II</span>,
#  <span class="toctext">UNIVAC</span>,
#  <span class="toctext">COBOL</span>,
#  <span class="toctext">Standards</span>,
#  <span class="toctext">Retirement</span>,
#  <span class="toctext">Post-retirement</span>,
#  <span class="toctext">Anecdotes</span>,
#  <span class="toctext">Death</span>,
#  <span class="toctext">Dates of rank</span>,
#  <span class="toctext">Awards and honors</span>,
#  <span class="toctext">Military awards</span>,
#  <span class="toctext">Other awards</span>,
#  <span class="toctext">Legacy</span>,
#  <span class="toctext">Places</span>,
#  <span class="toctext">Programs</span>,
#  <span class="toctext">In popular culture</span>,
#  <span class="toctext">Grace Hopper Celebration of Women in Computing</span>,
#  <span class="toctext">See also</span>,
#  <span class="toctext">Notes</span>,
#  <span class="toctext">Obituary notices</span>,
#  <span class="toctext">References</span>,
#  <span class="toctext">Further reading</span>,
#  <span class="toctext">External links</span>]


print( soup.select('.toctext')[0] )
# <span class="toctext">Early life and education</span>


first_item = soup.select('.toctext')[0]
print(first_item.text)
# 'Early life and education'



# If I want to print all list:

for item in soup.select('.toctext'):
    print(item.text)

# Early life and education
# Career
# World War II
# UNIVAC
# COBOL
# Standards
# Retirement
# Post-retirement
# Anecdotes
# Death
# Dates of rank
# Awards and honors
# Military awards
# Other awards
# Legacy
# Places
# Programs
# In popular culture
# Grace Hopper Celebration of Women in Computing
# See also
# Notes
# Obituary notices
# References
# Further reading
# External links











