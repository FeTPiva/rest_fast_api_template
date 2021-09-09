FROM python:3.7

RUN pip install fastapi uvicorn

EXPOSE 80

COPY ./app /app
COPY ./requirements.txt /app/

RUN pip install -r /app/requirements.txt

CMD ["uvicorn", "credit_score.main:app", "--host", "0.0.0.0", "--port", "8000"]
