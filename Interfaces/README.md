# Interfaces Module

This module contains the interface definitions that expose functionality to the external world. The interfaces consist mainly of API route definitions that will be responsible for dealing with HTTP requests to various endpoints of the virtual library system.

The endpoints created within this module will serve as the access points for the frontend to communicate with the backend, executing use cases such as creating, updating, and deleting entities or performing operations like user authentication and book loan management.

## API Routes

The `api_routes` directory contains all route definitions, grouped by entity or main responsibility. Each route file will be set up with FastAPI in mind, taking advantage of its declarative syntax to define operation types (GET, POST, PUT, DELETE), endpoint paths, and request/response schemas.

`book_routes.py` - Endpoints for managing books.
`student_routes.py` - Endpoints for managing students.
`librarian_routes.py` - Endpoints for managing librarians.
`administrator_routes.py` - Endpoints for managing administrators.
`authentication_routes.py` - Endpoints for user authentication.

The API layer will validate and serialize request data, invoke corresponding use cases from the UseCases module, handle any exceptions, and format the responses according to the REST standards.

## Notes

Ensure that all routes are authenticated and authorized where necessary according to the role permissions. Remember to keep this module apart from direct domain logic or data access logic to adhere to Clean Architecture principles.