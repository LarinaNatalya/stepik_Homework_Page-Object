from .base_page import BasePage

class MainPage(BasePage):#MainPage. Его нужно сделать наследником класса BasePage- доступ ко всем атрибутам и методам своего класса-предка
    def go_to_login_page(self): #self , чтобы иметь доступ к атрибутам и методам класса
    login_link=self.browser.find_element(By.CSS_SELECTOR, "#login_link") #обращаться к аргументу BasePage как self
    login_link.click()