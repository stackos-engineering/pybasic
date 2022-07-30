FROM python:3.9.13

RUN mkdir /app
WORKDIR /app


COPY ./app /app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "example.py" ]
