FROM python:3.11.3-slim

WORKDIR /root/
EXPOSE 8080

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY lib.py .

ENTRYPOINT ["python"]
CMD ["lib.py"]
