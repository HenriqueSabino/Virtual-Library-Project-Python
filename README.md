# Virtual Library Backend

This is the backend part of the virtual library system, designed to manage the catalog of books and the users who interact with the library (students, librarians, and administrators).

## Getting Started

To set up the project:

1. Ensure you have Docker and Docker Compose installed.
2. Clone this repository.
3. Configure your environment variables in the `.env` file.
4. Run `docker-compose up` to start the services.

## Project Structure

- `Core/`: Contains the domain logic with entities, use cases, and interfaces.
- `UseCases/`: Contains application-specific business rules.
- `Interfaces/`: Contains the API routes that interact with the outside world.
- `Infrastructure/`: Handles data persistence and external interfaces implementation.
- `Presentation/`: Houses the application's entry point and orchestrates the user-facing part of the application.
- `Root/`: Contains configuration files and scripts for project setup and deployment.

## How To Use

Make API calls to perform actions like registering books, students, and librarians; managing loans and returns; and configuring system settings.

## Testing

Run the test suite with the following command:

```bash
docker-compose exec web pytest
```

## Deployment

The included `Dockerfile` and `docker-compose.yml` files should suffice for most deployment scenarios.

For detailed instructions and configurations, refer to the deployment documentation.

## Contributing

Please submit a pull request for any contributions.

For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.