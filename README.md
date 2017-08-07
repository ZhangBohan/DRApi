# DRApi

Don't repeat API offer some useful APIs.

## Get website favion API

```
GET /icon?url=http://sanic.readthedocs.io/en/latest/sanic/routing.html#request-parameters
```

- `url`: target page url

response favion url if found an url for this page

```
{"url": "http://sanic.readthedocs.io/favicon.ico"}
```

## Get data QR code

```
GET /qrcode?data=balabala
```

OR

```
POST /qrcode
{"foo": "bar"}
```

response qrcode image