import structlog

from restclient import Restclient

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get():
    # Создание экземпляра класса
    client = Restclient(
        host='https://petstore.swagger.io'
    )

    # Вызов методов класса
    pet_id = 2
    result = client.get(path=f'/v2/pet/{pet_id}')
