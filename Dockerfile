FROM python:3.9.6

COPY requirements.txt .

RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir -Ur requirements.txt

COPY . .

CMD ["python", "bot.py"]
