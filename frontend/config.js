// see http://vuejs-templates.github.io/webpack for documentation.
var path = require('path')

module.exports = {
  build: {
    index: path.resolve(__dirname, '../fengyuan/templates/index.html'),
    assetsRoot: path.resolve(__dirname, '../fengyuan/static'),
    assetsSubDirectory: '/',
    assetsPublicPath: '/',
    productionSourceMap: true
  },
  dev: {
    port: 8080,
    proxyTable: {}
  }
}
