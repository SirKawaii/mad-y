FROM python:3.9.1

WORKDIR /mad-y

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/ .

CMD [ "python", "./miyu.py"]
