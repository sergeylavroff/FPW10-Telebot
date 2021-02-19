import requests
import json

r = requests.get(
    'https://baconipsum.com/api/?type=all-meat&paras=1&start-with-lorem=0&format=json')  # делаем запрос на сервер по переданному адресу
texts = json.loads(r.content)
print(type(texts))
print(texts[0])