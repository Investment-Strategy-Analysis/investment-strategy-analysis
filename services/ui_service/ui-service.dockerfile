FROM node:16-alpine

WORKDIR /app

COPY package.json package-lock.json ./services/ui_service/

RUN npm install

COPY . services/ui_service/

EXPOSE 3000

#CMD npm run build
#CMD npm run serve
CMD npm start
