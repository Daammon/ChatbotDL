# import urllib.request
# import re
# import requests
import time
# import pandas as pd
# import numpy as np

import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')

#Web scraping
# from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=chrome_options)

def get_url_search(nombre):
  url_base="https://www.imdb.com/find?s=nm&q="
  url_medio=nombre.lower().replace(' ', '+')
  url_fin="&ref_=nv_sr_sm"
  url= url_base + url_medio + url_fin
  return url

def get_url_movie(peli_separado):
    url_base="https://www.imdb.com/find?q="
    url_medio=peli_separado
    url_fin="&s=tt&ttype=ft&exact=true&ref_=fn_tt_ex"
    url= url_base + url_medio + url_fin
    return url

def Find_all_movies_of_actor(actor):
    # URL Actor A
    try:
        browser.get(get_url_search(actor))
    except:
        print("An error occured.")
    time.sleep(10)

    browser.find_element_by_link_text(actor).click()

    print(" URL deL actor A : " + browser.current_url)

    # Lista pelis actor A
    # En el bucle known_for guardamos las peliculas, siempre hay 4.
    # el bucle tiene formato raro

    movie_list = []
    elements = browser.find_element_by_class_name("filmo-category-section")

    movies = elements.find_elements_by_tag_name("b")
    # print(movies)
    # print(len(movies))
    for i in range(len(movies)):
        # print(movies[i].text)
        movie_list.append(movies[i].text)

    print(movie_list)

    return (movie_list)

def Find_best_movies_actor(actor):

  # pretransformacion del input- cambiarlo a lowercase, separarlo con +

  nombre_separado=actor.lower().replace(' ', '+')

  #nos metemos en la url

  try:
    browser.get(get_url_search(nombre_separado))
  except:
    print("An error occured.")
  time.sleep(10)

  print(" URL de la búsqueda : " + browser.current_url )

  #Con selenium, accedemos a la pagina del actor clickando en el resultado de la busqueda

  browser.find_element_by_link_text(actor).click()

  print(" URL del actor : " + browser.current_url)


  #En el bucle known_for guardamos las peliculas, siempre hay 4.
  #el bucle tiene formato raro

  best_movies=[]

  for i in range(4):
    xpath = "//*[@id=\"knownfor\"]/div[" + str(i+1) + "]/div[2]/a"
    #print(xpath)
    elements=browser.find_element_by_xpath(xpath)
    #print(elements.text)
    best_movies.append(elements.text)

  for i in best_movies:
    print(i)

  return (best_movies)

def Find_year_from_movie(movie):

  # pretransformacion del input- cambiarlo a lowercase, separarlo con +

  peli_separado=movie.lower().replace(' ', '%20')

  #busqueda de la pelicula (tipo pelicula y exact match)

  try:
    browser.get(get_url_movie(peli_separado))
  except:
    print("An error occured.")
  time.sleep(10)

  print(" URL de la búsqueda : " + browser.current_url )

  #clickamos el primer resultado

  browser.find_element_by_link_text(movie).click()

  #metodo alternativo: xpath
  #xpath="/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[2]/table/tbody/tr/td[2]/text()"
  #elements=browser.find_element_by_xpath(xpath)

  #cogemos el año

  print(" URL de la peli : " + browser.current_url )


  year=browser.find_element_by_id("titleYear").text
  print (year)


  return(year)

def common(a,b):
    c = [value for value in a if value in b]
    return c


def Find_common_movie_of_actors(actor_a, actor_b):
    # URL Actor A
    try:
        browser.get(get_url_search(actor_a))
    except:
        print("An error occured.")
    time.sleep(10)

    browser.find_element_by_link_text(actor_a).click()

    print(" URL deL actor A : " + browser.current_url)

    # Lista pelis actor A
    # En el bucle known_for guardamos las peliculas, siempre hay 4.
    # el bucle tiene formato raro

    movie_list_a = []
    elements = browser.find_element_by_class_name("filmo-category-section")

    movies = elements.find_elements_by_tag_name("b")
    # print(movies)
    # print(len(movies))
    for i in range(len(movies)):
        # print(movies[i].text)
        movie_list_a.append(movies[i].text)

    # for i in movie_list_a:
    # print(i)

    # URL Actor B
    try:
        browser.get(get_url_search(actor_b))
    except:
        print("An error occured.")
    time.sleep(10)

    browser.find_element_by_link_text(actor_b).click()

    print(" URL del actor B : " + browser.current_url)

    # Lista pelis actor B
    # En el bucle known_for guardamos las peliculas, siempre hay 4.
    # el bucle tiene formato raro

    movie_list_b = []
    elements = browser.find_element_by_class_name("filmo-category-section")

    movies = elements.find_elements_by_tag_name("b")
    # print(movies)
    # print(len(movies))
    for i in range(len(movies)):
        # print(movies[i].text)
        movie_list_b.append(movies[i].text)

    # for i in movie_list_b:
    # print(i)

    ### contrastar listas a y b
    common_movie = common(movie_list_a, movie_list_b)
    print(common_movie)
    return (common_movie)

def get_url_search_genre(category):
  url_base="https://www.imdb.com/search/title/?genres="
  url_medio=category.lower()
  url_fin="&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=66F966JHMXHEEF7A5JKZ&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1"
  url= url_base + url_medio + url_fin
  return url

def Find_best_movie_by_genre(genre):

  try:
    browser.get(get_url_search_genre(genre))
  except:
    print("An error occured.")
  time.sleep(10)

  print(" URL de mejores pelis de la categoría: " + browser.current_url )

  xpath = "//*[@id=\"main\"]/div/div[3]/div/div[1]/div[3]/h3/a"

  best_movie_genre=browser.find_element_by_xpath(xpath).text
  print(best_movie_genre)
  return(best_movie_genre)

