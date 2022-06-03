from classes.fcs import fcs
import constants as c

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from bs4 import BeautifulSoup
import math as m
import time as t

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

cant_iter = m.ceil(c.cant_iter)
dates = c.dates
cryptos_data = {}
cont = 1

# Open the csv file and write the headers
fcs.start_csv()

for i in range(13,23):

    for j in range(1,13):
        
        # control end of data
        if i == 22 and j > 5:
            break
        try:
            url = ""
            driver.get('chrome://settings/clearBrowserData')

            if j < 10:
                url = 'https://coinmarketcap.com/historical/20%s0%s01/' % (i,j)
                driver.get(url)
            else:
                url = 'https://coinmarketcap.com/historical/20%s%s01/' % (i,j)
                driver.get(url)

            t.sleep(1)

            # Make scroll to the bottom of page or top if get_crypto_list throws error
            fcs.run_scroll(driver)

            soup = BeautifulSoup(driver.page_source, 'html.parser')

            date = url[-9:-1]

            # Get the cryptos info
            cryptos_data = fcs.get_crypto_list(driver, soup, cont, date)

            # Write info in a csv
            fcs.write_csv(cryptos_data)
            
            cryptos_data.clear()
        except:
            continue

driver.close()