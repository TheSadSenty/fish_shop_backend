# fish_shop_backend
## Setting up development environment
1. `git clone https://github.com/TheSadSenty/fish_shop_backend.git`
2.  `cd fish_shop_backend`
3.  `python3 -m venv env`
4.  `source env/bin/activate`
5.  `pip install -r requirements.txt`
6.  `python3 manage.py runserver`
## TODO
- [ ] Create `ProductsList` and `Category` views so the server can return all products and categories as valid JSON
- [ ] Decide, which authentication mechanism we want to use (Basic authentication, JWT, Cookie Authentication, ...)
- [ ] Develop user model (fields, different types of user and etc.)
- [ ] Decide if we want to stick with the default Django admin panel or develop our own
- [ ] Add tests
