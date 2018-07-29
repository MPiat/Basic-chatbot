from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re
import pandas as pd


options = Options()
options.add_argument("--headless")
# Got to supply path for gecko driver for firefox headless browser
driver = webdriver.Firefox(firefox_options=options, executable_path="geckodriver.exe")

# Getting conversations page by page
list = []
def convo_grabber(idNum):
    URL = 'http://notsocleverbot.jimrule.com/index.php?page='+str(idNum)
    driver.get(URL)
    convos = driver.find_element_by_xpath("//*[@id=\"posts\"]").text
    convoses = convos.split("Comment")
    for i in convoses:
        list.append(i)

def gather_data(x):    
    #start = time.time()
    for num in range(1,x):
        convo_grabber(num)
    #end = time.time()
    #print(end - start)
    driver.close()

    clear_convs = []
    for item in list:
        clear_convs.append(re.sub(r'^Posted.*\n?', '', item, flags=re.MULTILINE))
    ## RERTURNS LIST OF CONVERSATIONS -- DONE

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
                cleared_line.append(text.split(":")[1].lstrip()) # list index out of range
            except:
                #print("###ERROR###")
                #print(text)
                pass
        cleared_qa.append(cleared_line)


    qa_final = []
    for text in cleared_qa:  
        for x in range(0,len(text)-1):
            l = []
            l.append(text[x])
            l.append(text[x+1])
            qa_final.append(l)

    convo_frame = pd.Series(dict(qa_final)).to_frame().reset_index()
    convo_frame.columns = ['q','a']
    return convo_frame