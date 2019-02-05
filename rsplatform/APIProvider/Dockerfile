From python:3-slim-stretch
WORKDIR /rsplatform/APIProvider
COPY . /APIProvider
RUN pip install --trusted-host pypi.python.org -r /APIProvider/requirment.txt
CMD ["python", "/APIProvider/app.py"]
