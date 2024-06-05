FROM python:3.11

WORKDIR /word_dir

ADD main.py .

CMD ["python", "./main.py"]