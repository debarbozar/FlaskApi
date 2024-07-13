FROM python:3.10.14-alpine3.20

#porta padrão do flask
EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

CMD [ "python", "app.py"]