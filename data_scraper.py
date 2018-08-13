# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re


def scrape(x):
    print("SCRAPING")
    options = Options()
    options.add_argument("--headless")
    # Got to supply path for gecko driver for firefox headless browser.
    driver = webdriver.Firefox(firefox_options=options, executable_path="geckodriver.exe")
    
    # Getting conversations page by page and adding the conversational data to the list.
    list = []
    def convo_grabber(idNum):
        URL = 'http://notsocleverbot.jimrule.com/index.php?page='+str(idNum)
        try:
            driver.get(URL)
            print(str(idNum)+"/"+str(x))
            convos = driver.find_element_by_xpath("//*[@id=\"posts\"]").text
            convoses = convos.split("Comment")
            for i in convoses:
                list.append(i)
        except:
            print("Connection Error")
            
    # Scraping the given number of pages, converting the data and saving it to a file. 
    def gather_data(x):    
        print("This is going to take some time...")
        for num in range(1,x+1):
            convo_grabber(num)
            
        driver.close()
    
        clear_convs = []
        for item in list:
            clear_convs.append(re.sub(r'^Posted.*\n?', '', item, flags=re.MULTILINE))
    
        qa_list = []
        for cnv in clear_convs:
            conv = cnv.split("\n")
            if len(conv) > 1:
                if len(conv[0]) < 1:
                    qa_list.append(conv[1:-1])
                else:
                    qa_list.append(conv[:-1])
    
        cleared_qa = []
        for line in qa_list:
            cleared_line = []
            for text in line:
                try:
                    cleared_line.append(text.split(":")[1].lstrip())
                except:
                    pass
            cleared_qa.append(cleared_line)
    
    
        qa_final = []
        for text in cleared_qa:  
            for x in range(0,len(text)-1):
                l = []
                l.append(text[x])
                l.append(text[x+1])
                qa_final.append(l)
        with open('firstCheck.txt', 'w') as data:
            for line in qa_final:
                for text in line:
                    data.write(str(text.encode("utf-8"))+"|")
                data.write("\n")
            
        print("Saving is done.")
    
    gather_data(x)        