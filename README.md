![profilesearchimg](https://github.com/HedvaldoCosta/ProfileSearch/assets/67663958/05d73be6-e245-496e-8180-b75e89cccf64)

# RESUMO
O setor de recursos humanos (RH) está em busca de novas contratações e necessita de uma forma para facilitar a busca de perfis em determinadas áreas e setores.

# INTRODUÇÃO
A aplicação possibilita que o usuário possa encontrar em torno de 30 perfis de acordo com a filtragem de área de conhecimento, localidade e site específico. Assim, acelerando o processo de busca de novos funcionários para a empresa. 

# SOLUÇÃO
Utilizando-se de recursos de web scraping, foi possível usar a biblioteca "Selenium" para a criação de uma variável webdriver que dá acesso para a máquina iniciar um conjunto de comandos dentro do navegador. Aplicando as funções e comandos necessários, a aplicação desenvolvida passou a pesquisar perfis de acordo com os filtros escolhidos pelo usuário.

**Código da solução: < https://bit.ly/3VKFo0j >**

![image](https://github.com/HedvaldoCosta/ProfileSearch/assets/67663958/ef7345c1-4747-400a-b6e1-a7beae226e81)

# FERRAMENTAS
Python 3.9.13

Pycharm 2023.1.1

pandas 2.0.1

selenium 4.9.0

streamlit 1.22.0

webdriver-manager 3.8.6

# SOBRE O CÓDIGO
```python
# Criar um script em Python que abre um navegador e simula interações com o navegador
from selenium import webdriver
# Automatizar o processo de download e instalação do driver do Chrome
from webdriver_manager.chrome import ChromeDriverManager
# Controlar o serviço do ChromeDriver
from selenium.webdriver.chrome.service import Service
# Conjunto de estratégias de localização de elementos em uma página da web
from selenium.webdriver.common.by import By
# Simular pressionamentos de teclas do teclado
from selenium.webdriver.common.keys import Keys
# Utilizado para criar o dataframe
import pandas as pd
# Contrução da aplicação web
import streamlit as st
```

````python
# Lista de sites para a filtragem
options_site = ['github.com', 'linkedin.com/in', 'facebook.com', 'instagram.com']
site = st.sidebar.selectbox('Site', options=options_site)
# Inserir a área de conhecimento desejada 
area = st.sidebar.text_input('Área de conhecimento')
# Inserir o local desejado
locality = st.sidebar.text_input('Localidade desejada')
````

````python
# A demonstração do dataframe só vai se dar após o usuário ter inserido o local e a área
if (area != '') & (locality != ''):
    lista_perfil = []
    # Configurar as opções do navegador Google Chrome no contexto do Selenium WebDriver
    # em Python. Nesse caso, foi utilizado para configurações de execução sem janela
    options = webdriver.ChromeOptions()
    # Função utilizada para que não abrisse um novo navegador no dispositivo
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
            # Buscando informações de acordo com o XPATH e acrescentando os links na lista
            # "lista_perfil"
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
    # Demonstrando o número total de perfis encontrados
    st.sidebar.info(f'Total de {len(dataframe_perfil)} perfis encontrados')
    st.dataframe(dataframe_perfil)
````
# SUMMARY
The human resources (HR) sector is looking for new hires and needs a way to facilitate the search for profiles in certain areas and sectors.

# INTRODUCTION
The application allows the user to find around 30 profiles according to the filtering of knowledge area, location and specific site. Thus, accelerating the process of searching for new employees for the company.

# SOLUTION
Using web scraping resources, it was possible to use the "Selenium" library to create a webdriver variable that gives access to the machine to start a set of commands within the browser. Applying the necessary functions and commands, the developed application began to search for profiles according to the filters chosen by the user.

**solution code: < https://bit.ly/3VKFo0j >**

![image](https://github.com/HedvaldoCosta/ProfileSearch/assets/67663958/ef7345c1-4747-400a-b6e1-a7beae226e81)

# TOOLS
Python 3.9.13

Pycharm 2023.1.1

pandas 2.0.1

selenium 4.9.0

streamlit 1.22.0

webdriver-manager 3.8.6

# ABOUT THE CODE
```python
# Create a Python script that opens a browser and simulates browser interactions
from selenium import webdriver
# Automate the Chrome driver download and installation process
from webdriver_manager.chrome import ChromeDriverManager
# Control the ChromeDriver Service
from selenium.webdriver.chrome.service import Service
# Set of strategies for locating elements on a web page
from selenium.webdriver.common.by import By
# Simulate keyboard keystrokes
from selenium.webdriver.common.keys import Keys
# Used to create the dataframe
import pandas as pd
# Construction of the web application
import streamlit as st
```

````python
# List of sites for filtering
options_site = ['github.com', 'linkedin.com/in', 'facebook.com', 'instagram.com']
site = st.sidebar.selectbox('Site', options=options_site)
# Insert the desired area of knowledge
area = st.sidebar.text_input('Área de conhecimento')
# Insert the desired location
locality = st.sidebar.text_input('Localidade desejada')
````

````python
# The dataframe demonstration will only take place after the user has entered the 
# location and area
if (area != '') & (locality != ''):
    lista_perfil = []
    # Configure Google Chrome browser options in the context of Selenium WebDriver in Python.
    # In this case it was used for windowless run configurations
    options = webdriver.ChromeOptions()
    # Function used to not open a new browser on the device
    options.add_argument("--headless")
    # Chromedriver starting and stopping
    service = Service(ChromeDriverManager().install())
    navigator = webdriver.Chrome(service=service, options=options)
    # entering the link: <https://google.com.br>
    navigator.get("https://google.com.br")
    # Searching the site, area and locality through browser search filters
    search = navigator.find_element(by=By.NAME, value='q')
    search.send_keys(f'site:{site} AND "{area}" AND "{locality}"')
    search.send_keys(Keys.ENTER)
    # Checking 3 search pages
    for c in range(1, 4):
        try:
            # Searching for information according to XPATH and adding links to the list
            # "lista_perfil"
            perfis = navigator.find_elements(by=By.XPATH, value='//div[@class="yuRUbf"]/a')
            for perfil in perfis:
                if site in perfil.get_attribute('href'):
                    lista_perfil.append(perfil.get_attribute('href'))
            navigator.find_element(by=By.XPATH, value='//*[@id="pnnext"]/span[2]').click()
        except:
            break
    # Adding the profiles link in a dataframe
    dataframe_perfil = pd.DataFrame(lista_perfil)
    dataframe_perfil.rename(columns={0: 'Perfis'}, inplace=True)
    navigator.quit()

    st.title('Lista de perfis encontrados')
    # Showing the total number of profiles found
    st.sidebar.info(f'Total de {len(dataframe_perfil)} perfis encontrados')
    st.dataframe(dataframe_perfil)
````
