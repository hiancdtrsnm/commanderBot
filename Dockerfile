FROM python:3.6


RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt requirements.txt
#RUN python -m venv venv
RUN pip install -r requirements.txt

RUN pip install path.py
COPY . /app

# run-time configuration
# EXPOSE 5000
CMD ["python commanderBot.py"]
