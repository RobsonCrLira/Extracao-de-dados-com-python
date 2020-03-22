import requests #import o resquest
from bs4 import BeautifulSoup #import o BeautifulSoup
import json

res = requests.get("https://projetos.digitalinnovation.one/blog/")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.find(class_="pagination").find_all('a')

all_pages = []
for link in links:
    page = requests.get(link.get('href'))
    all_pages.append(BeautifulSoup(page.text, 'html.parser'))

all_posts = []

for posts in all_pages:
    posts = posts.find_all(class_="post")
    for post in posts:
        info = post.find(class_="post-content")
        title = info.h2.text
        preview = info.p.text
        author = info.find(class_="post-author").text
        time = info.find(class_="post-date")['datetime']
        img = post.find(class_="wp-post-image")['src']
        all_posts.append({'title': title,
                          'preview': preview,
                          'author': author, 
                          'img': img,
                          'time': time})
        with open('posts.json', 'w') as json_file:
            json.dump(all_posts, json_file, indent=3, ensure_ascii=False)


print("Operação executada com sucesso")