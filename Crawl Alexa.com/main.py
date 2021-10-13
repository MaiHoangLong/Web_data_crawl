from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':

    r = requests.get('https://www.alexa.com/topsites').text
    soup = BeautifulSoup(r, 'lxml')

    for table in soup.find_all('div', class_='td DescriptionCell'):
        domain = table.p.a.text
        with open('domain.json', 'a') as f:
            f.write(f'{domain} \n')
            print(domain)




