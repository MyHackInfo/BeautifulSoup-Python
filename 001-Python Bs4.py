import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce,'lxml')
#print(soup)
#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup.title.text)
#print(soup.p)
#print(soup.find_all('p'))

'''
for parag in soup.find_all('p'):
    print(parag.string)
'''

##for parag in soup.find_all('p'):
##    print(parag.text)
## 

#print(soup.get_text())
for url in soup.find_all('a'):
    print(url)
    #print(url.text)
    #print(url.get('href'))
