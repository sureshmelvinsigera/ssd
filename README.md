# SSDCS_PCOM7E August 2021

## Installation

Clone git repository

```
git clone git@github.com:sureshmelvinsigera/ssd.git
cd ssd
```

Create Python3 virtual environment

```
python3 -m venv <name_of_virtualenv>
````

Activate virtual environment

```
source venv/bin/activate
```

Run the following command in your terminal to install the requirements:

```sh
pip install -r requirements.txt
```

Note: you may need to use `pip3` instead of `pip` if you are using a Linux operating system.

Run the application by using the following commands:

```
python manage.py migrate
python manage.py runserver
```

Note that `python manage.py runserver` is sufficient to run the application; `python manage.py migrate` must be executed
if the model-based code has changed.

## API Endpoints

### Auth

| Method | Url          | Description  |   Endpoint security |
| ------ |------------| ------------| -------------|
| POST | http://127.0.0.1:8000/auth/users/astronaut/register/ | Log in | Public |
| POST | http://127.0.0.1:8000/auth/users/astronaut/login | Sign up | Public | 
| POST | http://127.0.0.1:8000/auth/users/scientist/register/ | Log in | Public | 
| POST | http://127.0.0.1:8000/auth/users/scientist/login | Sign up | Public | 
| GET | http://127.0.0.1:8000/astronauts/in-space/ | Retrieve all astronauts in space | Public
| GET | http://127.0.0.1:8000/astronauts/health-report/ | Retrieve all health reports of the current logged in astronaut| Private

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

#### http://127.0.0.1:8000/astronauts/health-report/

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

#### http://127.0.0.1:8000/astronauts/health-report/
Headers
```json
{
  "Key": "Authorization",
  "Value": JWT
  <token>
}

```

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "weight": 155,
      "blood_type": "B",
      "blood_pressure": 120,
      "heart_rate": 80
    }
  ]
}
```