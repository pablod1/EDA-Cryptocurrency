import constants as c
import time as t
import math as m
import csv
from selenium.webdriver.common.by import By

class fcs:

    # Function to scroll down and click Load more btn
    def run_scroll(d):

        cant_iter = m.ceil(c.cant_iter)-1
        d.execute_script("window.scrollTo(0, 220)")
        
        for x in range(cant_iter):
            
            speed = 100
            while speed < 2000:
                d.execute_script("window.scrollBy(0, "+str(speed)+")")
                speed += 100 
                t.sleep(0.2)

            if x != cant_iter-1:
                
                if d.find_elements(By.XPATH, "//*[contains(text(), 'Load More')]"):
                    try:
                        #btn_more = WebDriverWait(d, 10).until(EC.presence_of_element_located(By.XPATH, "//*[contains(text(), 'Load More')]"))
                        btn_more = d.find_element(By.XPATH, "//*[contains(text(), 'Load More')]")
                        btn_more.click()
                    except:
                        break
                else: 
                    break
            else:
                break

    # Once everythins is loaded we get the full data
    def get_crypto_list(driver, soup, cont, i):
        print(i)
        items = soup.find_all('tr', {'class', 'cmc-table-row'})

        year, month, day = i[:4],i[4:6],i[6:8]

        date = year+'-'+month+'-'+day

        cryptos_data = {}
        
        try:
            for item in items:
                name = item.find(class_='cmc-table__column-name--name cmc-link').text
                symbol = item.find(class_='cmc-table__cell--sort-by__symbol').text
                rank = item.find(class_='cmc-table__cell--sort-by__rank').text
                price = item.find(class_='cmc-table__cell--sort-by__price').text
                mcap = item.find(class_='cmc-table__cell--sort-by__market-cap').contents[0].text
                circulating_supply = item.find(class_='cmc-table__cell--sort-by__circulating-supply').text

                cryptos_data['crypto_%s' % (cont)] = {
                        'name':name,
                        'symbol':symbol,
                        'rank':rank,
                        'price':price,
                        'mcap':mcap,
                        'circulating_supply':circulating_supply,
                        'date':date
                    }
                
                cont += 1
        except AttributeError:
            print("He entrado al except de get_crypto()")
            fcs.run_scroll(driver)

        return cryptos_data

    # We open the csv to write the header
    def start_csv():
        f = open('../../../../csv_file.csv_test', 'w', newline='')
        header = ['name','symbol','rank','price','mcap','circulating_supply','date']
        writer = csv.writer(f)
        writer.writerow(header)
        f.close()

    # Open again to write the collected data
    def write_csv(cryptos_data):
        with open('../../../../csv_file.csv_test','a', newline='', encoding='UTF-8') as f:
            writer = csv.writer(f)

            for i in cryptos_data.keys():
                lista_aux = []
                for j in cryptos_data[i].keys():
                    lista_aux.append(cryptos_data[i].get(j))

                writer.writerow(lista_aux)
