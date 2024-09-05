FROM python:3.10

WORKDIR /app

COPY app.py .

COPY template/* .

COPY requirement.txt .


RUN pip install -r requirement.txt

EXPOSE 5000

CMD [ "python3" , "app.py" ]