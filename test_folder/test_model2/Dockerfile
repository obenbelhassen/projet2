FROM debian:latest

RUN apt-get update && apt-get install python3-pip -y && pip3 install requests

ADD test_model2.py /test_model2/test_model2.py

WORKDIR /test_model2/


VOLUME ["/home/"]

#ENV LOG=/1

CMD python3 test_model2.py
