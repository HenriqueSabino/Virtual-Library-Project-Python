# UseCases Module

The UseCases module contains the application's business logic. Each use case represents a discrete piece of functionality within the system, such as creating a book, updating a student's information, or loaning a book to a student.

The module is organized by feature, with each sub-directory representing a different domain of the system:

- book_management
- student_management
- librarian_management
- admin_management
- authentication
- loan_management

Each use case follows the Command or Query pattern and is designed to be invoked by the Presentation module. Dependency inversion is used to reference interfaces defined in the Core module, ensuring the use cases remain decoupled from specific infrastructure implementations.

## Use Case Files

Each use case is implemented as a separate Python file within its respective sub-directory. The name of the file indicates the action and the domain it belongs to. For instance, `CreateBook.py` handles the logic for creating new book entries in the system.

## Dependency Injection

Use cases depend on interfaces rather than concrete classes. Dependencies are injected at runtime, allowing for easy swapping of implementations and facilitating testing.

## Important Notes

- Each use case should handle only one task or operation.
- Business rules are enforced within use cases, ensuring the Core module remains pure and agnostic to application logic.
- Use cases can interact with each other if necessary, but should maintain a clear boundary of responsibilities.