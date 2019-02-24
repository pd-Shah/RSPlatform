FROM node:9.6.1
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app/
RUN npm install
RUN npm install react-scripts@1.1.1 -g
CMD npm start
