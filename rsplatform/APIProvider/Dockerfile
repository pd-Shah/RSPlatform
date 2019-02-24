# if you want to run this image alone, with out docker-compose
# then uncomment commented line

From python:3-slim-stretch
# RUN echo "curdir: " $PWD
ADD . /rsplatform/APIProvider
WORKDIR /rsplatform/APIProvider
# COPY . /APIProvider
RUN pip install --trusted-host pypi.python.org -r requirment.txt
ENV FLASK_APP=engine
ENV FLASK_ENV=development
CMD flask run -h "0.0.0.0"
# CMD ["python", "./app.py"]
