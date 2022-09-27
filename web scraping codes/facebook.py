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



#Defining a function to check the validity of Xpath in the browser
def hasXpath(xpath):
    try:
        if (wd.find_elements_by_xpath(xpath)):
            return True
    except:
        return False

#instantiting chrome browser in such a way that no notification popus up while selenium executes
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
wd = webdriver.Chrome(chrome_options=chrome_options)


#username and password 
#Please enter valid credentials
#Do not disclose it to anyone
usr="########" #Username
pas="#########" #password


#Taking to the log-in page 
wd.get('https://www.facebook.com')

#Automatic Sign in to Facebook with the details provided above
# locate email form by_class_name
username = wd.find_element_by_id('email')
username.send_keys(usr) 
sleep(0.5)

# locate password form by_class_name
passw = wd.find_element_by_id('pass')
passw.send_keys(pas)
sleep(0.5)

# locate submit button by_xpath
sign_in_button = wd.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
print("logged in")

#Enter the keyword you need to search for
keyword=["cars"]

#For loop for multiple keywords
for i in range(0,len(keyword)):

    #Open the file in write mode with the keyword provided
    f=open(keyword[i]+"_facebook.txt","wb") 
    #Entering search page for facebook with the keyword   
    wd.get('https://www.facebook.com/search/posts/?q='+keyword[i]+'&epa=SERP_TAB')

    if (hasXpath('//div[@class="_4f38"]/div/a[4]')):
        allp=wd.find_elements_by_xpath('//div[@class="_4f38"]/div/a[4]')
        see_url = [x.get_attribute("href") for x in allp] 
        wd.get(see_url[0])
        
        j=0
        #Value of J determines how much time scrolling happens to the bottom of page
        while (j<100):
            # Scroll down to bottom so as to load more content
            wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(0.5)
            j=j+1

        if(hasXpath('//div[@class="_6-cp"]')):
            posts=wd.find_elements_by_xpath('//div[@class="_6-cp"]/div/span/a')
            #Takes link of all the posts from the page
            html = [x.get_attribute("href") for x in posts] 
            for p in html:
                #Go to each link individually
                wd.get(p)
                f.write(("Post URL - ").encode('ascii'))
                f.write(p.encode("utf-8"))
                f.write(("\n").encode('ascii'))

                #Taking the user name from the post with the Xpath provided
                if hasXpath('//div[@class="_6a _5u5j _6b"]/h5/span/span/a'):    
                    name=wd.find_element_by_xpath('//div[@class="_6a _5u5j _6b"]/h5/span/span/a')
                    name_user=name.text.encode("utf-8")
                    f.write(("User Name - ").encode('ascii'))
                    f.write(name_user)
                    f.write(("\n").encode('ascii'))
                
                #Taking the date from the post with the Xpath provided
                if hasXpath('//span[@class="fsm fwn fcg"]/a/abbr/span'):
                    date=wd.find_element_by_xpath('//span[@class="fsm fwn fcg"]/a/abbr/span')
                    date_posted=date.text.encode("utf-8")
                    f.write(("Date Posted - ").encode('ascii'))
                    f.write(date_posted)
                    f.write(("\n").encode('ascii'))

                #Taking the No. of likes from the post with the Xpath provided
                if hasXpath('//span[@class="_81hb"]'):
                    likes=wd.find_element_by_xpath('//span[@class="_81hb"]')
                    no_of_likes=likes.text.encode("utf-8")
                    f.write(("Number of Likes - ").encode('ascii'))
                    f.write(no_of_likes)
                    f.write(("\n").encode('ascii'))
                
                else:
                    f.write(("Number of Likes - 0").encode('ascii'))
                    f.write(("\n").encode('ascii'))
                
                #Taking the no. of comments from the post with the Xpath provided
                if hasXpath('//a[@class="_3hg- _42ft"]'):
                    comments=wd.find_element_by_xpath('//a[@class="_3hg- _42ft"]')
                    no_of_comments=comments.text.encode("utf-8")
                    f.write(("Number of Comments - ").encode('ascii'))
                    f.write(no_of_comments)
                    f.write(("\n").encode('ascii'))

                else:
                    f.write(("Number of Comments - 0").encode('ascii'))
                    f.write(("\n").encode('ascii'))

                #Taking the shares from the post with the Xpath provided
                if hasXpath('//a[@class="_3rwx _42ft"]'):
                    shares=wd.find_element_by_xpath('//a[@class="_3rwx _42ft"]')
                    no_of_shares=shares.text.encode("utf-8")
                    f.write(("Number of Shares - ").encode('ascii'))
                    f.write(no_of_shares)
                    f.write(("\n").encode('ascii'))

                else:
                    f.write(("Number of Shares - 0").encode('ascii'))
                    f.write(("\n").encode('ascii'))

                f.write(("\n").encode('ascii'))
                f.write(("Post on Facebook").encode('ascii'))                    
                f.write(("\n\n").encode('ascii'))

                #Taking the content from the post with the Xpath provided
                if hasXpath('//div[@class="_5pbx userContent _3576"]'):
                    final_post=wd.find_element_by_xpath('//div[@class="_5pbx userContent _3576"]')
                    post_text = final_post.text.encode("utf-8")
                    f.write(post_text)
                    f.write(("\n \n").encode('ascii'))
                    f.write("--------------------------------------------------------------------******************------------------------------------------------------------".encode('ascii'))
                    f.write(("\n \n").encode('ascii'))

                elif hasXpath('//div[@class="_5pbx userContent _3ds9 _3576"]'):
                    final_post=wd.find_element_by_xpath('//div[@class="_5pbx userContent _3ds9 _3576"]')
                    post_text = final_post.text.encode("utf-8")
                    f.write(post_text)
                    f.write(("\n \n").encode('ascii'))
                    f.write("--------------------------------------------------------------------******************------------------------------------------------------------".encode('ascii'))
                    f.write(("\n \n").encode('ascii'))


    #Goes to a new link in the browser from where user's post can be extracted
    wd.get('https://www.facebook.com/search/latest/?q=' +keyword[i]+ '&epa=SEARCH_BOX')
    j=0
    #Value of J determines how much time scrolling happens to the bottom of page
    while (j<100):
        # Scroll down to bottom
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
        j=j+1

    if(hasXpath('//div[@class="_6-cp"]')):
            posts=wd.find_elements_by_xpath('//div[@class="_6-cp"]/div/span/a')
            #Takes link of all the posts from the page
            html = [x.get_attribute("href") for x in posts] 
            for p in html:
                #Go to each link individually
                wd.get(p)
                f.write(("Post URL - ").encode('ascii'))
                f.write(p.encode("utf-8"))
                f.write(("\n").encode('ascii'))

                #Taking the user name from the post with the Xpath provided
                if hasXpath('//div[@class="_6a _5u5j _6b"]/h5/span/span/a'):    
                    name=wd.find_element_by_xpath('//div[@class="_6a _5u5j _6b"]/h5/span/span/a')
                    name_user=name.text.encode("utf-8")
                    f.write(("User Name - ").encode('ascii'))
                    f.write(name_user)
                    f.write(("\n").encode('ascii'))
                
                #Taking the date from the post with the Xpath provided
                if hasXpath('//span[@class="fsm fwn fcg"]/a/abbr/span'):
                    date=wd.find_element_by_xpath('//span[@class="fsm fwn fcg"]/a/abbr/span')
                    date_posted=date.text.encode("utf-8")
                    f.write(("Date Posted - ").encode('ascii'))
                    f.write(date_posted)
                    f.write(("\n").encode('ascii'))

                #Taking the Number of likes from the post with the Xpath provided
                if hasXpath('//span[@class="_81hb"]'):
                    likes=wd.find_element_by_xpath('//span[@class="_81hb"]')
                    no_of_likes=likes.text.encode("utf-8")
                    f.write(("Number of Likes - ").encode('ascii'))
                    f.write(no_of_likes)
                    f.write(("\n").encode('ascii'))
                
                else:
                    f.write(("Number of Likes - 0").encode('ascii'))
                    f.write(("\n").encode('ascii'))
                
                #Taking the Number of comments from the post with the Xpath provided
                if hasXpath('//a[@class="_3hg- _42ft"]'):
                    comments=wd.find_element_by_xpath('//a[@class="_3hg- _42ft"]')
                    no_of_comments=comments.text.encode("utf-8")
                    f.write(("Number of Comments - ").encode('ascii'))
                    f.write(no_of_comments)
                    f.write(("\n").encode('ascii'))

                else:
                    f.write(("Number of Comments - 0").encode('ascii'))
                    f.write(("\n").encode('ascii'))

                #Taking the Number of shares from the post with the Xpath provided
                if hasXpath('//a[@class="_3rwx _42ft"]'):
                    shares=wd.find_element_by_xpath('//a[@class="_3rwx _42ft"]')
                    no_of_shares=shares.text.encode("utf-8")
                    f.write(("Number of Shares - ").encode('ascii'))
                    f.write(no_of_shares)
                    f.write(("\n").encode('ascii'))

                else:
                    f.write(("Number of Shares - 0").encode('ascii'))
                    f.write(("\n").encode('ascii'))

                f.write(("\n").encode('ascii'))
                f.write(("Post on Facebook").encode('ascii'))                    
                f.write(("\n\n").encode('ascii'))

                #Taking the Content from the post with the Xpath provided
                if hasXpath('//div[@class="_5pbx userContent _3576"]'):
                    final_post=wd.find_element_by_xpath('//div[@class="_5pbx userContent _3576"]')
                    post_text = final_post.text.encode("utf-8")
                    f.write(post_text)
                    f.write(("\n \n").encode('ascii'))
                    f.write("--------------------------------------------------------------------******************------------------------------------------------------------".encode('ascii'))
                    f.write(("\n \n").encode('ascii'))

                elif hasXpath('//div[@class="_5pbx userContent _3ds9 _3576"]'):
                    final_post=wd.find_element_by_xpath('//div[@class="_5pbx userContent _3ds9 _3576"]')
                    post_text = final_post.text.encode("utf-8")
                    f.write(post_text)
                    f.write(("\n \n").encode('ascii'))
                    f.write("--------------------------------------------------------------------******************------------------------------------------------------------".encode('ascii'))
                    f.write(("\n \n").encode('ascii'))
        
    #Closing the file
    f.close()
    #Colsing the browser
wd.close()

