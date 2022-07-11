FROM debian:latest

RUN apt-get update && apt-get install python3-pip -y && pip3 install requests

ADD test_model3.py /test_model3/test_model3.py

WORKDIR /test_model3/


VOLUME ["/home/"]

#ENV LOG=/1

CMD python3 test_model3.py
