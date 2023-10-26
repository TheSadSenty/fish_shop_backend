# fish_shop_backend
## Setting up development environment
1. `git clone https://github.com/TheSadSenty/fish_shop_backend.git`
2.  `cd fish_shop_backend`
3.  `python3 -m venv env`
4.  `source env/bin/activate`
5.  `pip install -r requirements.txt`
6.  `python3 manage.py runserver`
## Applaying migrations
`python3 manage.py migrate`
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
## TODO
- [ ] Create `ProductsList` and `CategoryList` views so the server can return all products and categories as valid JSON
- [ ] Decide, which authentication mechanism we want to use (Basic authentication, JWT, Cookie Authentication, ...)
- [ ] Develop user model (fields, different types of user and etc.)
- [ ] Decide if we want to stick with the default Django admin panel or develop our own
- [ ] Add tests
