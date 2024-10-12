FROM python:3.9-alpine3.13

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copiar los archivos de requerimientos primero
COPY requirements.txt .

# Instalar dependencias
RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apk add --no-cache postgresql-client

# Copiar el resto de los archivos del proyecto
COPY . .


# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
