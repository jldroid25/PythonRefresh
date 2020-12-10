
#--------- Web Crawling in python -------------#
'''
1- pip install 'requests' module

2- in Ipython interpreter >>> import requests 

2 >>> response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch'
3 >>> print(response.text)
4 >>> print(type(response.text))
5 >>> print(type(response.json()))


-------- Using Beautifull Soup library to parse HTML -----------
>>> from bs4 import BeautifulSoup

>>> import requests

>>> response = requests.get('https://en.wikipedia.org')

>>> html = response.test

>>> print(html)

# Use the BeautifulSoup to parse the html
>>> soup = BeautifulSoup(html, 'html.parser')

>>> soup.title # get the page title

>>> soup.p  # get a paragraph

>>> soup.p.a # get a link in a paragraph

>>> for link in soup.find_all('a') #Get all the links in paragraph
         print(link.get('href'))

# ---> see library documentation for more info/tutorial
'''