From python:3-slim-stretch
WORKDIR /rsplatform/services
COPY . /orchestrator
RUN pip install --trusted-host pypi.python.org -r /orchestrator/requirment.txt
EXPOSE 80
ENV NAME orchestrator
CMD ["python", "/orchestrator/app.py"]
