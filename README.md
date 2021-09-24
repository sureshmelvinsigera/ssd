# SSDCS_PCOM7E August 2021

## API Endpoints

### Auth

| Method | Url          | Description  |
| ------ |------------| ------------|
| POST | /auth/users/register | Log in |
| POST | /auth/users/login | Sign up |


####  http://localhost:8000/auth/users/register/
```json
{
	"username":"markV",
	"first_name": "Mark Vande", 
	"last_name": "Hei",
	"email": "markv@nasa.gov",
	"password": "u73dg2626_#4"
}
```

#### http://localhost:8000/auth/users/login/
```json
{
	"username":"markV",
	"email": "markv@nasa.gov",
	"password": "u73dg2626_#4"
}
```