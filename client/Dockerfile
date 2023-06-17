FROM python:3.11:slim
WORKDIR /app
COPY ./app.py  /app/app.py
COPY ./requirements.txt ./app/requirements.txt
RUN pip install -r requirements.txt
CMD [ "python", "app.py" ]