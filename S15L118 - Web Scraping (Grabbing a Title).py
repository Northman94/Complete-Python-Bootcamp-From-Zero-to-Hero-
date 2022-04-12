# S15 L116 is in Conspect (General info)

# Open e.g. Wikipedia. RMB on page empty space. View page source. (Win: Ctrl+U)
# e.g. if I want to grab an Image. RMB on it. Inspect(Посмотреть код).
# This will reveal relevant code area.



# https://example.com/

import requests

result = requests.get('https://example.com/')

type(result)
# requests.models.Response

result.text
# '<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n
# <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html;
# charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1"
# />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n
# margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui,
# BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial,
# sans-serif;\n        \n    }\n    div {\n        width: 600px;\n
# margin: 5em auto;\n        padding: 2em;\n        background-color: #fdfdff;\n
# border-radius: 0.5em;\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\n
# }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n
# }\n    @media (max-width: 700px) {\n        div {\n            margin: 0 auto;\n
# width: auto;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n
# <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents.
# You may use this\n    domain in literature without prior coordination or asking for permission.
# </p>\n    <p><a href="https://www.iana.org/domains/example">More information...
# </a></p>\n</div>\n</body>\n</html>\n'


# ^^^ a HTML-code stored as a giant string ^^^
# in order to Parse through it we need to install beautifull soup.

import bs4

soup = bs4.BeautifulSoup(result.text, "lxml") #lxml is a parsing engine

print(soup)
# <!DOCTYPE html>
# <html>
# <head>
# <title>Example Domain</title>
# <meta charset="utf-8"/>
# <meta content="text/html; charset=utf-8" http-equiv="Content-type"/>
# <meta content="width=device-width, initial-scale=1" name="viewport"/>
# <style type="text/css">
#     body {
#         background-color: #f0f0f2;
#         margin: 0;
#         padding: 0;
#         font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
#
#     }
#     div {
#         width: 600px;
#         margin: 5em auto;
#         padding: 2em;
#         background-color: #fdfdff;
#         border-radius: 0.5em;
#         box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
#     }
#     a:link, a:visited {
#         color: #38488f;
#         text-decoration: none;
#     }
#     @media (max-width: 700px) {
#         div {
#             margin: 0 auto;
#             width: auto;
#         }
#     }
#     </style>
# </head>
# <body>
# <div>
# <h1>Example Domain</h1>
# <p>This domain is for use in illustrative examples in documents. You may use this
#     domain in literature without prior coordination or asking for permission.</p>
# <p><a href="https://www.iana.org/domains/example">More information...</a></p>
# </div>
# </body>
# </html>



# Select what is inside <title> tag
# and return a list of relevant tags results

soup.select('title')
# [<title>Example Domain</title>]


soup.select('title')[0].getText()
# 'Example Domain'


site_paragraph = soup.select('p')
type(site_paragraph[0])
# bs4.element.Tag

site_paragraph[0].getText()
# 'This domain is for use in illustrative examples in documents.
# You may use this\n    domain in literature without prior
# coordination or asking for permission.'

