FROM python:3
WORKDIR /pythonProject

ADD app.py /
COPY . .

RUN pip install -r requirements.txt


CMD [ "python", "./app.py" ]