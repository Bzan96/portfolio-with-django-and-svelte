# syntax=docker/dockerfile:1
FROM node:14-alpine

WORKDIR /frontend

# install dependencies
COPY package.json package-lock.json ./

RUN npm ci

# Copy all local files into the image.
COPY . .

RUN npm run build

###
# Only copy over the Node pieces we need
# ~> Saves 35MB
###
FROM node:14-alpine

WORKDIR /frontend

COPY --from=0 /frontend .
COPY . .

EXPOSE 3000
# EXPOSE 24678