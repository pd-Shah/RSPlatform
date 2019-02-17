# api provider Service
this service is an interface between `admin interface` and `user interface` with any deeper part of back-end.
deeper parts like, `algorithm services` and `data base`.

in order to run this docker first install docker from [here](https://docs.docker.com/install/), then run as below:

```bash
sudo docker run -p 8080:5000 apiprovicer:test
```

in order to run `flask` project run:
```bash
pd@localhost: FLASK_APP=engine 
pd@localhost: export FLASK_ENV=development  
pd@localhost: flask run 
```