FROM python:3.9

WORKDIR /fastapi/

ADD requirements.txt .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000
CMD ["bash", "-c",  "uvicorn main:app --reload --host 0.0.0.0 --port 80"]