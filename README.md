# Tivix Family Budget application

## About the project

Application was created for the recruitment task.


## Installation

### Prerequisites:
  * [docker](https://docs.docker.com/docker-for-mac/install/)
  * [docker-compose](https://docs.docker.com/compose/install/)

### Project set up:
  1. Clone this repository.
  2. Run `docker-compose build`.
  3. Run `docker-compose up`.
  4. Run `docker-compose run server python manage.py migrate`
  5. Test endpoints via `Postman`.


### Swagger UI (API Documentation):

Go to the: [http://localhost:8000/docs](http://localhost:8000/docs)

### TODO:
  * Testing
  * Documentation
  * Dockerizing frontend
