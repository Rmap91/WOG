FROM python:latest
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y python-pip
#RUN apt-get install -y python3
#RUN sudo apt-get install -y py3-pip
RUN pip install selenium
RUN pip install flask
RUN pip install webdriver-manager
RUN pip install currencyconverter
