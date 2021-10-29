FROM node:17

WORKDIR /mady

COPY app/package*.json ./

CMD npm install

COPY app/. .

CMD [ "node", "index.js"]