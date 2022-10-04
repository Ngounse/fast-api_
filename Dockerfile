ARG PYTHON_VERSION=3.10-slim-bullseye

# define an alias for the specfic python version used in this file.
FROM python:${PYTHON_VERSION} as python

WORKDIR /app

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y

COPY ./requirements.txt /app

RUN pip3 install -r requirements.txt

COPY ./theCooffeeHouse /app/theCooffeeHouse

EXPOSE 8000

CMD ["uvicorn", "theCooffeeHouse.main_schema:app", "--host=0.0.0.0", "--reload"]