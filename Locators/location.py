from selenium import webdriver
from selenium.webdriver.edge.service import Service


class location:
    myAccount = '//*[@id="top-links"]/ul/li[2]/a'
    login = '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a'
    email = '//*[@id="input-email"]'
    password = '//*[@id="input-password"]'
    loginbutton = '//*[@id="content"]/div/div[2]/div/form/input'


class base:
    edge_path = "E:\\WebDriver\\msedgedriver.exe"
    service = Service(executable_path=edge_path)
    driver = webdriver.Edge(service=service)
    url = "http://testbasc.great-site.net/"