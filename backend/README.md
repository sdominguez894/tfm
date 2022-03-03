# Backend of the multi-blockchain block explorer


To run the backend [Python](https://www.python.org/) and [Poetry](https://python-poetry.org/) are required, install them before continuing.

Install all the dependencies using the following command:

    poetry install

Start the app with the command:

    poetry run uvicorn explorer.main:app

For development, start the server with the flag --reload to use hot-reload:

    poetry run uvicorn explorer.main:app --reload