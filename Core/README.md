# Core Module

## Overview

This Core module serves as the central part of the application. It encloses all the domain entities and the contracts for use cases. It adheres to the Clean Architecture principles by Robert C. Martin, ensuring that the domain logic is separated from external concerns.

## Entities

Entities represent the business objects of the application. In the context of our virtual library system, the following entities are included:

- Book: Represents a book with its attributes like title, author, ISBN, status, etc.
- Student: Represents a student, including personal details and rental history.
- Librarian: Represents a librarian with capabilities to manage books and students.
- Administrator: Represents an administrative user with full system rights.

## Use Case Interfaces

These interfaces define the contracts for the use cases that operate on the entities. The use cases include actions such as managing (CRUD operations) books, students, and user accounts, as well as book rentals and returns.

- IBookRepository: Interface for book-related actions.
- IStudentRepository: Interface for student-related actions.
- ILibrarianRepository: Interface for librarian-related actions.
- IUserRepository: Generic interface for user-related actions.
- IAdminRepository: Interface for administrator-related actions.
- IAuthenticationService: Interface for handling authentication and authorization.

## Dependency Rule

The Core module should not be dependent on any other module of the application. All dependencies should point inward. Lower-level modules like Infrastructure and Presentation should depend on Core, not the other way around.

## Contribution

When contributing to this module, ensure that any new entities or use case interfaces align with the existing design principles and contribute towards a more robust and maintainable codebase.