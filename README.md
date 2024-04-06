# fish_shop_backend
# Список любимых товаров
## Получить список любимых товаров
### Запрос
```shell
http http://127.0.0.1:8000/api/favorite/ 'Authorization: Token f3c4f7e337ea508f2a8a1ccb2681ec9a6471744e'
```
### Ответ
```http
HTTP/1.1 200 OK  
Allow: GET, POST, DELETE, HEAD, OPTIONS  
Content-Length: 849  
Content-Type: application/json  
Cross-Origin-Opener-Policy: same-origin  
Date: Thu, 07 Dec 2023 00:14:08 GMT  
Referrer-Policy: same-origin  
Server: WSGIServer/0.2 CPython/3.10.12  
Vary: Cookie  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY  
  
[  
   {  
       "product": {  
           "amount": 10,  
           "category": {  
               "name": "wiueiuwiyueiuyweiuy"  
           },  
           "description": "wdkwkdwkl;dkl;wk;dkw;dkl;wk;dkwkdkwdkwkldwk;dkw;dw",  
           "id": 1,  
           "name": "Hhshdhshd",  
           "photo": "/products_photos/download.jpeg",  
           "price": "123.00"  
       }  
   },  
   {  
       "product": {  
           "amount": 7,  
           "category": {  
               "name": "wiueiuwiyueiuyweiuy"  
           },  
           "description": "shjkfhjksdfjksjkfjkdsf",  
           "id": 2,  
           "name": "djdsjklfjklsfjklsjklffsjlks",  
           "photo": "/products_photos/download_BnNGcbA.jpeg",  
           "price": "1212.00"  
       }  
   },  
   {  
       "product": {  
           "amount": 6,  
           "category": {  
               "name": "wiueiuwiyueiuyweiuy"  
           },  
           "description": "fwjowjefwjklfjwjlfjklwjklfw",  
           "id": 3,  
           "name": "iuyiouiouioufweiufiweijuf",  
           "photo": "/products_photos/download_HOCxkfS.jpeg",  
           "price": "3232.00"  
       }  
   },  
   {  
       "product": {  
           "amount": 5,  
           "category": {  
               "name": "wiueiuwiyueiuyweiuy"  
           },  
           "description": "",  
           "id": 4,  
           "name": "sdsijojiocsjkcsjvjksjvs",  
           "photo": "/products_photos/download_J4UZXeM.jpeg",  
           "price": "23232.00"  
       }  
   }  
]
```
## Добавить товар в список
### Запрос
```shell
http POST http://127.0.0.1:8000/api/favorite/ 'Authorization: Token f3c4f7e337ea508f2a8a1ccb2681ec9a6471744e' product=4
```
### Ответ
```http
HTTP/1.1 200 OK  
Allow: GET, POST, DELETE, HEAD, OPTIONS  
Content-Length: 0  
Cross-Origin-Opener-Policy: same-origin  
Date: Thu, 07 Dec 2023 00:19:41 GMT  
Referrer-Policy: same-origin  
Server: WSGIServer/0.2 CPython/3.10.12  
Vary: Cookie  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY
```
## Удалить товар из списка
### Запрос
```shell
http DELETE http://127.0.0.1:8000/api/favorite/ 'Authorization: Token f3c4f7e337ea508f2a8a1ccb2681ec9a6471744e' product=3
```
### Ответ
```http
HTTP/1.1 200 OK  
Allow: GET, POST, DELETE, HEAD, OPTIONS  
Content-Length: 0  
Cross-Origin-Opener-Policy: same-origin  
Date: Thu, 07 Dec 2023 00:16:00 GMT  
Referrer-Policy: same-origin  
Server: WSGIServer/0.2 CPython/3.10.12  
Vary: Cookie  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY
```
# Пользователь

## Регистрация
### Запрос
```shell
http POST http://127.0.0.1:8000/api/user/ username=Maxim first_name=Maxim last_name=Kasyanov email=maxim@ema  
il.com password=iwwhkdhkwdwdjwdghwd
```

```shell
http POST http://127.0.0.1:8000/api/user/ username=Maxim5 first_name= last_name= email= password=1234
```
### Ответ
```http
HTTP/1.1 200 OK  
Allow: POST, OPTIONS  
Auth-Token: 457d29ad9ca4cb195597b2b51756a075436197e4  
Content-Length: 0  
Cross-Origin-Opener-Policy: same-origin  
Date: Thu, 07 Dec 2023 22:22:00 GMT  
Referrer-Policy: same-origin  
Server: WSGIServer/0.2 CPython/3.10.12  
Vary: origin  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY
```
## Вход
### Запрос
```shell
http POST http://127.0.0.1:8000/api/user/login/ username=Maxim5 password=1234
```
### Ответ
```http
HTTP/1.1 200 OK  
Allow: POST, OPTIONS  
Auth-Token: 457d29ad9ca4cb195597b2b51756a075436197e4  
Content-Length: 0  
Cross-Origin-Opener-Policy: same-origin  
Date: Thu, 07 Dec 2023 22:23:01 GMT  
Referrer-Policy: same-origin  
Server: WSGIServer/0.2 CPython/3.10.12  
Vary: origin  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY
```
## Выход
### Запрос
```shell
http DELETE http://127.0.0.1:8000/api/user/logout/ 'Authorization: Token f3c4f7e337ea508f2a8a1ccb2681ec9a6471744e'
```
### Ответ
```http
HTTP/1.1 200 OK  
Allow: DELETE, OPTIONS  
Content-Length: 0  
Cross-Origin-Opener-Policy: same-origin  
Date: Thu, 07 Dec 2023 22:24:25 GMT  
Referrer-Policy: same-origin  
Server: WSGIServer/0.2 CPython/3.10.12  
Vary: origin  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY
```
## Информация о пользователе
### Запрос
```shell
http http://127.0.0.1:8000/api/user_informathion/ 'Authorization: Token f3c4f7e337ea508f2a8a1ccb2681ec9a6471744e'
```
### Ответ
```http
HTTP/1.1 200 OK  
Allow: GET, HEAD, OPTIONS  
Content-Length: 63  
Content-Type: application/json  
Cross-Origin-Opener-Policy: same-origin  
Date: Fri, 01 Dec 2023 18:07:59 GMT  
Referrer-Policy: same-origin  
Server: WSGIServer/0.2 CPython/3.10.12  
Vary: Cookie  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY  
  
{  
   "email": "",  
   "first_name": "",  
   "last_name": "",  
   "username": "carlos"  
}
```
# Товары и категории
## Вывести список всех товаров
### Запрос
```shell
http http://127.0.0.1:8000/api/products/
```
### Ответ
```http
HTTP/1.1 200 OK  
Allow: GET, HEAD, OPTIONS  
Content-Length: 271  
Content-Type: application/json  
Cross-Origin-Opener-Policy: same-origin  
Date: Fri, 01 Dec 2023 17:48:46 GMT  
Referrer-Policy: same-origin  
Server: WSGIServer/0.2 CPython/3.10.12  
Vary: Cookie  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY  
  
{  
   "count": 2,  
   "next": "http://127.0.0.1:8000/api/products/?page=2",  
   "previous": null,  
   "results": [  
       {  
           "amount": 4,  
           "category": {  
               "name": "43434"  
           },  
           "description": "",  
           "id": 1,  
           "name": "dfdfdfdf",  
           "photo": "http://127.0.0.1:8000/products_photos/Screenshot_20230415_000841.png",  
           "price": "3434.00"  
       }  
   ]  
}
```
## Вывести конкретный товар
### Запрос
```shell
http http://127.0.0.1:8000/api/products/2/
```
### Ответ
```http
HTTP/1.1 200 OK  
Allow: GET, HEAD, OPTIONS  
Content-Length: 230  
Content-Type: application/json  
Cross-Origin-Opener-Policy: same-origin  
Date: Fri, 01 Dec 2023 17:50:16 GMT  
Referrer-Policy: same-origin  
Server: WSGIServer/0.2 CPython/3.10.12  
Vary: Cookie  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY  
  
{  
   "amount": 6,  
   "category": {  
       "name": "43434"  
   },  
   "description": "scs,cs,ckjnsn,mcnsmc,nsn,csn,mc,nsmcnmsnc,m",  
   "id": 2,  
   "name": "skhdjshkdshkdhskj",  
   "photo": "http://127.0.0.1:8000/products_photos/Screenshot_20230415_000841.png",  
   "price": "565.00"
```
## Вывести список всех категорий
### Запрос
```shell
http http://127.0.0.1:8000/api/categories/
```
### Ответ
```http
HTTP/1.1 200 OK  
Allow: GET, HEAD, OPTIONS  
Content-Length: 68  
Content-Type: application/json  
Cross-Origin-Opener-Policy: same-origin  
Date: Fri, 01 Dec 2023 17:58:59 GMT  
Referrer-Policy: same-origin  
Server: WSGIServer/0.2 CPython/3.10.12  
Vary: Cookie  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY  
  
{  
   "count": 1,  
   "next": null,  
   "previous": null,  
   "results": [  
       {  
           "name": "43434"  
       }  
   ]  
}
```
## Вывести конкретную категорию
### Запрос
```shell
http http://127.0.0.1:8000/api/categories/1/
```
### Ответ
```http
HTTP/1.1 200 OK  
Allow: GET, HEAD, OPTIONS  
Content-Length: 16  
Content-Type: application/json  
Cross-Origin-Opener-Policy: same-origin  
Date: Fri, 01 Dec 2023 17:59:36 GMT  
Referrer-Policy: same-origin  
Server: WSGIServer/0.2 CPython/3.10.12  
Vary: Cookie  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY  
  
{  
   "name": "43434"  
}
```
# Корзина
## Добавление товара в корзину
### Запрос
```shell
http POST http://127.0.0.1:8000/api/cart/ 'Authorization: Token f3c4f7e337ea508f2a8a1ccb2681ec9a6471744e' product_id=1 quantity=3434
```
### Ответ
```http
HTTP/1.1 201 Created  
Allow: GET, POST, HEAD, OPTIONS  
Content-Length: 276  
Content-Type: application/json  
Cross-Origin-Opener-Policy: same-origin  
Date: Fri, 01 Dec 2023 17:18:44 GMT  
Referrer-Policy: same-origin  
Server: WSGIServer/0.2 CPython/3.10.12  
Vary: Cookie  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY  
  
{  
   "created_at": "2023-12-01T17:18:44.498631Z",  
   "id": 9,  
   "item": {  
       "amount": 4,  
       "category": {  
           "name": "43434"  
       },  
       "description": "",  
       "id": 1,  
       "name": "dfdfdfdf",  
       "photo": "/products_photos/Screenshot_20230415_000841.png",  
       "price": "3434.00"  
   },  
   "quantity": 3434,  
   "updated_at": "2023-12-01T17:18:44.498644Z"  
}
```
## Редактирование товара в корзине
### Запрос
```shell
http PUT http://127.0.0.1:8000/api/cart/1/ 'Authorization: Token f3c4f7e337ea508f2a8a1ccb2681ec9a6471744e' product_id=1 quantity=34
```
### Ответ
```http
HTTP/1.1 200 OK  
Allow: GET, PUT, DELETE, HEAD, OPTIONS  
Content-Length: 0  
Cross-Origin-Opener-Policy: same-origin  
Date: Fri, 01 Dec 2023 17:23:06 GMT  
Referrer-Policy: same-origin  
Server: WSGIServer/0.2 CPython/3.10.12  
Vary: Cookie  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY
```
## Удаление товара из корзины
### Запроc
```shell
http DELETE http://127.0.0.1:8000/api/cart/1/ 'Authorization: Token f3c4f7e337ea508f2a8a1ccb2681ec9a6471744e'
```
### Ответ
```http
HTTP/1.1 200 OK  
Allow: GET, PUT, DELETE, HEAD, OPTIONS  
Content-Length: 0  
Cross-Origin-Opener-Policy: same-origin  
Date: Fri, 01 Dec 2023 17:24:00 GMT  
Referrer-Policy: same-origin  
Server: WSGIServer/0.2 CPython/3.10.12  
Vary: Cookie  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY
```
## Вывести все товары в корзине
### Запроc
```shell
http http://127.0.0.1:8000/api/cart/ 'Authorization: Token f3c4f7e337ea508f2a8a1ccb2681ec9a6471744e'
```
### Ответ
```http
HTTP/1.1 200 OK  
Allow: GET, POST, HEAD, OPTIONS  
Content-Length: 1109  
Content-Type: application/json  
Cross-Origin-Opener-Policy: same-origin  
Date: Fri, 01 Dec 2023 17:27:12 GMT  
Referrer-Policy: same-origin  
Server: WSGIServer/0.2 CPython/3.10.12  
Vary: Cookie  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY  
  
[  
   {  
       "created_at": "2023-11-28T15:10:48.824336Z",  
       "id": 6,  
       "item": {  
           "amount": 4,  
           "category": {  
               "name": "43434"  
           },  
           "description": "",  
           "id": 1,  
           "name": "dfdfdfdf",  
           "photo": "/products_photos/Screenshot_20230415_000841.png",  
           "price": "3434.00"  
       },  
       "quantity": 3434,  
       "updated_at": "2023-11-28T15:10:48.824350Z"  
   },  
   {  
       "created_at": "2023-11-28T15:10:50.231260Z",  
       "id": 7,  
       "item": {  
           "amount": 4,  
           "category": {  
               "name": "43434"  
           },  
           "description": "",  
           "id": 1,  
           "name": "dfdfdfdf",  
           "photo": "/products_photos/Screenshot_20230415_000841.png",  
           "price": "3434.00"  
       },  
       "quantity": 3434,  
       "updated_at": "2023-11-28T15:10:50.231272Z"  
   },  
   {  
       "created_at": "2023-11-28T15:09:28.204252Z",  
       "id": 4,  
       "item": {  
           "amount": 4,  
           "category": {  
               "name": "43434"  
           },  
           "description": "",  
           "id": 1,  
           "name": "dfdfdfdf",  
           "photo": "/products_photos/Screenshot_20230415_000841.png",  
           "price": "3434.00"  
       },  
       "quantity": 3434,  
       "updated_at": "2023-11-28T15:13:08.510458Z"  
   },  
   {  
       "created_at": "2023-12-01T17:18:44.498631Z",  
       "id": 9,  
       "item": {  
           "amount": 4,  
           "category": {  
               "name": "43434"  
           },  
           "description": "",  
           "id": 1,  
           "name": "dfdfdfdf",  
           "photo": "/products_photos/Screenshot_20230415_000841.png",  
           "price": "3434.00"  
       },  
       "quantity": 3434,  
       "updated_at": "2023-12-01T17:18:44.498644Z"  
   }  
]
```
## Вывести конкретный товар в корзине
### Запроc
```shell
http http://127.0.0.1:8000/api/cart/4/ 'Authorization: Token f3c4f7e337ea508f2a8a1ccb2681ec9a6471744e''
```
### Ответ
```http
HTTP/1.1 200 OK  
Allow: GET, PUT, DELETE, HEAD, OPTIONS  
Content-Length: 276  
Content-Type: application/json  
Cross-Origin-Opener-Policy: same-origin  
Date: Fri, 01 Dec 2023 17:29:58 GMT  
Referrer-Policy: same-origin  
Server: WSGIServer/0.2 CPython/3.10.12  
Vary: Cookie  
X-Content-Type-Options: nosniff  
X-Frame-Options: DENY  
  
{  
   "created_at": "2023-11-28T15:09:28.204252Z",  
   "id": 4,  
   "item": {  
       "amount": 4,  
       "category": {  
           "name": "43434"  
       },  
       "description": "",  
       "id": 1,  
       "name": "dfdfdfdf",  
       "photo": "/products_photos/Screenshot_20230415_000841.png",  
       "price": "3434.00"  
   },  
   "quantity": 3434,  
   "updated_at": "2023-11-28T15:13:08.510458Z"  
}
```
