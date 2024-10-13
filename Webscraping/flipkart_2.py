from bs4 import BeautifulSoup
import pandas as pd
import os
w={'link':[],'title':[] ,'specification':[],'rating_review':[],'price':[],'test_offer':[],'off_percentage':[]}
for file in os.listdir("data1"):
    file_path = os.path.join("data1", file)
    with open(file_path, 'r', encoding='utf-8') as f:
        html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    try:
        t = soup.find(class_="KzDlHZ")
        title = t.get_text()  # Extract text if element is foun

        s = soup.find(class_='G4BRas')
        specification = s.get_text()

        r = soup.find(class_='_5OesEi')
        rating_review = r.get_text()

        p = soup.find(class_='hl05eU')
        price = p.get_text()

        #
        test_offer = soup.find(class_='M4DNwV')
        test_offer = test_offer.get_text()

        off_percentage = soup.find(class_='UkUFwK')
        off_percentage = off_percentage.get_text()


        l = soup.find("a")
        link = 'https://www.flipkart.com' + l['href']
        w['link'].append(link)
        w['title'].append(title)
        w['specification'].append(specification)
        w['rating_review'].append(rating_review)
        w['price'].append(price)
        w['test_offer'].append(test_offer)
        w['off_percentage'].append(off_percentage)

    except Exception as e:
        print(e)

df=pd.DataFrame(data = w)
df.to_csv('flipkart_laptop_data.csv')