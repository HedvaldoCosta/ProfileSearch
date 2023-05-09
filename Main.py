# Bibliotecas necessárias para a execução da aplicação
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import streamlit as st

# Filtragem de sites para a busca de perfil
options_site = ['github.com', 'linkedin.com/in', 'facebook.com', 'instagram.com']
site = st.sidebar.selectbox('Site', options=options_site)
# Inserir a área de conhecimento e o local que deseja do perfil
area = st.sidebar.text_input('Área de conhecimento')
locality = st.sidebar.text_input('Localidade desejada')

# Execução do selenium para a coleta dos links sem a necessidade de abrir um novo navegador
if (area != '') & (locality != ''):
    lista_perfil = []
    # Configurar as opções do navegador Google Chrome no contexto do Selenium WebDriver em Python
    # nesse caso, foi utilizado para configurações de execução sem janela
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    # Iniciação e parada do chromedriver
    service = Service(ChromeDriverManager().install())
    navigator = webdriver.Chrome(service=service, options=options)
    # entrando no link: <https://google.com.br>
    navigator.get("https://google.com.br")
    # Pesquisando o site, área e localidade por meio de filtros de pesquisa do navegador
    search = navigator.find_element(by=By.NAME, value='q')
    search.send_keys(f'site:{site} AND "{area}" AND "{locality}"')
    search.send_keys(Keys.ENTER)
    # Verificando 3 páginas de pesquisa
    for c in range(1, 4):
        try:
            perfis = navigator.find_elements(by=By.XPATH, value='//div[@class="yuRUbf"]/a')
            for perfil in perfis:
                if site in perfil.get_attribute('href'):
                    lista_perfil.append(perfil.get_attribute('href'))
            navigator.find_element(by=By.XPATH, value='//*[@id="pnnext"]/span[2]').click()
        except:
            break
    # Acrescentando o link dos perfis em um dataframe
    dataframe_perfil = pd.DataFrame(lista_perfil)
    dataframe_perfil.rename(columns={0: 'Perfis'}, inplace=True)
    navigator.quit()

    st.title('Lista de perfis encontrados')
    st.sidebar.info(f'Total de {len(dataframe_perfil)} perfis encontrados')
    st.dataframe(dataframe_perfil)
