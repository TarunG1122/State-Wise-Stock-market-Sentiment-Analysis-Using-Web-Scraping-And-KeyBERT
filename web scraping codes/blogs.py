# coding=utf-8
# imports libraries of python
from PIL import Image
import pytesseract
from pytesseract import image_to_string
import requests
from io import BytesIO
import sys
import re
from selenium import webdriver
from time import sleep
import time
from selenium.common.exceptions import StaleElementReferenceException


def hasXpath(xpath):
    try:
        if (wd1.find_element_by_xpath(xpath)):
            return True
    except:
        return False

def hasXpath1(xpath):
	try:
		if (wd1.find_element_by_xpath(xpath)):
			return True
	except:
		return False

wd = webdriver.Chrome()
wd.get('https://www.social-searcher.com/google-social-search/')

abc=wd.find_elements_by_xpath('//*[@class="google-social-option"]')

for i in range(1,len(abc)):
	abc[i].click()

keyword="stock market fraud"
f=open(keyword+".txt",'wb')

key=wd.find_element_by_id('googlesearchinput')
key.send_keys(keyword) 

button=wd.find_element_by_class_name('main-search')
button.click()

get_social_media=wd.find_elements_by_xpath('//iframe[@class="cse-iframe"]')
links=[x.get_attribute("src") for x in get_social_media]
for i in links:
	wd.get(i)
	sleep(5)
	arr_post=[]
	#For links of facebook
	if "facebookcse" in i:
		j=1
		while(j<=10):
			posts=wd.find_elements_by_xpath('//div[@class="gsc-webResult gsc-result"]/div/div/div/a')
			links_for_post=[x.get_attribute("data-ctorig") for x in posts]
			wd1 = webdriver.Chrome()
			for each_link in links_for_post:
				wd1.get(each_link)
				sleep(3)
				if hasXpath('//div[@class="_5pbx userContent _3576"]'):
					content=wd1.find_element_by_xpath('//div[@class="_5pbx userContent _3576"]')
					post_of_user=content.text
					arr_post.append(post_of_user)
			wd1.close()
			j=j+1
			page_numbers=wd.find_elements_by_xpath('//div[@class="gsc-cursor-page"]')
			for n in range(0,len(page_numbers)):
				if (page_numbers[n].text==str(j)):
					#print(j)
					page_numbers[n].click()
					break
			sleep(3)
	
	#For links of twitter
	elif "twittercse" in i:
		j=1
		while(j<=10):
			posts=wd.find_elements_by_xpath('//div[@class="gsc-webResult gsc-result"]/div/div/div/a')
			links_for_post=[x.get_attribute("data-ctorig") for x in posts]
			wd1 = webdriver.Chrome()
			#print(links_for_post)
			for each_link in links_for_post:
				wd1.get(each_link)
				sleep(3)
				if hasXpath('//div[@class="js-tweet-text-container"]'):
					content=wd1.find_element_by_xpath('//div[@class="js-tweet-text-container"]')
					post_of_user=content.text
					arr_post.append(post_of_user)
			wd1.close()
			j=j+1
			page_numbers=wd.find_elements_by_xpath('//div[@class="gsc-cursor-page"]')
			for n in range(0,len(page_numbers)):
				if (page_numbers[n].text==str(j)):
					#print(j)
					page_numbers[n].click()
					break
			sleep(3)

	# elif "googlepluscse" in i:
	# 	j=1
	# 	while(j<=10):
	# 		posts=wd.find_elements_by_xpath('//div[@class="gsc-webResult gsc-result"]/div/div/div/a')
	# 		links_for_post=[x.get_attribute("data-ctorig") for x in posts]
	# 		wd1 = webdriver.Chrome()
	# 		print(links_for_post)
	# 		for each_link in links_for_post:
	# 			wd1.get(each_link)
	# 			sleep(3)
	# 			if hasXpath('//div[@class="js-tweet-text-container"]'):
	# 				content=wd1.find_element_by_xpath('//div[@class="js-tweet-text-container"]')
	# 				post_of_user=content.text
	# 				arr_post.append(post_of_user)
	# 		wd1.close()
	# 		j=j+1
	# 		page_numbers=wd.find_elements_by_xpath('//div[@class="gsc-cursor-page"]')
	# 		for n in range(0,len(page_numbers)):
	# 			if (page_numbers[n].text==str(j)):
	# 				print(j)
	# 				page_numbers[n].click()
	# 				break
	# 		sleep(3)

	#For links of instagram
	elif "instagramcse" in i:
		j=1
		while(j<=10):
			posts=wd.find_elements_by_xpath('//div[@class="gsc-webResult gsc-result"]/div/div/div/a')
			links_for_post=[x.get_attribute("data-ctorig") for x in posts]
			wd1 = webdriver.Chrome()
			#print(links_for_post)
			for each_link in links_for_post:
				wd1.get(each_link)
				sleep(3)
				if hasXpath('//div[@class="C4VMK"]'):
					content=wd1.find_element_by_xpath('//div[@class="C4VMK"]')
					post_of_user=content.text
					arr_post.append(post_of_user)
			wd1.close()
			j=j+1
			page_numbers=wd.find_elements_by_xpath('//div[@class="gsc-cursor-page"]')
			for n in range(0,len(page_numbers)):
				if (page_numbers[n].text==str(j)):
					#print(j)
					page_numbers[n].click()
					break
			sleep(3)

	#For links of Linkedin
	elif "linkedincse" in i:
		j=1
		while(j<=10):
			posts=wd.find_elements_by_xpath('//div[@class="gsc-webResult gsc-result"]/div/div/div/a')
			links_for_post=[x.get_attribute("data-ctorig") for x in posts]
			wd1 = webdriver.Chrome()
			#print(links_for_post)
			for each_link in links_for_post:
				wd1.get(each_link)
				sleep(3)
				if hasXpath('//p'):
					pars=wd1.find_elements_by_xpath('//p')
					for paragraphs in pars:
						if (paragraphs.text!=''):
							arr_post.append(paragraphs.text)
			wd1.close()
			j=j+1
			page_numbers=wd.find_elements_by_xpath('//div[@class="gsc-cursor-page"]')
			for n in range(0,len(page_numbers)):
				if (page_numbers[n].text==str(j)):
					#print(j)
					page_numbers[n].click()
					break
			sleep(3)

	#For links of Pin Interest
	elif "pinterestcse" in i:
		j=1
		while(j<=10):
			posts=wd.find_elements_by_xpath('//div[@class="gsc-webResult gsc-result"]/div/div/div/a')
			links_for_post=[x.get_attribute("data-ctorig") for x in posts]			
			#print(links_for_post)
			for each_link in links_for_post:
				wd1 = webdriver.Chrome()
				wd1.get(each_link)
				sleep(3)
				if hasXpath('//button[@class="RCK Hsu mix Vxj aZc GmH adn a_A gpV hNT iyn BG7 NTm KhY"]'):
					butt=wd1.find_element_by_xpath('//button[@class="RCK Hsu mix Vxj aZc GmH adn a_A gpV hNT iyn BG7 NTm KhY"]')
					butt.click()
					window_name = wd1.window_handles[1]
					wd1.switch_to.window(window_name=window_name)
					sleep(3)
				if hasXpath('//p'):
					pars=wd1.find_elements_by_xpath('//p')
					for paragraphs in pars:
						if (paragraphs.text!=''):
							arr_post.append(paragraphs.text)
				wd1.close()
			j=j+1
			page_numbers=wd.find_elements_by_xpath('//div[@class="gsc-cursor-page"]')
			for n in range(0,len(page_numbers)):
				if (page_numbers[n].text==str(j)):
					#print(j)
					page_numbers[n].click()
					break
			sleep(3)

	
	#print(arr_post)
	#print(len(arr_post))
	arr_post=list(dict.fromkeys(arr_post))
	#print(len(arr_post))
	for i in range(0,len(arr_post)):
		f.write((arr_post[i]).encode('utf-8'))
		f.write(('\n\n').encode('ascii'))
wd.close()

