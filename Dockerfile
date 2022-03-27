FROM python:latest
WORKDIR https://github.com/Rmap91/WOG
COPY . /app
#RUN apt-get install -y python3
RUN apt-get update && apt-get install -y python3-pip
RUN pip3 install selenium
RUN pip3 install flask
RUN pip3 install webdriver-manager
RUN pip3 install currencyconverter
CMD ["python3", "e2e.py"]
