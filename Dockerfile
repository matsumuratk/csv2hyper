FROM python:slim

WORKDIR /app
COPY ./app /app
RUN pip install --upgrade pip
RUN python -m pip install flask tableauhyperapi pandas pantab chardet jinja2


CMD ["python", "main.py"]

#  docker image build -t csv2hyper .
#  docker run -dit -p 8080:8080 --name csv2hyper_container -d csv2hyper