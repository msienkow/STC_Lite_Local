# Dockerfile, Image, Container
FROM python:3-alpine

WORKDIR /stc

# ADD stc_lite.py .

# ADD stc_logging.py .

# ADD stc_lite_mysql.py .

# ADD requirements.txt .

ADD endless.py .

RUN pip install -r requirements.txt



CMD [ "python", "./endless.py" ] 