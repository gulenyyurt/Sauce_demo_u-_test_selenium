from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driveri bekleten yapı
from selenium.webdriver.support import expected_conditions as ec # beklenen koşullar 
from selenium.webdriver.common.action_chains import ActionChains # bir dizi zincir misali aksşyonlar
import pytest

class Test_productpeice:
    def setup_method(self): #pytest tarafından tanımlanan bir metod her test öncesi otomaik olarak çalıştırılır.
        self.driver =webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/inventory.html")
        userNameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
       
        actions= ActionChains(self.driver)
        actions.send_keys_to_element(userNameInput,"standard_user")
        actions.send_keys_to_element(passwordInput,"secret_sauce")
        actions.perform()
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"login-button")))
        loginButton.click()

    def teardown_method(self): #her test bitiminde çalışacak fonksiyon
        self.driver.quit()
        
    def test_product_count(self):
        productList = WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
        assert len(productList) == 6
        
    def test_basket(self):
        addToCard=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")))
        
        self.driver.execute_script("window.scrollTo(0,500)") #asagıdaki action ın yaptıgı işi yapıyor bu javascript codu
        addToCard.click()  # action aktif olursa bu ve üstündeki satır silinir.
        # actions2=ActionChains(driver)
        # actions2.move_to_element(addToCard) #butonun olduğu yere sayfayı tası
        # actions2.click()
        # actions2.perform()  
        sleep(3)
        removeButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[6]/div[2]/div[2]/button")))
        assert removeButton.text == "Remove"
        
        addToCard=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH," //*[@id='add-to-cart-sauce-labs-backpack']")))
        
        self.driver.execute_script("window.scrollTo(0,500)") #asagıdaki action ın yaptıgı işi yapıyor bu javascript codu
        addToCard.click()  # action aktif olursa bu ve üstündeki satır silinir. 
        sleep(3)
        removeButton=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='remove-sauce-labs-backpack']")))
        assert removeButton.text == "Remove"
        sleep(3)

        basket=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='shopping_cart_container']/a")))
        basket.click()
        sleep(3)
        product=WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='item_4_title_link']/div")))
        assert product.text== "Sauce Labs Backpack"
        sleep(3)