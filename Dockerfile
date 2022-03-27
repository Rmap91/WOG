FROM python:3
WORKDIR /app
COPY . /app
RUN apt-get update -y
#RUN apt-get install -y python3
RUN sudo apt-get install -y python3-pip
RUN pip install selenium
RUN pip install flask
RUN pip install webdriver-manager
RUN pip install currencyconverter
