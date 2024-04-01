from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json

with open("data\\employees.json", "r") as file:
    data = json.load(file)

employees = data["employees"]

for employee in employees:
    print("First Name:", employee["firstName"])
    print("Last Name:", employee["lastName"])
    print("Age:", employee["age"])
    print("Position:", employee["position"])
    print()