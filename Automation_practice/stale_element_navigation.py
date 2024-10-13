# from selenium import  webdriver
# from selenium.webdriver.common.by import  By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get("https://www.flipkart.com/")
#
#
# element=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Payments")))
# driver.execute_script("arguments[0].scrollIntoView();",element)
# element.click()
# driver.back()
# elementa=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Payments")))
# elementa.click()

def fibb(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a

# Create the generator object
gen = fibb(10)

# Now use next() to get the first value from the generator
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


a= '121'
b = {}

for i in a:
    if i in b :
        b[i] +=1
    else:
        b[i] =1
print(b)


def palindrome(l):

    left  , right=0 , len(l)-1
    while left <right:
        if l[left] != l[right]:
            print("not a palindrome")
            return False
        left +=1
        right -=1
    print("Is palindrome")
    return True
obj = palindrome(a)
print(obj)

print(type(a))

def target_vaue(num , target):
    for i in range(len(num)):
        for j in range(i+1 , len(num)):
            if num[i] +num[j] == target:
                print(f"sum of {num[i]} + {num[j]} is ={target}")
num =[2 , 3 , 6 , 7]
target= 5
obj1=target_vaue(num, target)
print(obj1)