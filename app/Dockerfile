# ВНИМАНИЕ: базовый образ устарел специально — на занятии Trivy покажет,
# чем это грозит, и мы починим его вместе с преподавателем (занятие 1, шаг 4).
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG APP_VERSION=dev
ENV APP_VERSION=${APP_VERSION}

EXPOSE 8000
CMD ["python", "-m", "flask", "--app", "app", "run", "--host", "0.0.0.0", "--port", "8000"]
