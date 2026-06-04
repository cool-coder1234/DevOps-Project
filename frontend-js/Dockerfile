FROM node:20-alpine AS build
WORKDIR /app
COPY apps/react-vite/package*.json ./
RUN npm install --legacy-peer-deps
COPY apps/react-vite/ .
RUN echo -e "VITE_APP_API_URL=http://localhost:5000\nVITE_APP_ENABLE_API_MOCKING=false" > .env
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]