# Feng Yuan Files App Frontend

## `index.html`

`index.html` in this directory is only used for `npm run dev` to test a single app. It is **not** a Django template, Feng Yuan has its own Django template that will render the nav bar, only the app part is handled by Vue.

When you run `npm run dev` you will only see a single app. Each app is developed and tested separately.

## static/

`static/` directory is needed for build, should change `build/build.js` to fix this later. TODO

> A Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

For detailed explanation on how things work, checkout the [guide](https://github.com/vuejs-templates/webpack#vue-webpack-boilerplate) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
