# if you want to run this image alone, with out docker-compose
# then uncomment commented line

From python:3-slim-stretch
# WORKDIR /rsplatform/APIProvider
# COPY . /APIProvider
RUN pip install --trusted-host pypi.python.org -r /APIProvider/requirment.txt
# CMD ["python", "/APIProvider/app.py"]
