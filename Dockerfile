FROM python:3
COPY account_generation_project /Account-Generator
COPY requirements.txt /
RUN pip install -r requirements.txt
EXPOSE 5000/tcp
CMD ["python", "Account-Generator/main.py"]
