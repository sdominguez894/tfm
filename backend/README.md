# Backend of the multi-blockchain block explorer


To run the backend [Python](https://www.python.org/) and [Poetry](https://python-poetry.org/) are required, install them before continuing.

From this folder, install all the dependencies using the following command:

    poetry install

Start the app with the command:

    poetry run uvicorn explorer.main:app

For development, start the server with the flag --reload to use hot-reload:

    poetry run uvicorn explorer.main:app --reload


After the server startup, visualize the interactive documentation of the web API in your browser at  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) or alternatively at [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) 

