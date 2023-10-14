FROM python
WORKDIR /app1
COPY . /app1
CMD ["python","app1.py"]