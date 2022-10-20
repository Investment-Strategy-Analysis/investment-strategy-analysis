FROM node:16-alpine

WORKDIR /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . .
RUN npm install

EXPOSE 5001

ENTRYPOINT ["/entrypoint.sh"]

#CMD npm run build
#CMD npm run serve
CMD ["npm", "run", "dev"]
