
FROM python:3.10-slim

COPY ./theCooffeeHouse /app/theCooffeeHouse
COPY ./requirements.txt /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "theCooffeeHouse.main_schema:app", "--host=0.0.0.0", "--reload"]