FROM debian:latest

RUN apt-get update && apt-get install python3-pip -y && pip3 install requests

ADD ML_API.py /server/ML_API.py

ADD log_newton_model.pkl /server/log_newton_model.pkl

ADD log_liblinear_model.pkl /server/log_liblinear_model.pkl

ADD knc_model.pkl /server/knc_model.pkl

ADD requirements.txt /server/requirements.txt

RUN pip3 install -r /server/requirements.txt

WORKDIR /server/

EXPOSE 5000

CMD python3 ML_API.py