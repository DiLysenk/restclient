# Restclient

Пакет restclient добавляет логи request/response при обращении к REST API

## Установка

Используйте `pip` для установки пакета:

```shell
pip install git+https://github.com/ValeriyMenshikov/restclient.git
```

## Использование

Сделайте импорт structlog для красивого вывода лога в терминал.
Создайте экземпляр класса RestClient передайте туда базовый URL сервиса.
При вызове метода передайте в параметр path эндпоинт, и при необходимости другие параметры, которые содержит библиотека requests.
```python
import structlog
from restclient import Restclient


# Включение красивого отображения лога
structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)

# Создание клиента
client = Restclient(
    host='https://petstore.swagger.io'
)

# Вызов методов класса
pet_id = 1
result = client.get(path=f'/v2/pet/{pet_id}')
```

Результат:

```sh
{
    "data": null,
    "event": "request",
    "event_id": "8a492c44-c84b-4981-912f-29563bcb9d45",
    "full_url": "https://petstore.swagger.io/v2/pet/2",
    "headers": null,
    "json": null,
    "method": "GET",
    "params": null,
    "service": "api"
}
curl -X GET -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'User-Agent: python-requests/2.31.0' https://petstore.swagger.io/v2/pet/2
{
    "content": "b'{\"id\":2,\"category\":{\"id\":1232,\"name\":\"555\"},\"name\":\"CatTest\",\"photoUrls\":[],\"tags\":[{\"id\":2,\"name\":\"54\"}],\"status\":\"available\"}'",
    "curl": "curl -X GET -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'User-Agent: python-requests/2.31.0' https://petstore.swagger.io/v2/pet/2",
    "event": "response",
    "event_id": "8a492c44-c84b-4981-912f-29563bcb9d45",
    "headers": "{'Date': 'Tue, 18 Jul 2023 08:17:09 GMT', 'Content-Type': 'application/json', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET, POST, DELETE, PUT', 'Access-Control-Allow-Headers': 'Content-Type, api_key, Authorization', 'Server': 'Jetty(9.2.9.v20150224)'}",
    "json": {
        "category": {
            "id": 1232,
            "name": "555"
        },
        "id": 2,
        "name": "CatTest",
        "photoUrls": [],
        "status": "available",
        "tags": [
            {
                "id": 2,
                "name": "54"
            }
        ]
    },
    "service": "api",
    "status_code": 200,
    "text": "{\"id\":2,\"category\":{\"id\":1232,\"name\":\"555\"},\"name\":\"CatTest\",\"photoUrls\":[],\"tags\":[{\"id\":2,\"name\":\"54\"}],\"status\":\"available\"}"
}
```

## Документация

TODO:

## Лицензия
[MIT License](https://opensource.org/licenses/MIT)

