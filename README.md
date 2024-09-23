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
```pip install...```
- Run migrations:
```python manage.py migrations```
- Run project locally:
```python manage.py runserver```
- To launch browser: http://localhost:8000/api/contacts/

# 2. Testing API
API can be tested using the following endpoint on the deployed version of the app or locally:

Base URL: https://smartmate-49ddea62e918.herokuapp.com/

- i List all contacts
    - Method: GET
    - URL /api/contacts/
    - List of all contact.
    - curl -X GET http://localhost:8000/api/contacts/

- ii Create a contact
    - **Method**: POST
    - **URL**: `/api/contacts/`
    - **Phone Number Format**: The `phone_number` field needs to be in the **E.16 format** (e.g., `+12302340987`)
     **Request JSON Body**:
    ```json
    {
    "first_name": "John",
    "last_name": "Doe",
    "phone_number": "+12345607890"
    }
    ```

    **Example `curl` Command**:
    ```
      curl -X POST http://localhost:8000/api/contacts/ \
      -H "Content-Type: application/json" \
      -d '{"first_name": "John", "last_name": "Doe", "phone_number": "+12345607890"}'
    ```

- iii Delete a contact
    - Method: DELETE
    - URL: /api/contact/id
    - curl -X DELETE curl -X GET http://localhost:8000/api/contacts/1
