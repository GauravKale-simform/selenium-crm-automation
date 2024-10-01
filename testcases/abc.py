from itertools import count

import requests
import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#
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
































