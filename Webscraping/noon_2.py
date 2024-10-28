from bs4 import BeautifulSoup
import pandas as pd
import os
w={'link':[] ,'product_name_description':[],'price':[] ,'express_delivery':[],'cashback':[],'review_rating':[]}
for file in os.listdir('phone_data'):
    try:
        file_path = os.path.join("noon_phone_data1", file)
        with open(file_path, 'r' , encoding='utf-8') as f:
            html_doc=f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')

        l=soup.find('a')
        link=l['href']


        p = soup.find('a')
        price=p['sc-8df39a2e-0 kXWkOO']
        print(price)
        #
        # pd=soup.find("sc-66eca60f-24 fPskJH")
        # Product_Name_Description=pd.get_text()
        # print(Product_Name_Description)
        #
        # r =soup.find("product-noon-express")
        # express_delivery= r.get_text()
        #
        # c= soup.find("bqmDLu")
        # cashback=c.get_text()
        #
        # rev= soup.find("bLaxTl")
        # review_rating=rev.get_text()
        #
        # w['link'].append(link)
        # w['product_name_description'].append(Product_Name_Description)
        # w['price'].append(price)
        # w['express_delivery'].append(express_delivery)
        # w['cashback'].append(cashback)
        # w['review_rating'].append(review_rating)

    except Exception as e:
        print(e)



# df =pd.DataFrame(data=w)
#
# df.to_csv("noon_smart_phone.csv")
