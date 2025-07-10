import requests
from bs4 import BeautifulSoup
import csv

url = 'https://quotes.toscrape.com'
urle = ''

allquotes = []
while True:
    response = requests.get(url + urle)
    if response.status_code != 200:
        print(f'{url + urle} could not be resolved')
        break
    else:
        blabla = response.text
        soup = BeautifulSoup(blabla, 'html.parser')
        quotes = soup.find_all('div', class_='quote')

        for quote in quotes:
            text = quote.find('span', class_='text').text.strip()
            author = quote.find('small', class_='author').text.strip()
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            allquotes.append((text, author, ','.join(tags)))

        nextbutton = soup.find('li', class_='next')
        if nextbutton:
            urle = nextbutton.a['href']
        else:
            print('There is not next page')
            break

with open('DemandedQuotes.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['text', 'author', 'tags'])
    writer.writerows(allquotes)
print ('The file DemandedQuotes.csv has been saved.')