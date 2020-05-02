FROM python:3

WORKDIR /app

COPY templates/ ./templates
COPY main.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP "main.py"
# ENV FLASK_ENV "development"

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0"]