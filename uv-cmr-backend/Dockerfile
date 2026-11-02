# Usamos una imagen base ligera de Python
FROM python:3.12-slim

# Variables de entorno para Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo en el contenedor
WORKDIR /app

# Instalar uv directamente (requisito de la EFI)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copiar el archivo de dependencias
COPY requirements.txt .

# Instalar las dependencias usando uv
RUN uv pip install --system -r requirements.txt

# Copiar todo el código del proyecto
COPY . .

# Exponer el puerto
EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]