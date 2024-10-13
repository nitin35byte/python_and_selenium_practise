from bs4 import BeautifulSoup
import pandas as pd
import os
w={'link':[] ,'title':[],'price':[] ,'previous_month_bought_count':[],'card_offer':[],'review_rating':[],'delivery_detail':[]}
for file in os.listdir('jeans_data'):
    try:
        file_path = os.path.join("jeans_data", file)
        with open(file_path, 'r' , encoding='utf-8') as f:
            html_doc=f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        t=soup.find('h2')
        title=t.get_text()
        #print(title)

        l=soup.find('a')
        link='https://www.amazon.in' +l['href']

        p=soup.find(class_='a-row a-size-base a-color-base')
        price=p.get_text()

        previous_month_bought_count=soup.find(class_='a-size-base a-color-secondary')
        previous_month_bought_count=previous_month_bought_count.get_text()

        c=soup.find(class_='a-row a-size-base a-color-secondary')
        card_offer=c.get_text()


        r = soup.find(class_='a-row a-size-small')
        review_rating = r.get_text()

        # o = soup.find(class_='a-badge-label-inner')
        # offer_tagline = o.get_text()


        de = soup.find(class_='a-row a-size-base a-color-secondary s-align-children-center')
        delivery_detail = de.get_text()
        w['link'].append(link)
        w['title'].append(title)
        w['price'].append(price)
        w['previous_month_bought_count'].append(previous_month_bought_count)
        w['card_offer'].append(card_offer)
        w['review_rating'].append(review_rating)
        #w['offer_tagline'].append(offer_tagline)
        w['delivery_detail'].append(delivery_detail)
    except Exception as e:
        print(e)


df = pd.DataFrame(data=w)

df.to_csv("jeans_data.csv")
