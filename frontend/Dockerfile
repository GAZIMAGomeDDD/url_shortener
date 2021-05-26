FROM node:14-buster-slim

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY ./package.json /app
RUN npm install

COPY . .
