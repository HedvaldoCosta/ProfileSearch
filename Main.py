from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import streamlit as st


options_site = ['github.com', 'linkedin.com/in', 'facebook.com', 'instagram.com']
site = st.sidebar.selectbox('Site', options=options_site)
area = st.sidebar.text_input('Área de conhecimento')
locality = st.sidebar.text_input('Localidade desejada')

if (area != '') & (locality != ''):
    lista_perfil = []
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    navigator = webdriver.Chrome(service=service, options=options)

    navigator.get("https://google.com.br")
    search = navigator.find_element(by=By.NAME, value='q')
    search.send_keys(f'site:{site} AND "{area}" AND "{locality}"')
    search.send_keys(Keys.ENTER)

    for c in range(1, 4):
        try:
            perfis = navigator.find_elements(by=By.XPATH, value='//div[@class="yuRUbf"]/a')
            for perfil in perfis:
                if site in perfil.get_attribute('href'):
                    lista_perfil.append(perfil.get_attribute('href'))
            navigator.find_element(by=By.XPATH, value='//*[@id="pnnext"]/span[2]').click()
        except:
            break

    dataframe_perfil = pd.DataFrame(lista_perfil)
    dataframe_perfil.rename(columns={0: 'Perfis'}, inplace=True)
    navigator.quit()

    st.title('Lista de perfis encontrados')
    st.sidebar.info(f'Total de {len(dataframe_perfil)} perfis encontrados')
    st.dataframe(dataframe_perfil)
