from bs4 import BeautifulSoup
import requests

def display_menu():

    print("Which of the following task you want to perform?")
    print("------------------------------------------------")
    print("1. Webpage")
    print("2. Wikipedia Page")
    print("------------------------------------------------")



def webpages():

    url = input("Paste a webpage url: ")
    source = requests.get(url)
    s = BeautifulSoup(source.text,'html')
    title = s.find('title')
    print("This is with HTML tags: ",title)
    notags = s.find('h1')
    print(("This is not with HTML tags: ",notags.text))

    links = s.find('a')
    print(links)
    print(links['href'])
    print(links['class'])
    link1 = s.find_all('a')
    link2 = len(link1)
    print("Total links in the webpage: ",link2)

    for i in link1[:6]:
        print(i)

        links2 = link1[1]
        print(links2)
        print()
        print('href is: ',links2['href'])

        div = links2.find('div')
        print(div)
        print()

        h = (div['class'])
        print(h)
        print(type(h))
        print()
        print("Class name of Div is: ","".join(div['class']))


def wikipage():

    url1 = input("Paste a wikipedia page url: ")
    wiki = requests.get(url1)
    s2 = BeautifulSoup(wiki.text,'html')
    print(s2.find(('title')))

    content = s2.find_all('div',class_='toc')

    for i in content:
        print(i.text)


    '''
    To perform this program, we need to have a conditional loop
    '''

while True:

    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        webpages()
    elif choice == '2':
        wikipage()
    else:
        break
