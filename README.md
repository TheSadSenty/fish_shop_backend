# fish_shop_backend
## Setting up development environment
1. `git clone https://github.com/TheSadSenty/fish_shop_backend.git`
2.  `cd fish_shop_backend`
3.  `touch .env`. Add the following lines:
```shel
DEBUG=True
SECRET_KEY=django-insecure-@e%9m0aw_!hnhip05to+a0eu+^f*kp=(yc9ghzoh5!a79ha@zr
POSTGRES_DB=postgres 
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=1234
POSTGRES_ADDRESS=localhost
```
4.  `python3 -m venv env`
5.  `source env/bin/activate`
6.  `pip install -r requirements.txt`
7.  `docker run --name tmp_db -p 5432:5432 -e POSTGRES_PASSWORD=1234 -d postgres:16.0` - Create a temporal database for development.
8.  `python3 manage.py migrate` - Applying migrations
9.  `python3 manage.py runserver`
## Launch the app in Docker
1. `touch .env`. Add the following lines:
```shel
DEBUG=True
SECRET_KEY=django-insecure-@e%9m0aw_!hnhip05to+a0eu+^f*kp=(yc9ghzoh5!a79ha@zr
POSTGRES_DB=postgres 
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=1234
POSTGRES_ADDRESS=postgres
```
2. `docker-compose up -d --build`
3. `docker container exec -it backend /usr/bin/python3 /app/manage.py migrate`
## Creating test data
`python3 manage.py shell` - Launch interactive shell
```python
from products.models import Products
from products.models import Category
c = Category(name="dsdsdsfsf")
c.save()
p = Products(name="fieffelije", description="ejlfjlefjkl", price=111.02, category=c)
p.save()
```
## Creating `.env` file
`touch .env`

Launch interactive shell:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
# <random abracadabra>
```
Paste `SECRET_KEY=<random abracadabra>` and `DEBUG=True` to `.env` file
## TODO
- [x] Create `ProductsList` and `CategoryList` views so the server can return all products and categories as valid JSON
- [ ] Decide, which authentication mechanism we want to use (Basic authentication, JWT, Cookie Authentication, ...)
- [ ] Develop user model (fields, different types of user and etc.)
- [-] Decide if we want to stick with the default Django admin panel or develop our own
- [ ] Add tests
- [ ] Add [protobuf](https://github.com/protocolbuffers/protobuf) support to export API schema
- [ ] Add [factory_boy](https://github.com/FactoryBoy/factory_boy) for fake data generation
- [ ] Decide if we want to return JSON instead of HTTP statuses for error handling. Something similar to this:

```
{
   "ok":false,
   "error_code":404,
   "description":"Not Found"
}
```
```
{
  "ok": true,
  "result": [
    {
      "update_id": 615081885,
      "message": {
        "message_id": 486,
        "from": {
          "id": 418155406,
          "is_bot": false,
          "first_name": "Maxim",
          "last_name": "Kasyanov",
          "username": "thesadsenty",
          "language_code": "ru"
        },
        "chat": {
          "id": 418155406,
          "first_name": "Maxim",
          "last_name": "Kasyanov",
          "username": "thesadsenty",
          "type": "private"
        },
        "date": 1698719198,
        "text": "hdfdf"
      }
    }
  ]
}
```
