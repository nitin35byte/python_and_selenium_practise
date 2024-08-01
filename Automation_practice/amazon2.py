import pandas as pd

def read_data():
    df=pd.read_excel('amazon_cart_items.xlsx')
    product=df['Item Name'].tolist()
    print(product)

    cart=[]

    # for pro in product:
    #     print(pro)
    for excel in product:
        if excel in cart:
            print("test case pass")
        else:
            print("test case fail")

    file=open("test_file.txt",'r')
read_data()


