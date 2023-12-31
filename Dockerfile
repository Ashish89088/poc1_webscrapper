FROM python:3.8-slim-buster

WORKDIR /<change accordingly>

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=127.0.0.1:5000"]

