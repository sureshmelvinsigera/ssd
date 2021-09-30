# SSDCS_PCOM7E August 2021

## API Endpoints

### Auth

| Method | Url          | Description  |   Endpoint security |
| ------ |------------| ------------| -------------|
| POST | http://127.0.0.1:8000/auth/users/astronaut/register/ | Log in | Public |
| POST | http://127.0.0.1:8000/auth/users/astronaut/login | Sign up | Public | 
| POST | http://127.0.0.1:8000/auth/users/scientist/register/ | Log in | Public | 
| POST | http://127.0.0.1:8000/auth/users/scientist/login | Sign up | Public | 
| GET | http://127.0.0.1:8000/astronauts/in-space/ | Retrieve all astronauts in space | Public | Public 

#### http://127.0.0.1:8000/auth/users/astronaut/register/

```json
{
  "username": "markV",
  "first_name": "Mark Vande",
  "last_name": "Hei",
  "email": "markv@nasa.gov",
  "password": "u73dg2626_#4"
}
```

#### http://127.0.0.1:8000/auth/users/astronaut/login/

```json
{
  "username": "markV",
  "email": "markv@nasa.gov",
  "password": "u73dg2626_#4"
}
```

#### http://127.0.0.1:8000/auth/users/scientist/register/

```json
{
  "username": "LauraB",
  "first_name": "Laura",
  "last_name": "Bollweg",
  "email": "bollweg@nasa.gov",
  "password": "u73dg2626_#5"
}
```

#### http://127.0.0.1:8000/auth/users/scientist/login/

```json
{
  "username": "LauraB",
  "email": "bollweg@nasa.gov",
  "password": "u73dg2626_#5"
}
```

#### http://127.0.0.1:8000/astronauts/in-space/

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "username": "markV",
            "email": "markv@nasa.gov"
        }
    ]
}
```
