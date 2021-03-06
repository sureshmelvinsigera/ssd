# SSDCS_PCOM7E August 2021
[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/summary/new_code?id=sureshmelvinsigera_ssd)
[![SSD](https://circleci.com/gh/sureshmelvinsigera/ssd.svg?style=svg)](https://circleci.com/gh/sureshmelvinsigera/ssd)

This repository contains a monolithic application comprised of a database, application, and website frontend. The IoT communication code is accessible from the `Infrastructure` folder, and contains a `README` of its own. Click the SonarCloud badge above for code analysis reports (including vulnerabilities), and click the CircleCI badge above for CI/CD reports (which displays linting results and automated tests). Copies of these reports are available in the `reports` folder.

## Installation

Clone the repository:

```
git clone https://github.com/sureshmelvinsigera/ssd.git
cd ssd
```

Run the following command in your terminal to install the requirements:

```sh
pip install -r requirements.txt
```

Run the application by using the following commands:

```
python manage.py migrate
python manage.py runserver
```
This will start the Django application. You will then need to begin hosting the website. Run the website by running the following command in the root directory, and then open the website by visiting `localhost:8002` in your web browser.
 

```
python -m http.server 8002
```

Note: you may need to use `python3` and `pip3` instead of `python` and `pip` respectively for these commands, if you are using a Linux operating system.

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

## Linting
Autopep8 is used to lint code. Please note that the build will fail if your code does not comply with PEP 8 formatting standards. If your build fails due to linting, find out which lines to change by visiting the CircleCI page by clicking on the badge at the top of this README, locating the failed build, and then clicking "Linting code according to PEP 8" for details. 

## Unimplemented Security Measures
The security of the application could be improved further, however, due to specific constraints, additional measures could not be implemented. These measures are briefly discussed below.

### HTTPS
HTTPS improves website security by encrypting communications and making website spoofing more difficult (Cloudflare, 2021). This was not implemented due to the costs associated with acquiring an SSL certificate, however, any production-ready system must use this protocol.

### Code Obfuscation
Due to the existence of a web frontend, attackers can attempt to find ways of compromising the system by analyzing the JavaScript code. Obfuscation can prevent this from happening by obscuring all JavaScript through various means, such as changing variable names, adding decoy code which does not do anything, and other conversion mechanisms to make it extremely difficult to interpret the code (JScrambler, 2021). This would only be done at the deployment phase of a project, and would not be seen in a repository- only the website. This has not been implemented because the application is currently not hosted online. 

## References
Cloudflare. (2021) Why use HTTPS? Available from: https://www.cloudflare.com/en-gb/learning/ssl/why-use-https/ [Accessed 24 October 2021].\
Django documentation. (2021) Customizing authentication in Django. Available from: https://docs.djangoproject.com/en/3.2/topics/auth/customizing/ [Accessed 25 October 2021].\
Github. (2021) Encrypted secrets. Available from: https://docs.github.com/en/actions/security-guides/encrypted-secrets [Accessed 24 October 2021].\
JScrambler. (2021) JavaScript Obfuscation: The Definitive Guide (2021). Available from: https://blog.jscrambler.com/javascript-obfuscation-the-definitive-guide [Accessed 24 October 2021].\
