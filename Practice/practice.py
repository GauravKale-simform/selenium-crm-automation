import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://ui.cogmento.com/")
# driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys('gauravkale.sinhgad@gmail.com')
# driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys('Royal@12345')
# driver.find_element(By.XPATH,"//div[@class='ui fluid large blue submit button']").click()
# time.sleep(10)
# hover_element = driver.find_element(By.XPATH,"//span[normalize-space()='Calls']")
# action = ActionChains(driver)
# action.move_to_element(hover_element).perform()
# clickable_element = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='main-nav']//div[8]//button[1]//i[1]")))
# clickable_element.click()
# driver.find_element(By.XPATH,"//label[normalize-space()='Call Script']").click()
# time.sleep(5)
# driver.execute_script("window.scrollBy(0, 1000);")
# time.sleep(5)
# element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='divider default text' and @role='alert' and text()='Search']")))
# element.send_keys('Ramesh')
# driver.find_element(By.XPATH,"//div[@class='divider default text' and @role='alert' and text()='Search']").send_keys('Ramesh')
# time.sleep(15)
# driver.find_element(By.XPATH,"//div[@name='participants'] //input[@aria-autocomplete='list']").send_keys('Manager')
# time.sleep(10)
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
## ##########################################
#
# str1 = str(input("Enter a string of integer:"))
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

# str1 = 'gaurav'
# for i in range(len(str1)):
#     for j in range(len(str1) - i):
#         print('',str1[j],end='')
#     print()

# ############################################

# for i in range(1,6):
#     print('*' * i)
# for j in range(5,0,-1):
#     print('*' * j)
# print()
# ############### Right side triangle ######################
# for i in range(1,6):
#     for j in range(5-i):
#         print(' ', end=' ')
#     for k in range(i):
#         print('*',end=' ')
#     print()

# ############### Pyramid Start Pattern ##############################

# for i in range(1,6):
#     for j in range(5-i):
#         print('', end=' ') #### here is the difference
#     for k in range(i):
#         print('*',end=' ')
#     print()

# ############## New Pattern Pyramid ###############################

# for i in range(1,4):
#     for j in range(5-i):
#         print(' ',end=' ')
#     for k in range(2 * i - 1):
#         print('*',end=' ')
#     print()
# ############################################
# num = 1
# for i in range(1,6):
#     for j in range(i):
#         print(i,end=' ')
#         num += 1
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
# print(f'Occurance of letter {char} in given string:-',cnt)

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
#
# str1 = 'it is a beautiful world'
# str_split = str1.split()
# str2 = []
# for i in str_split:
#     str2.append(i[::-1])
# rev_str1 = ' '.join(str2)
# print(rev_str1)
########################################################################################################################
# for i in range(1,6):
#     for j in range(i):
#         print('*',end=' ')
#     print()
########################################################################################################################
# for i in range(1,4):
#     for j in range(5-i):
#         print(' ',end=' ')
#     for k in range(2 * i - 1):
#         print('*',end=' ')
#     print()
########################################################################################################################
# num = 1
# for i in range(1,6):
#     for j in range(i):
#         print(num,end='')
#         num += 1
#     print()
# ######################################################################################################################
# a = ('radar ')
# updated_a = a.strip()
# rev_a = updated_a[::-1]
# if updated_a == rev_a:
#     print('string is palindrome')
# else:
#     print('string is not palindrome')
# ######################################################################################################################
# a = 'hello simform has got 4 ratings in best place to work on glassdoor'
# b = 'aeiou'
# vowels = []
# letter = []
# for i in a:
#         if i in b:
#             vowels.append(i)
#         elif i.isalpha():
#             letter.append(i)
# print(len(vowels))
# print(len(letter))
# ######################################################################################################################
# a = 'programming'
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(''.join(b))
# ######################################################################################################################)

# a = list(range(1,11))
# print(a)
# print('Length of list :- ',len(a))
# max_a,min_a = max(a), min(a)
# print(max_a,min_a)
# a.append(15)
# print('List after appending an element :- ',a)
# a.remove(a[2])
# print('After removing the 3rd element :- ',a)
# a.remove(9)
# print('After removing specific element 9',a)
# rev_a = a[::-1]
# print('Reverse of a list :- ',rev_a)
# even_num = []
# for i in range(1,21):
#     if i % 2 == 0:
#         even_num.append(i)
# print('Even numbers from 1 to 20',even_num)
# b = [1,2,3,4,5,2,1,9,8,2,3,4,5,3,2]
# char = [1,2,5,4]
# for i in char:
#     count = b.count(i)
#     print(f'Element {i} is apprearing in list {count} times')
# b = [5,9,3,6,1,4,7,12,65,48,20,67,13,22]
# b.sort(reverse=True)
# print(b)

# ######################################################################################################################

# a = [5, 3, 8, 5, 1, 3, 9, 7, 8, 2, 6, 3, 5, 7, 2, 1]
# without_repeating = []
# for i in a:
#     if i not in without_repeating:
#         without_repeating.append(i)
# print(without_repeating)
# ######################################################################################################################
# Given a list of strings, write a Python program to sort the list based on the length of each string

# strings = ["apple", "banana", "kiwi", "watermelon", "grape", "orange", "blueberry", "fig"]
# sorted_strings = sorted(strings,key=len)
# print(sorted_strings[::-1])
# ######################################################################################################################
#Flatten a nested list into a single list (e.g., [[1, 2], [3, 4]] should become [1, 2, 3, 4]).
# a = [[1,2],[3,4]]
# b = []
# for i in a:
#     for j in i:
#         b.append(j)
# print(b)

# ######################################################################################################################
# Write a program to rotate a list by n positions (e.g., for n=2, [1, 2, 3, 4] becomes [3, 4, 1, 2]).

# a = [1,2,3,4,5,6,7,8,9]
# n = 3
# sorted_a = a[-n:] + a[:-n] #for right rotation and for left rotation remove -
# print(sorted_a)
# ######################################################################################################################
# Given two lists, write a Python program to find the common elements between them without using sets.
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [4, 5, 6, 7, 8, 9]
# common_element = []
# for i in list1:
#     if i in list2 and i not in common_element:
#         common_element.append(i)
# print(common_element)

# common_element = set(list1) & set(list2)
# print(common_element)
#
# union_of_l1_l2 = set(list1) | set(list2)
# print(union_of_l1_l2)
#
# union_all = list1 + list2
# print(union_all)
#
# minus = set(list1) - set(list2)
# print(minus)
# ######################################################################################################################

from itertools import count

import requests
import time

from unicodedata import numeric

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# base_url = 'https://www.flipkart.com/'
# driver = webdriver.Chrome()
# driver.get(base_url)
# driver.maximize_window()
# cart_element = driver.find_element(By.XPATH,"//a[normalize-space()='Cart']")
# if cart_element.is_displayed():
#     driver.save_screenshot("C://Users//gaurav//Desktop//Automation//CRM_Project//ScreenShots.success_flipcard.png")
#     # clickable_element = wait.until(EC.element_to_be_clickable((By.ID, 'clickable_id')))
#     # clickable_element.click()
#     print('Landed on working URL')
# else:
#     print('URL is not working')
# driver.implicitly_wait(2)
# driver.find_element(By.XPATH,"//span[contains(text(),'Mobiles')]").click()
# driver.implicitly_wait(2)
# driver.find_element(By.XPATH,"//a[@title='Mobiles']").click()
# driver.implicitly_wait(2)
#
# mob_under_fifteen = []
# mob_nam = driver.find_elements(By.XPATH,"//div[@class='KzDlHZ']")
# list_of_prices = driver.find_elements(By.XPATH,"//div[@class='Nx9bqj _4b5DiR']")
#
# for i in range(len(mob_nam)):
#     mob_name = mob_nam[i].text
#     price_value = int(list_of_prices[i].text.replace('₹','').replace(',','').strip())
#     if price_value < 15000:
#         mob_under_fifteen.append(mob_name)
# for j in mob_under_fifteen:
#     print(j)
# ############################### API Testing Using REST APIS ################################
# base_url = 'https://fakestoreapi.com//products/category/jewelery'
# response = requests.get(base_url)
# json_data = response.json()
# print(json_data)
# id = []
# title =[]
# price = []
# description = []
# category1 = []
# rating = []
# for i in json_data:
#     id.append(i['id'])
#     title.append(i['title'])
#     price.append(i['price'])
#     description.append(i['description'])
#     category1.append(i['category'])
#     rating.append(i['rating'])
# source_data = {'id':[5, 6, 7, 8],
#                'title':["John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet", 'Solid Gold Petite Micropave ', 'White Gold Plated Princess', 'Pierced Owl Rose Gold Plated Stainless Steel Double'],
#                'price':[690, 168, 9.99, 10.99],
#                'description':["From our Legends Collection, the Naga was inspired by the mythical water dragon that protects the ocean's pearl. Wear facing inward to be bestowed with love and abundance, or outward for protection.", 'Satisfaction Guaranteed. Return or exchange any order within 30 days.Designed and sold by Hafeez Center in the United States. Satisfaction Guaranteed. Return or exchange any order within 30 days.', "Classic Created Wedding Engagement Solitaire Diamond Promise Ring for Her. Gifts to spoil your love more for Engagement, Wedding, Anniversary, Valentine's Day...", 'Rose Gold Plated Double Flared Tunnel Plug Earrings. Made of 316L Stainless Steel'],
#                'category':['jewelery', 'jewelery', 'jewelery', 'diamond'],
#                'rating':[{'rate': 4.6, 'count': 400}, {'rate': 3.9, 'count': 70}, {'rate': 3, 'count': 400}, {'rate': 1.9, 'count': 100}]
#                }
# destination_data = {'id':id,'title':title,'price':price,'description':description,'category':category1,'rating':rating}
#
# for key in source_data.keys():
#     sd_values = source_data[key]
#     dd_values = destination_data[key]
#     for i in range(len(sd_values)):
#         if sd_values[i] != dd_values[i]:
#             print(f'Mismatch In the field of {key}')
#             print(f'Source data {sd_values[i]}')
#             print(f'Destination data {dd_values[i]}')
# ############################### Uploading a file in selenium ################################
# base_url = 'https://the-internet.herokuapp.com/upload'
# driver = webdriver.Chrome()
# driver.get(base_url)
# driver.maximize_window()
# time.sleep(2)
# upload_file = driver.find_element(By.XPATH,"//input[@id='file-upload']")
# file_path = 'C://Users//gaurav//Desktop//timesheet.txt'
# upload_file.send_keys(file_path)
# time.sleep(2)
# driver.find_element(By.ID,"file-submit").click()
# time.sleep(2)
# ############################### Action Chains drag and drop ################################
# base_url = 'xyz'
# source_element = driver.find_element(By.ID,"abc")
# target_element = driver.find_element(By.ID,'pqr')
# actions = ActionChains(driver)
# actions.drag_and_drop(source_element,target_element).perform()
# driver.quit()
#############################################################################################
# str1 = 'asdft12wer323reer332dssd'
# #op = tfdsa12rew323reer332dssd
# digit1 = ''
# char = ''
# for i in str1:
#     if i.isdigit():
#         digit1 += char[::-1] + i
#         char = ''
#     else:
#         char += i
# digit1 += char[::-1]
# print(digit1)
#############################################################################################
# mix_num = [-1,-5,6,'z','a','b','c','s','56',3,2,1,99,55]
# alpha = []
# num = []
# for i in mix_num:
#     if isinstance(i,str) and i.isalpha():
#         alpha.append(i)
#     elif isinstance(i,int) or isinstance(i,str) and i.isdigit():
#         num.append(int(i))
# print(alpha)
# print(sorted(num))
#############################################################################################
# list1 = [1,2,3,[[[[7]]]]],[[1,2]],[[1,2]],[3,4],[[7]]
# #op = [1,2,3,7,1,2,1,2,3,4,7]
# updatelist = []
# for i in list1[0][0:3]:
#     updatelist.append(i)
# for j in list1[0][3][0][0][0]:
#     updatelist.append(j)
# for k in list1[1][0]:
#     updatelist.append(k)
# for l in list1[2][0]:
#     updatelist.append(l)
# for m in list1[3]:
#     updatelist.append(m)
# for n in list1[4][0]:
#     updatelist.append(n)
# print(updatelist)
############################# API Testing ##########################################
# base_url = 'https://reqres.in/api/unknown'
#
# response = requests.get(base_url)
# status_code = response.status_code
# print(status_code)
# json_data = response.json()
# print(json_data)
#
# for i in range(200):
#     response = requests.get(base_url)
#     print(f"Response {i + 1}: {response.status_code}")

############################## Client Interview Scenario (ACA) ##############################################
# base_url = 'https://www.nike.com/t/dunk-low-retro-mens-shoes-5FQWGR/DD1391-103'
# driver = webdriver.Chrome()
# driver.get(base_url)
# driver.maximize_window()
# time.sleep(2)
# driver.find_element(By.XPATH,"//a[@href='/t/dunk-low-retro-mens-shoes-5FQWGR/DD1391-100']").click()
# all_sizes = driver.find_elements(By.XPATH,"//div[@class=' css-pp90vm nds-grid-item']")
# # print(all_sizes)
# for i in all_sizes:
#     if i.is_enabled():
#         i.click()
#         print(i.text)
#     else:
#         print('The shoes is out of stock')
#     break
####################### API Testing Data Comparison ################################################

# base_url = 'https://reqres.in/api/users/'
# response = requests.get(base_url)
# json_data = response.json()
# data = json_data['data']
# actual_data = data[1]
# # print(actual_data)
# excepted_data = {"id": 3,
#     "email": "janet.weaver@reqres.in",
#     "first_name": "Janat",
#     "last_name": "Weaver",
#     "avatar": "https://reqres.in/img/faces/2-image.jpg"}
#
# for key in excepted_data.keys():
#     ex_values = excepted_data[key]
#     ac_values = actual_data[key]
#     if ex_values != ac_values:
#         print(f'Mismatch in the field :- {key}')
#         print(f'Excepted :- {ex_values}')
#         print(f'Actual :- {ac_values}')
# else:
#     print('All fields in the payload are matching')

################# 2nd min or max num from the list ###################################
# numbers = [10, 20, 4, 45, 99, 99]
# min_num = min(numbers)
# updated = []
# for i in numbers:
#     if i != min_num:
#         updated.append(i)
# print(min(updated))





































































