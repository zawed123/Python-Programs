from requests import get
while True:
    from bs4 import BeautifulSoup as soup
    word = input('\nEnter the word:- ')
    try:
        res = get(f'https://www.lexico.com/definition/{word}').text
        soup = soup(res,'lxml')
        data = soup.find("div",class_="trg").p.find('span',class_='ind').text
        print(f'WORD:- {word}')
        print(f'MEANING:- {data}')
    except:
        print('Data not available')
