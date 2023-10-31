# fish_shop_backend
## Setting up development environment
1. `git clone https://github.com/TheSadSenty/fish_shop_backend.git`
2.  `cd fish_shop_backend`
3.  `python3 -m venv env`
4.  `source env/bin/activate`
5.  `pip install -r requirements.txt`
6.  `python3 manage.py migrate` - applying migrations
8.  `python3 manage.py runserver`
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
- [ ] Decide if we want to stick with the default Django admin panel or develop our own
- [ ] Add tests
- [ ] Add [factory_boy](https://github.com/FactoryBoy/factory_boy) for fake data generation
