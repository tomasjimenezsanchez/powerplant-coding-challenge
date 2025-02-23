
Powerplant Coding Challenge

This project is an API that calculates the optimal power production for various power plants based on demand and fuel costs. It is built with FastAPI and can be run locally or inside a Docker container.


Project Structure

powerplant-coding-challenge/
│── app/                      # API main code
│   │── main.py               # API entry point
│   │── models.py             # Data models using Pydantic
│   │── services.py           # Energy optimization logic
│   │── utils.py              # Funciones auxiliares (Opcionales)
│
│── example_payloads/         # JSON test cases
│── tests/                    # Unit tests (ejemplo)
|── requirements.txt          # Python dependencies
│── README.md                 # Project documentation
│── Dockerfile                # Docker container setup


Prerequisites

Before running the API, make sure you have the following installed:

🔹 Python 3.8 or higher → Download here
🔹 Docker (Optional) → Download here
🔹 pip and virtualenv (for virtual environments)

Installation and Running Locally

1.- Clone the Repository
git clone https://github.com/tomasjimenezsanchez/powerplant-coding-challenge.git
cd powerplant-coding-challenge

2.- Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows

3.- Install Dependencies
pip install -r requirements.txt
4.- Start the API
python -m uvicorn app.main:app --host 0.0.0.0 --port 8888 --reload

The API will be available at:
 http://127.0.0.1:8888/docs (Swagger UI)
 http://127.0.0.1:8888/redoc (Redoc UI)


Running the API with Docker

    1.- Build the Docker Image
    docker build -t powerplant-api .

    2.- Run the Container
    docker run -p 8888:8888 powerplant-api

    3.- Check if the API is running:
    docker ps

    Stop the container:
    docker stop <container_id>
    
    Remove the container:
    docker rm <container_id>

Testing API

You can test the API using Postman, cURL, or directly from the browser http://127.0.0.1:8888/docs#/default/production_plan_productionplan_post
Example using cURL:
curl -X 'POST' 'http://127.0.0.1:8888/productionplan' \
-H 'Content-Type: application/json' \
-d @example_payloads/payload1.json

Running Unit tests

pytest tests/

FUTURE IMPROVEMENTS

1.- Support for a database to store generation logs.
2.- Implement performance metrics using Prometheus
3.- Deploy to AWS Lambda or Azure Functions
4.- Refine the calculation algorithm

CONTACT

Author: TOMAS JIMENEZ SANCHEZ
Email: emailtomasjimenez@gmail.com
