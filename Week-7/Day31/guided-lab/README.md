# Django Multi-Method View System

A simple Django project that demonstrates how to work with GET and POST requests using Class-Based Views, sessions, and JSON responses.

## Features

- Register page using GET and POST methods.
- Login page using GET and POST methods.
- Username is stored using Django Session.
- Login validates the username registered in the session.
- Profile page displays the logged-in username.
- Status endpoint returns a JSON response.
- Uses Class-Based Views (CBV) and Function-Based View (FBV).

## Routes

- `/accounts/register/` - Register page
- `/accounts/login/` - Login page
- `/accounts/profile/` - Profile page
- `/accounts/status/` - JSON status endpoint

## Screenshots

### Register Page

![Register](screenshots/register.png)

### Login Page

![Login](screenshots/login.png)

### Profile Page

![Profile](screenshots/profile.png)

## Run the Project

```bash
python manage.py migrate
python manage.py runserver