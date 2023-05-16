# Python-FastAPI-Boilerplate

Python-FastAPI-Boilerplate is a starter template for building large scale applications using FastAPI and microservices architecture. It provides a solid foundation for building scalable, maintainable, and modular applications.

## Installation

Clone the repository
```
 git clone https://github.com/<username>/<repo-name>.git
```

Create a virtual environment
```
 python -m venv env
```

Install dependencies
```
 pip install -r requirements.txt
```

Activate the virtual environment
```
 source env/bin/activate
```

## Get started

```
  uvicorn main:app --reload
```

## Project Structure

    python-fastapi-boilerplate/
    ├── config.py
    ├── core/
    │   ├── models/
    │   ├── schema/
    │   ├── services/
    │   ├── app.py
    │   ├── db.py
    │   ├── exceptions.py
    │   └── utils.py
    ├── microservices/
    │   ├── admin/
    │   │   ├── admin.py
    │   │   ├── dependencies.py
    │   │   ├── middleware.py
    │   │   ├── routers/
    │   │   │   └── v1/
    │   │   │       └── app_settings.py
    │   │   └── schema/
    │   ├── auth/
    │   │   ├── auth.py
    │   │   ├── dependencies.py
    │   │   ├── middleware.py
    │   │   ├── routers/
    │   │   │   └── v1/
    │   │   │       └── jwt_authentication.py
    │   │   └── schema/
    │   │   │       ├── AuthLoginRequest.py
    │   │   │       └── AuthRegisterRequest.py
    │   ├── primary/
    │   │   ├── dependencies.py
    │   │   ├── middleware.py
    │   │   ├── primary.py
    │   │   ├── routers/
    │   │   │   └── v1/
    │   │   │       └── article.py
    │   │   └── schema/
    │   └──         └── ArticleRequest.py
    ├── .gitignore
    ├── main.py
    ├── README.md
    └── requirements.txt


## API Documentation For Application And Microservices

    {server domain}/docs  # for main application
    {server domain}/{microservice prefix}/docs  # for microservice application

## License

This project is licensed under the MIT License. See the LICENSE file for details.