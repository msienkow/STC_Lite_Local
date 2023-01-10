# Dockerfile, Image, Container
FROM python:3-alpine

WORKDIR /stc

RUN apk add --update git

RUN git clone https://github.com/msienkow/STC_Lite_Local.git

RUN cd STC_Lite_Local

RUN pip3 install -r requirements.txt

CMD [ "python", "./endless.py" ] 