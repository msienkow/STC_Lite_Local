# Dockerfile, Image, Container
FROM python:3.11

WORKDIR /stc

ADD stc_lite.py .

ADD stc_logging.py .

ADD stc_lite_mysql.py .

ADD requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "./stc_lite_mysql.py" ] 