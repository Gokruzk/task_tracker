# --- Stage 1: Build ---
FROM node:20-alpine AS build-stage

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install

COPY . .

ARG VITE_API_BASE_URL
ENV VITE_API_BASE_URL=$VITE_API_BASE_URL

RUN yarn build

# --- Stage 2: Production ---
FROM nginx:stable-alpine AS production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]