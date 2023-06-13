from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

def main():

    url = 'https://zooshoptest.ru/'
    
    # Создание объекта driver, передаем объекту ссылку страницы

    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)
    except Exception as e:
        print(e, '\n', 'input link not found')
        driver.close()
        sys.exit(-1)

    # ожидаем, пока кнопка "Обратная связь" будет прогружена на странице.
    # после обращаемся к нему и нажимаем
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((
        By.XPATH, "//div[contains(@class,'animation')]"))).click()
    
    # после нажатия на кнопку "Обратная связь" ожидаем, что форма будет
    # прогружена, далее обращаемся к элементу ввода имени
    input_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((
            By.XPATH, "//input[contains(@autocomplete,'given-name')]"
    )))
    
    # кликаем на элемент ввода, очищаем ранее введенные данные, вставляем 
    # тестовые данные
    input_name.click()
    input_name.clear()
    input_name.send_keys('name')
    
    # находим элемент ввода для фамилии, кликаем, 
    # очищаем и вставляем как было ранее  
    input_lastname = driver.find_element(
        By.XPATH, "//input[contains(@autocomplete,'family-name')]")
    input_lastname.click()
    input_lastname.clear()
    input_lastname.send_keys('lastname')

    # обращаемся к элементу ввода для телефона, кликаем, 
    # очищаем и вставляем как было ранее
    input_phone = driver.find_element(
        By.XPATH, "//input[contains(@name,'phone')]")
    input_phone.click()
    input_phone.send_keys('+79912345678')

    # находим элемент ввода для эл. почты, кликаем, 
    # очищаем и вставляем как было ранее
    input_email = driver.find_element(
        By.XPATH, "//input[contains(@name,'email')]")
    input_email.click()
    input_email.send_keys('abc@mail.com')

    # находим элемент ввода для комментария, кликаем, 
    # очищаем и вставляем как было ранее
    input_text = driver.find_element(
        By.XPATH, "//textarea[contains(@class, 'b24-form-control')]")
    input_text.click()
    input_text.send_keys('aboba')

    # обращаемся к кнопке "Отправить" для дальнейшей 
    # отправки введенных ранее данных  
    submit = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Отправить')]")
    submit.click()

    # ожидаем, пока форма будет направлена 
    # для последующей проверки успешности тест кейса  
    success = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((
            By.XPATH, "//p[contains(text(), 'Спасибо, ваше сообщение отправлено.')]"
    )))

    # проверяем на успешность обработки тест кейса
    # в случае успеха - ничего не произойдет
    # в случае провала - на консоли выведется ошибка AssertionError
    # и обращение на ошибочную строку
    assert success.text == 'Спасибо, ваше сообщение отправлено.'
    assert str.__contains__(success.text, 'Спасибо, ваше сообщение отправлено.')

    driver.close()

if __name__ == "__main__":
    main()