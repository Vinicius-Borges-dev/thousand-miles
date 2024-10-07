FROM python:3.9

WORKDIR /app

RUN python -m venv venv

COPY requirements.txt .
RUN . venv/bin/activate && pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["/bin/bash", "-c", "source venv/bin/activate && python app.py"]
