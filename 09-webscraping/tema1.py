from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import re

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
# table = browser.find_element_by_xpath('by=By.XPATH, value=xpath')
table = browser.find_element(by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]/tbody')
header = browser.find_element(by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]/tbody/tr[1]')
table_text = table.text
lista = table_text.split('\n')
lista = lista[1:-2]
lista1 = []
print(lista)

for k in lista:
    j = k.split(' ')
    for x in j:
        lista1.append(x)
lista1.remove("Mare")
lista1.remove("Mun.")


header_text = re.findall('[A-Z][^A-Z]*', header.text)
dictionar = {i : [] for i in header_text}
for j in range(0, len(header_text)):
    for i in range(int(j), len(lista1), len(header_text)):
        # print(lista[i])
        dictionar[header_text[int(j)]].append(lista1[i])
# print(dictionar)

df = pd.DataFrame(dictionar)

print(df.loc['Județ'])



