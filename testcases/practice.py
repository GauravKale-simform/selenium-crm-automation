# import time
# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://ui.cogmento.com/")
# driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys('gauravkale.sinhgad@gmail.com')
# driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys('Royal@12345')
# driver.find_element(By.XPATH,"//div[@class='ui fluid large blue submit button']").click()
# time.sleep(10)
# hover_element = driver.find_element(By.XPATH,"//span[normalize-space()='Calendar']")
# action = ActionChains(driver)
# action.move_to_element(hover_element).perform()
# clickable_element = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='main-nav']//div[2]//button[1]//i[1]")))
# clickable_element.click()
# driver.find_element(By.XPATH,"//label[normalize-space()='End Date']").click()
# time.sleep(5)
# driver.find_element(By.XPATH,"//input[@name='title']").send_keys("abcdef")
# time.sleep(5)
# driver.find_element(By.XPATH,"//label[text()='Start Date']/following-sibling::div[contains(@class, 'calendarField')]").click()
# time.sleep(5)
# driver.execute_script("window.scrollBy(0, 1000);")
# time.sleep(5)
# driver.find_element(By.XPATH,"//a[normalize-space()='No recurrence. Click to set.']").click()
# time.sleep(5)
# driver.find_element(By.XPATH,"//div[@name='freq']").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//div[@name='freq']//div[3]").click()
# time.sleep(5)
# # driver.find_element(By.XPATH,"//label[normalize-space()='Phone']").click()
# # time.sleep(2)
# # # driver.find_element(By.XPATH,"//span[normalize-space()='Companies']").click()
# # driver.find_element(By.XPATH,"//div[@name='hint']//input[@type='text']").send_keys("India")
# # driver.find_element(By.XPATH,"//div[@class='visible menu transition']//span[@class='text'][normalize-space()='India']").click()
# # time.sleep(2)
# # driver.find_element(By.XPATH,"//input[@placeholder='Number']").send_keys("8888929274")
# # time.sleep(10)
# # #element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".ui.active.visible.fluid.multiple.search.selection.dropdown")))
# # element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='search icon']")))
# # element.send_keys("technology")
# # #driver.execute_script("window.scrollBy(0,1000);")
# # #time.sleep(2)
# # # driver.find_element(By.CSS_SELECTOR,".ui.active.visible.fluid.multiple.search.selection.dropdown").send_keys("technology")
# # # time.sleep(2)
# # # driver.find_element(By.XPATH,"//span[@class='text'][normalize-space()='technology']").click()
# # # time.sleep(20)
# # driver.find_element(By.XPATH,"//div[@name='channel_type']").click() #social channel
# # time.sleep(2)
# # driver.find_element(By.XPATH,"//div[@class='three fields']//div[@class='ui field']//div[3]").click()
# # time.sleep(15)
# # driver.find_element(By.XPATH, "//div[@class='ui field'][.//label[normalize-space()='Social channels']]//div[@class='ui input']//input[@name='value']").send_keys("gauravkale")
# # time.sleep(5)
# # driver.find_element(By.XPATH,"//body/div[@id='ui']/div[@class='ui fluid container']/div[@class='ui fluid container']/div[@id='main-content']/div[@class='ui fluid container ']/div[@class='ui fluid container main-content']/form[@class='ui form segment custom-form-container']/div[7]/div[2]/div[1]/div[1]").click()
# # time.sleep(2)
# # driver.find_element(By.XPATH, "//div[@class='visible menu transition']//div[2]").click()
# # time.sleep(2)
# # driver.find_element(By.XPATH,"//div[@name='status']//i[@class='dropdown icon']").click()
# # time.sleep(2)
# # driver.find_element(By.XPATH, "//div[@class='visible menu transition']//div[7]").click()
# # time.sleep(2)
# # driver.find_element(By.XPATH,"//div[@name='source']//i[@class='dropdown icon']").click()
# # time.sleep(2)
# # driver.find_element(By.XPATH,"//div[@class='visible menu transition']//div[11]").click()
# # time.sleep(2)
# # file_input = driver.find_element(By.XPATH,"//input[@name='image']")
# # file_path = "C:/Users/gaurav/Downloads/indian_flag.png"
# # file_input.send_keys(file_path)
# # time.sleep(10)
#
import copy
from itertools import count
#
# str1 = str(input("Enter a string:"))
# new_str = ""
# for i in range(len(str1)):
#     if str1[i].isdigit():
#         new_str += str1[i-1] * (int(str1[i]) - 1)
#     else:
#         new_str += str1[i]
#
# print(new_str)

# ###################### Gaurav Practice ################################################

# str1 = 'gaurav'
# for i in range(len(str1)+1):
#     for j in range (i):
#         print(str1[j],end=' ')
#     print()

# ##########################################

# str1 = 'gauravk'
# for i in range(1,len(str1)):
#     for j in range(len(str1) - i):
#         print('',str1[j],end='')f
#     print()

# ############################################

# for i in range(1,6):
#     print('*' * i)
# for j in range(5,0,-1):
#     print('*' * j)
# print()
# ############################################

# for i in range(1,6):
#     for j in range(5-i):
#         print(' ', end=' ')
#     for k in range(i):
#         print('*',end=' ')
#     print()

# #############################################

# for i in range(1,6):
#     for j in range(5-i):
#         print('', end=' ') #### here is the difference
#     for k in range(i):
#         print('*',end=' ')
#     print()

# #############################################

# for i in range(1,6):
#     for j in range(i):
#         print('*', end=' ')# * * *
#     print()# * * * *

# ############################################

# my_dict1 = {'name' : 'gaurav', 'address' :'pune','salary' : '5000','dept': 'cse'}
# a = my_dict1.items()
# for key,value in (a):
#     print(f'Keys is:{key} and value is:{value}')

# ############################################

# str1 = 'Gaurav Kale'
# full_name = str1.split()
# first_name = full_name[0]
# last_name = full_name[1]
# print('This is full name:-',str1)
# print('This is first name:-',first_name)
# print('This is last name:-',last_name)
# reverse_last_name = last_name[::-1]
# print('This is reverse of last name:-',reverse_last_name)

# ################# Factroil of given number ############################
# a = int(input('Find the Factroil of :- '))
# result = 1
# for i in range(1,a+1):
#     result *= i
# print(result)
# ################## Fibonacci Serires ###########################
# a = int(input('Find the fib series of number :- '))
# fib = [0,1]
# for i in range(2,a):
#     fib.append(fib[-1] + fib[-2])
# # print(fib)# by using this print O/p is getting in list so to get in integer
# for j in fib:
#     print(j,end=' ')
# ############### Palindrome Check ###############################
# str1 = input('Enter a string :- ')
# # print(str1)
# palindrome = str1[::-1]
# print('Palindrome of enterend string :',palindrome)
# if str1 == palindrome :
#     print('Palindrome is possible')
# else:
#     print('Palindrome is not possible')

# ############# Reverse Of String ################################
# str1 = input('Enter a string :- ')
# reverse_str1 = str1 [::-1]
# print(reverse_str1)
# ############## Check prime number #################################
# a = int(input("Enter a number: "))
# if a > 1:
#     for i in range(2, a):
#         if a % i == 0:
#             print("It is not a prime number")
#             break
#     else:
#         print("Number is prime")
# else:
#     print("Number is not within the range")

# ######## Create a loop that prints all prime numbers between 1 and 50 #####################################
# a = 50
# for i in range(2,a + 1):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         print(i,end=' ')
# ############# # Count occurances of character #################################
# str1 = input('Enter a string:-')
# char = input('Enter a letter:-')
# cnt = str1.count(char)
# print(f'Occurance of letter {char} in {str1} string:-',cnt)

# ##############################################
# a = 'aabbccdefaa'
# chars_to_count = ['a', 'b', 'c']
# for char in chars_to_count:
#     count = a.count(char)
#     print(f'{char} - {count}')
# ############# Addition of 1 - 50 numbers ################################
# a = int(input())
# result = 0
# for i in range(1,a+1):
#     result += i
# print('Addition of 1 to entered numbers :-',result)

# ######### Table of any number ####################################
# a = int(input())
# for i in range(1,11):
#     b = a * i
#     print(b,end=' ')
# ##############################################
# class my_class():
#     def __init__(self):
#         print("This is Cnstructor without parameter: ")
# my_class()
#
# class u_class():
#     def __init__(self,x,y):
#         self.a = x + y
#         print(self.a)
# u_class(7,8)
# ##############################################
# def decorator(func):
#     def dog_barking():
#         print('dog is now Barking')
#     func()
#     print('After barking now Dog is Eating')
#     return dog_barking
# @decorator
# def pet():
#     print('i love dogs')
# pet()
# ##############################################
# def is_anagram(str1, str2):
#     if len(str1) != len(str2):
#         print('The strings have different lengths. They cannot be anagrams.')
#     return False
# sorted_str1 = sorted(str1)
# sorted_str2 = sorted(str2)
# if sorted_str1 == sorted_str2:
#     print("The strings '{}' and '{}'are anagrams.".format(str1,str2))
# else:
#     print("The strings '{}' and '{}' are not anagrams.".format(str1, str2))
# is_anagram('gaurav', 'ravgau')

# ##############################################

# list1 = [0,0,1,1,1,2,2,3,3,4]
# unique1 = []
# for i in list1:
#     if i not in unique1:
#         unique1.append(i)
# print(unique1)

# ##############################################

# def separate_special_chars(text):
#     result = ''
#     for char in text:
# #Check if the character is alphanumeric or whitespace
#         if not char.isalnum() or char.isspace(): #change of not word
#             result += char # If it is, add it to the result string
#     return result
#
# text = "Hello! How are you? I'm doing fine, thank you."
# result = separate_special_chars(text)
# print(result)# Output: Hello How are you Im doing fine thank you
# ##############################################
# str1 = 'A/B$c'
# print('Original string:-',str1)
# a = list('A/B$c')
# op= 'c$B/A'
# reverse_a = a[::-1]
# for j in reverse_a:
#     print(j,end=' ')
# my_str = ''.join(reverse_a)
# print('\n Revrsed string :-',my_str)

# ##############################################
# a = 'abc@#123'
# # list_a = list(a)
# al_num = []
# spe = []
# for i in a:
#     if i.isalnum():
#         al_num.append(i)
#     else:
#         spe.append(i)
# print(al_num,spe)
# ##############################################

# sd = {'id':[1,2,3,4],'name':['a','b','c','d'],'salary':[10,20,30,40],'dept':['a1','a2','a3','a4']}
# td = {'id':[1,2,3,4],'name':['a','jb','cg','d'],'salary':[10,20,30,400],'dept':['a1','a2','a3','a4']}
# for key in sd.keys():
#     sd_values = sd[key]
#     print(sd_values)
#     td_values = td[key]
#     for i in range(len(sd_values)):
#         if sd_values[i] != td_values[i]:
#             print(f'Mismatched data is {key}')
#             print(f'Source data {sd_values[i]}')
#             print(f'Target data {td_values[i]}\n')

# ###############################################