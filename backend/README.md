# Backend of the multi-blockchain block explorer


To run the backend [Python](https://www.python.org/) and [Poetry](https://python-poetry.org/) are required, install them before continuing.

From this folder (/backend/), install all the dependencies using the following command:

    poetry install

Start the app with the command:

    poetry run uvicorn src.main:app

For development, start the server with the flag --reload to use hot-reload:

    poetry run uvicorn src.main:app --reload


After the server startup, visualize the interactive documentation of the web API in your browser at  [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) or alternatively at [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) 


## Docker

To build the docker image run the following command:

    docker build -t your_username/multichain-backend .

To run the docker image, run:

    docker run your_username/multichain-backend

To push the docker image to Docker Hub, run:

    docker push your_username/multichain-backend

