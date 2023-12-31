import data
import sender_stand_request

def get_kit_body(name):
    # копирование словаря с телом запроса из файла data
    current_body = data.kit_body.copy()
    # изменение значения в поле name
    current_body["name"] = name
    # возвращается новый словарь с нужным значением name
    return current_body

def get_new_user_token():
    return sender_stand_request.post_new_user(data.user_body).json()['authToken']

def get_headers_for_post_new_kit():
    kit_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {get_new_user_token()}"
    }
    return kit_headers

def post_new_kit_for_auth_user(body):
    headers = get_headers_for_post_new_kit()
    return sender_stand_request.post_new_kit(body, headers)
def test_create_kit_1_letter_in_name_get_success_response():
    # В переменную user_body сохраняется обновленное тело запроса с именем “а”
    user_body = get_kit_body("а")
    # В переменную user_response сохраняется результат запроса на создание нового набора
    user_response = post_new_kit_for_auth_user(user_body)
    # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201, "Status code is not 201"
    # Проверяется, что в ответе есть поле name, и оно равно полю name в запросе
    assert user_response.json()["name"] == user_body["name"]

def test_create_kit_511_letter_in_name_get_success_response():
    test_string = 'abcd' * 127 + 'abc'
    # В переменную user_body сохраняется обновленное тело запроса
    user_body = get_kit_body(test_string)
    # В переменную user_response сохраняется результат запроса на создание нового набора
    user_response = post_new_kit_for_auth_user(user_body)
    # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201, "Status code is not 201"
    # Проверяется, что в ответе есть поле name, и оно равно полю name в запросе
    assert user_response.json()["name"] == user_body["name"]

def test_create_kit_0_letter_in_name_get_negative_response():
    # В переменную user_body сохраняется обновленное тело запроса с именем “”
    user_body = get_kit_body("")
    # В переменную user_response сохраняется результат запроса на создание нового набора
    user_response = post_new_kit_for_auth_user(user_body)
    # Проверяется, что код ответа равен 400
    assert user_response.status_code == 400, "Status code is not 400"

def test_create_kit_512_letter_in_name_get_negative_response():
    test_string = 'abcd' * 128
    # В переменную user_body сохраняется обновленное тело запроса
    user_body = get_kit_body(test_string)
    # В переменную user_response сохраняется результат запроса на создание нового набора
    user_response = post_new_kit_for_auth_user(user_body)
    # Проверяется, что код ответа равен 400
    assert user_response.status_code == 400, "Status code is not 400"

def test_create_kit_english_letters_in_name_get_success_response():
    # В переменную user_body сохраняется обновленное тело запроса
    user_body = get_kit_body("QWErty")
    # В переменную user_response сохраняется результат запроса на создание нового набора
    user_response = post_new_kit_for_auth_user(user_body)
    # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201, "Status code is not 201"
    # Проверяется, что в ответе есть поле name, и оно равно полю name в запросе
    assert user_response.json()["name"] == user_body["name"]

def test_create_kit_russian_letters_in_name_get_success_response():
    # В переменную user_body сохраняется обновленное тело запроса
    user_body = get_kit_body("Мария")
    # В переменную user_response сохраняется результат запроса на создание нового набора
    user_response = post_new_kit_for_auth_user(user_body)
    # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201, "Status code is not 201"
    # Проверяется, что в ответе есть поле name, и оно равно полю name в запросе
    assert user_response.json()["name"] == user_body["name"]

def test_create_kit_special_characters_in_name_get_success_response():
    # В переменную user_body сохраняется обновленное тело запроса
    user_body = get_kit_body('"№%@",')
    # В переменную user_response сохраняется результат запроса на создание нового набора
    user_response = post_new_kit_for_auth_user(user_body)
    assert user_response.status_code == 201, "Status code is not 201"
    # Проверяется, что в ответе есть поле name, и оно равно полю name в запросе
    assert user_response.json()["name"] == user_body["name"]

def test_create_kit_whitespaces_in_name_get_success_response():
    # В переменную user_body сохраняется обновленное тело запроса
    user_body = get_kit_body(" Человек и КО ")
    # В переменную user_response сохраняется результат запроса на создание нового набора
    user_response = post_new_kit_for_auth_user(user_body)
    # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201, "Status code is not 201"
    # Проверяется, что в ответе есть поле name, и оно равно полю name в запросе
    assert user_response.json()["name"] == user_body["name"]

def test_create_kit_numbers_in_name_get_success_response():
    # В переменную user_body сохраняется обновленное тело запроса
    user_body = get_kit_body("123")
    # В переменную user_response сохраняется результат запроса на создание нового набора
    user_response = post_new_kit_for_auth_user(user_body)
    # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201, "Status code is not 201"
    # Проверяется, что в ответе есть поле name, и оно равно полю name в запросе
    assert user_response.json()["name"] == user_body["name"]

def test_create_kit_without_parametr_get_negative_response():
    # В переменную user_body сохраняется пустой dict
    user_body = {}
    # В переменную user_response сохраняется результат запроса на создание нового набора
    user_response = post_new_kit_for_auth_user(user_body)
    # Проверяется, что код ответа равен 400
    assert user_response.status_code == 400, "Status code is not 400"

def test_create_kit_other_type_of_parametr_in_name_get_negative_response():
    # В переменную user_body сохраняется обновленное тело запроса
    user_body = get_kit_body(123)
    # В переменную user_response сохраняется результат запроса на создание нового набора
    user_response = post_new_kit_for_auth_user(user_body)
    # Проверяется, что код ответа равен 400
    assert user_response.status_code == 400, "Status code is not 400"
