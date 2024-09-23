# SmartMate Emergency Contact API

This API allows you to create, list, and delete emergency contacts. Below are the steps to set up the project locally and details on how to use the API endpoints.

# 1. Project Setup

### Prerequisites:
- Python 3.10 or higher
- Django 5.1.1
- Pip

### Steps
- Clone the Repository
- cd smartmate
- Set Up and activate a Virtual Environment
- Install dependencies:
```bash pip install -r requirements.txt```
- Run migrations
- Run project locally
```bash python manage.py runserver```
- Launch http://localhost:8000/api/contacts/ in browser

# 2. Testing API
API can be tested using the following endpoint on the deployed version of the app:

Base URL: https://smartmate-49ddea62e918.herokuapp.com/

- i List all contacts
    - Method: GET
    - URL /api/contacts/
    - List of all contact.
- ii Create a contact
    - Method: POST
    - URL: /api/contacts/
    - Request JSON Body:
    ```bash {
    "first_name": "John",
    "last_name": "Doe",
    "phone_number": "+1234567890"
    }
- iii Delete a contact
    - Method: DELETE
    - URL: /api/contact/id
