FROM node:16-alpine

WORKDIR /app

COPY package.json .
COPY package-lock.json .

RUN npm install

COPY . services/ui_service/

EXPOSE 5173

#CMD npm run build
#CMD npm run serve
CMD npm run dev
