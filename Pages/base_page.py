class BasePage():#класс внутри которого методы
    def __init__(self, browser, url):#конструктор
        self.browser = browser
        self.url = url
    def open(self):#метод
        self.browser.get(self.url)