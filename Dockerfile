FROM alpine:latest
WORKDIR /app
COPY model model
COPY static static
COPY templates templates
COPY app.py .
COPY CarPrice.py .
RUN apk update
RUN apk add py3-flask py3-scikit-learn
CMD ["python", "app.py"]
EXPOSE 5000