# Core source code for the application
This directory contains the core functionality for the application. These code can be used from any part of the application including the microservices.

## models/
    This directory contains the models that are used to interact with the database. Each file in this directory represents a table/collection in the database depends on database type (SQL | MongoDB)

## schema/
    This directory contains the Pydantic models that represent the request and response schemas for the API. These models are used to validate incoming requests and to serialize outgoing responses.

## services/
    This directory contains the business logic of the application. Each file in this directory represents a service and contains functions that implement the business logic for that service.
    It also can contain a folder that will be like small libary for the application.

## app.py
    This file contains the function that creates the main FastAPI application. 
    It registers all microservices together, registers exceptions, etc, and returns the FastAPI application.

## db.py
    This file contains the code that sets up the database connection.

## utils.py
    This file contains utility functions that are used throughout the application.

## exceptions.py
    This file contains the custom exceptions that are raised by the application.