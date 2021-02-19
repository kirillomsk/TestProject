from selenium import webdriver
from conftest import chromedriver


class Test:
    def setup_method(self):
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.get('https://checkme.kavichki.com/')

    def teardown_method(self):
        self.driver.close()

    # тест того, что всё добавляется в правильном порядке
    def test_add_to_table(self):
        self.driver.find_element_by_id('open').click()
        self.driver.find_element_by_id('name').send_keys('name')
        self.driver.find_element_by_id('count').send_keys('count')
        self.driver.find_element_by_id('price').send_keys('price')
        self.driver.find_element_by_id('add').click()
        assert self.driver.find_element_by_css_selector('tr:nth-child(5) > td:nth-child(1)').text == 'name'
        assert self.driver.find_element_by_css_selector('tr:nth-child(5) > td:nth-child(2)').text == 'count'
        assert self.driver.find_element_by_css_selector('tr:nth-child(5) > td:nth-child(3)').text == 'price'

    # тест кнопки "Сбросить"
    def test_drop(self):
        before = len(self.driver.find_elements_by_tag_name('tr'))
        self.driver.find_element_by_css_selector('a:nth-child(4)').click()
        after = len(self.driver.find_elements_by_tag_name('tr'))
        assert before != after

    # тест кнопки "Удалить"
    def test_delete(self):
        assert len(self.driver.find_elements_by_class_name('delete')) == 4
        for i in range(4):
            self.driver.find_element_by_class_name('delete').click()
        assert len(self.driver.find_elements_by_class_name('delete')) == 0

    # тест удаления созданного пункта списка
    def test_new_delete(self):
        self.driver.find_element_by_id('open').click()
        self.driver.find_element_by_id('name').send_keys('name')
        self.driver.find_element_by_id('count').send_keys('count')
        self.driver.find_element_by_id('price').send_keys('price')
        self.driver.find_element_by_id('add').click()
        self.driver.find_element_by_css_selector('tr:nth-child(5) > td:nth-child(4) > a').click()
        assert len(self.driver.find_elements_by_class_name('delete')) == 4
