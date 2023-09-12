FROM ubuntu:latest
WORKDIR /app
COPY model model
COPY static static
COPY templates templates
COPY app.py .
COPY CarPrice.py .
RUN apt update
RUN apt install python3 python3-venv -y
RUN python3 -m venv venv
RUN venv/bin/pip install flask scikit-learn
CMD ["venv/bin/python3", "app.py"]
EXPOSE 5000