FROM python:3

RUN apt update && apt upgrade

RUN apt install -y tesseract-ocr tesseract-ocr-deu

WORKDIR /usr/ocr_service

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
