def find_whole_numbers(numbers):
    whole_number =[]
    for number in numbers:
        if isinstance(number,(int,float)) and number >=0 and number == int(number):
            whole_number.append(number)
    return  whole_number

input_numbers = [1.5, 2, -3, 4, 5.0, 6.7, 7, 8.0, -9, 10]
whole_numbers = find_whole_numbers(input_numbers)
print("Whole numbers in the list:", whole_numbers)


my_list=[1,2,3,[45,6],[4,5],6]
total = 0
for i in my_list:
    if type(i) ==list:
        for j in i :
            total +=j

    else:
        total +=i
print(total)

def find_sum(n):
    totall=0

    for i in n:
        if isinstance(i, list):
            totall +=find_sum(i)
        else:
            totall +=i
    return totall
my_list=[1,2,3,[45,6],[4,5],6]
total = find_sum(my_list)
print(total)
