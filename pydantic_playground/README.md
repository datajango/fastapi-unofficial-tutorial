# Pydantic Playground Notes

By Anthony Leotta

## From [Pydantic](https://lyz-code.github.io/blue-book/coding/python/pydantic/)

- Pydantic is a data validation and settings management using python type annotations.

- pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.

- Define how data should be in pure, canonical python; check it with pydantic.

- Advantages:
    - Perform data validation in an easy and nice way.
    - Seamless integration with FastAPI and Typer.
    - Nice way to export the data and data schema.
- Disadvantages:
    - You can't define cyclic relationships, therefore there is no way to simulate the backref SQLAlchemy function.

##