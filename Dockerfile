FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install flask

EXPOSE 8000
ENV ASPNETCORE_URLS=http://+:8000


COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000"]