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

Run the website by typing the following in the root directory:

```
python -m http.server 8002
```

Note that `python manage.py runserver` is sufficient to run the application; `python manage.py migrate` must be executed
if the model-based code has changed.

## API Endpoints

| Method | Url          | Description  |   Endpoint security |
| ------ |------------| ------------| -------------|
| POST | http://127.0.0.1:8000/auth/users/astronaut/register/ | Log in | Public |
| POST | http://127.0.0.1:8000/auth/users/astronaut/login | Sign up | Public | 
| POST | http://127.0.0.1:8000/auth/users/scientist/register/ | Log in | Public | 
| POST | http://127.0.0.1:8000/auth/users/scientist/login | Sign up | Public | 
| GET | http://127.0.0.1:8000/astronauts/in-space/ | Retrieve all astronauts in space | Public
| GET | http://localhost:8000/astronaut/health-reports/ | Create new health report for current logged in astronaut | Private
| GET | http://localhost:8000/astronaut/health-reports/ | Retrieve all health reports of the current logged in astronaut| Private
| GET | http://localhost:8000/astronaut/health-reports/1 | Retrieve single health report of the current logged in astronaut| Private
| GET | http://localhost:8000/scientist/health-reports/ | Scientist retrieve all health report from all the astronauts | Private
| GET | http://localhost:8000/scientist/health-reports/1 | Scientist retrieve single health report of the astronaut| Private
| PUT | http://localhost:8000/scientist/health-reports/1 | Scientist give feed back to the astronaut| Private
| GET | http://127.0.0.1:8000/swagger-docs/ | API documentation | Public | 

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


### http://localhost:8000/astronaut/health-reports/
Create new health report
Headers
```json
{
  "Key": "Authorization",
  "Value": JWT <TOKEN>
}
```

```json
{
      "weight": 155,
      "blood_type": "B",
      "blood_pressure": 120,
      "heart_rate": 80,
      "muscle_mass": 34
}
```

#### http://127.0.0.1:8000/astronauts/health-report/
Headers
```json
{
  "Key": "Authorization",
  "Value": JWT <TOKEN>
}
```

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

#### http://127.0.0.1:8000/astronauts/health-reports/
Headers
```json
{
  "Key": "Authorization",
  "Value": JWT <TOKEN>
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


#### http://localhost:8000/astronaut/health-reports/1
Headers
```json
{
  "Key": "Authorization",
  "Value": JWT <TOKEN>
}
```

```json
{
    "id": 1,
    "weight": 155,
    "blood_type": "B",
    "blood_pressure": 120,
    "heart_rate": 80
}
```


##### http://localhost:8000/scientist/health-reports/1
Headers
```json
{
  "Key": "Authorization",
  "Value": JWT <TOKEN>
}
```

```json
{
    "weight": 155,
    "blood_type": "B",
    "blood_pressure": 120,
    "heart_rate": 80,
    "feedback": "No feedback as of yet"
}
```