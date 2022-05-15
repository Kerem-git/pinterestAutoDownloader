from cgi import print_arguments
from time import sleep
from selenium import webdriver


driver = webdriver.Chrome("C:/SRC/chromeDriver/chromedriver.exe")


url = "https://tr.pinterest.com/search/pins/?q=dua%20lipa&rs=typed&term_meta[]=dua%7Ctyped&term_meta[]=lipa%7Ctyped"

driver.get(url)



for i in range(500):
    driver.execute_script("window.scrollTo(0,999999)")
    sleep(3)

    ab = driver.find_elements_by_xpath("//*[@href]")

    links = []
    pins = []
    imgs = []
    for a in ab:
        l = a.get_attribute("href")
        links.append(l)


    for link in links:
        splitted = link.split("/")
        if splitted[3] == "pin":
            with open("pins.txt","a") as s:
                s.write(link+"\n")
            print(link)
        else:
            pass


driver.quit()