FROM python:3.8.2


COPY requirements.txt /

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /

CMD ["python", "stream.py"]