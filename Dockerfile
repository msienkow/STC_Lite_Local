# Dockerfile, Image, Container
FROM python:3.11

WORKDIR /stc

ADD test.py .

ADD requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "./test.py" ] 