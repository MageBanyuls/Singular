FROM apache/airflow:latest-python3.10


USER root

ENV PYTHONPATH=/opt/airflow

RUN apt-get update && \
    apt-get -y install git && \
    apt-get clean


USER airflow

COPY requirements.txt /requirements.txt
RUN pip install matplotlib
RUN pip install pandas
RUN pip install seaborn