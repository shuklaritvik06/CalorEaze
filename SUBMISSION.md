# Calories API

The Calories API is a RESTful API that provides information about the calorie content of various food items you have consumed in the day.

I decided to use Django Rest Framework (DRF) for my project due to its numerous benefits and features that align perfectly with my requirements for building a robust and scalable API.

- Rapid Development
- Flexibility
- Serialization
- Authentication and Permissions

![Screenshot from 2023-06-19 01-15-19](https://github.com/DiveHQ-Octernships/dive-backend-engineering-octernship-shuklaritvik06/assets/72812470/c1fcabe9-77f0-488f-9eaa-77d143215327)


## Features

- [x] Authentication using JWT
- [x] Role Based Authorization
- [x] Swagger UI
- [x] DRF Permissions
- [x] DRF Validators
- [x] Google OAuth
- [x] Serialization

### Some Endpoints

**Status**

```markdown
/status/
```

*Response*

```json
{
  "status": "success",
  "code": 200,
  "message": "Calorie API is running smoothly",
  "data": {
    "version": "1.0.0",
    "timestamp": "2023-06-18T16:06:03.388Z"
  }
}
```

**Authentication** (No Permission Classes)

*Register*

- /api/v1/auth/signup/

*Response*

```json
{
  "status": "success",
  "code": 201,
  "message": "User registered successfully",
  "data": {
    "username": "rakesh",
    "email": "rakesh@rakesh.com",
    "registration_date": "2023-06-18",
    "registration_time": "16:08:43.678004",
    "first_name": "Rakesh",
    "last_name": "Nagar",
    "role": "REGULAR"
  }
}
```

*Login*

- /api/v1/auth/login/

*Response*

```json
{
  "status": "success",
  "message": "Login successful",
  "data": {
    "user": {
      "email": "rakesh@rakesh.com",
      "first_name": "Rakesh",
      "last_name": "Nagar",
      "role": "REGULAR",
      "registration_date": "2023-06-18",
      "registration_time": "16:08:43.678004"
    },
    "auth_token": {
      "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3MTA4MTUyLCJpYXQiOjE2ODcxMDQ1NTIsImp0aSI6IjBkYzE1YmQwZDgzMzQzNmM4MmE1OWY1ZWU3MjRlMDUwIiwidXNlcl9pZCI6MTIsImVtYWlsIjoicmFrZXNoQHJha2VzaC5jb20iLCJyb2xlIjoiUkVHVUxBUiIsImlzcyI6IkRpdmVIUSJ9.hb8SdWEsFaAcUCsr7qkYRrFUummRtIF-JgcletlddX4",
      "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NzE5MDk1MiwiaWF0IjoxNjg3MTA0NTUyLCJqdGkiOiI5MDY3ZDg3NDI2NGM0Yzc4ODJmNWJjYTU4N2Y0N2ZiYyIsInVzZXJfaWQiOjEyLCJlbWFpbCI6InJha2VzaEByYWtlc2guY29tIiwicm9sZSI6IlJFR1VMQVIiLCJpc3MiOiJEaXZlSFEifQ.Yvo0bkY2yddmlg-ZJyGa2AxrFWs6hbAY2ErVmKoWo_w"
    }
  }
}
```

> Setup Locally to use Swagger UI and interact with the api easily

### How to set up locally?

- Clone the repo

```
git clone https://github.com/DiveHQ-Octernships/dive-backend-engineering-octernship-shuklaritvik06.git
```

- Change the working directory

```
cd dive-backend-engineering-octernship-shuklaritvik06
```

- Set up .env file

```
Make a new file with the help of .env.example file

Define all the environment variables in that file. Navigate to https://www.nutritionix.com to get the APP Key and APP Id
```

- Install the dependencies

```
pip install -r requirements.txt
```

- Migrate the models to the db

```
python3 manage.py makemigrations --settings "api.settings.local"
python3 manage.py migrate --settings "api.settings.local"
```

- Run the server

There are 2 different settings for production and development, we will use the dev one

```
python3 manage.py runserver --settings "api.settings.local"
```

Hurray! Your API Server has been successfully started!

Now go to http://localhost:8000/docs/swagger and Authenticate yourself using the Google OAuth or username & password

**Setup Google Auth**

- Create a Super User

```
python3 manage.py createsuperuser --settings "api.settings.local"
```

- Login to the Admin Portal

![Screenshot from 2023-06-18 21-54-34](https://github.com/DiveHQ-Octernships/dive-backend-engineering-octernship-shuklaritvik06/assets/72812470/153df697-0839-4a48-83af-2f165fc5c8b3)


You would see Social Applications on the left side CLICK on that and then ADD SOCIAL APPLICATION

- Now Select the Google as provider and fill the client id and secret from the Google console

Google OAuth Setup Completed Successfully!


**Testing**

Run Tests

```markdown
python3 manage.py test --settings "api.settings.local"
```

**Docker Way**

- Pull the image from docker hub

```commandline
docker push ritvikshukla/caloriesapi:latest
```

```commandline
docker run -p 8000:8000 -d ritvikshukla/caloriesapi
```
