FROM python:3.9-slim-buster

WORKDIR /app

COPY models/ models/

COPY src/ src/

COPY app.py .

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port 8000 for the application
EXPOSE 8000

# Run the command to start the application
ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
