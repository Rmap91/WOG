FROM ubuntu:20.04
WORKDIR /app
COPY . /app
#RUN apt-get install -y python3
RUN apt-get update && apt-get install -y python3-pip
RUN pip install selenium
RUN pip install flask
RUN pip install webdriver-manager
RUN pip install currencyconverter
