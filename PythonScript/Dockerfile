FROM python:3.11-buster

WORKDIR /src

RUN pip install psycopg2

COPY db_script.py ./

CMD ["python", "db_script.py"]