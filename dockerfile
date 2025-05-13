
#Docker file
FROM python:3.11

WORKDIR /app


COPY ProyectoPython.py /app/ProyectoPython.py

CMD ["python", "ProyectoPython.py"]