#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Fri Mar 15 22:15:49 2019

@author: teodoratanasov
"""

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def imprimir(c):
    i = 0
    for v in c:
        print(str(i)+"__")
        i+=1
        for co in v:
            print('*' + co + '*')


def buscarComentarios(links):
    todosComentarios = []
    #option = webdriver.firefox()
    option = webdriver.ChromeOptions()
    option.add_argument("—incognito")
    option.add_argument("--window-size=700x900")
    browser = webdriver.Chrome(executable_path='/Users/teodoratanasov/Downloads/chromedriver',
                               chrome_options=option)
    for link in links:
        browser.get(link)
        comentarioProducto = []
        for i in range(1, 12):
            path = '//*[@id="BVRRContainer"]/div/div/div/div/ol/li[' + str(
                i) + ']/div/div[1]/div/div[2]/div/div/div[1]/p'
            titles_element = browser.find_elements_by_xpath(path)
            # use list comprehension to get the actual repo titles and not the selenium objects.
            #print(len(titles_element))
            if len(titles_element) != 0:
                comentarioProducto.append(titles_element[0].text)
        if comentarioProducto != None:
            todosComentarios.append(comentarioProducto)
    browser.quit()
    return todosComentarios


url = "https://www.elcorteingles.es/search/?itemsPerPage=36&s="
print("Introduce un producto a buscar: ")
producto = input()
producto = producto.replace(' ', "%20")
# print(producto)
url += producto + "&sorting=ratingDesc"
print("Conectando a: " + url)
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
aux = soup.find_all('h3', class_='info-name')
aux = str(aux)
soup2 = BeautifulSoup(aux, 'html.parser')
links = []
for tag in soup2.findAll('a', href=True):
    links.append("https://www.elcorteingles.es" + tag['href'])
comentariosFin = buscarComentarios(links)
imprimir(comentariosFin)