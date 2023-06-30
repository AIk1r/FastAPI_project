FastAPI project

This project implements the principles of CRUD.
It connects to and interacts with the database.
You can look at the project itself and see for yourself, in the future it will be supplemented and brought to a more diligent form.

You wiil need to use commands:
pipenv shell
pipenv install fastapi fastapi-sqlalchemy pydantic alembic psycopg2 uvicorn python-dotenv

You will need to use the following commands to create the table:
alembic revision --autogenerate -m "New Migrations"
alembic upgrade head

Checked the functionality here: https://hoppscotch.io
