#Creating a python alogrithm to solve the median of a numeric sequence 
import time 
import tqdm
try:
    number_of_numerical_values=int(input("How many numbers do you want in your numerical sequence?:"))
    numbers=[]
    for num in range(number_of_numerical_values):
        enter_num=int(input("number:"))
        numbers.append(enter_num)
    else:
        numbers.sort()
        if number_of_numerical_values%2==0:
            print(f'The median is {(numbers[numbers.index(numbers[-1])//2]+numbers[(numbers.index(numbers[-1])//2)+1])/2}')
        else:
            print(f'The median is {numbers[numbers.index(numbers[-1])//2]}')
except ValueError:
    pass