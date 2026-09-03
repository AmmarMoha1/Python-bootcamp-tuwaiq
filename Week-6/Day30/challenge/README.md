# Django Modular Routing Project

A simple Django project that demonstrates modular routing using multiple apps.

## Apps

- Users
- Courses
- Payments
- Dashboard

## Features

- Separate `urls.py` for each app
- `include()` for modular routing
- Named URLs and namespaces
- Dynamic routes using `slug`
- Class-Based View with `.as_view()`
- Shared `base.html`
- Template inheritance
- Central `templates` folder

## Example Routes

```text
/users/login/
/users/profile/
/courses/
/courses/python-basics/
/payments/checkout/
/dashboard/