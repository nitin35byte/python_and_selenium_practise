from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowhandler=driver.window_handles
print(windowhandler)
title=driver.find_element(By.TAG_NAME,"h3")
print(title.text)
driver.switch_to.window(windowhandler[1])


title1=driver.find_element(By.TAG_NAME,"h3")
print(title1.text)


h =[1,2,3,2,2,1,2,4,41,4,5,6,4]
a = {}
b = []
for i in h:
    if i in a:
        a[i] +=1
    else:
        a[i]=1

for word , count in a.items():
    if count >1:
        b.append(word)
print(b)

print(a)
print(b)

h = 'hellow world'
char_count = {}
duplicates = []

# Count the occurrences of each character
for i in h:
    if i in char_count:
        char_count[i] += 1
    else:
        char_count[i] = 1
for char, count in char_count.items():
    if count > 1:
        duplicates.append(char)

print("Duplicate characters:", duplicates)

print(char_count)
print(duplicates)