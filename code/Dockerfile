FROM python:3.9-alpine

WORKDIR /app

COPY calc/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY calc . 

CMD cat /app/math_calc.py