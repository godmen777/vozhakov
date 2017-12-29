var path = require('path')
var ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  entry: './index.js',
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader',
      },
      {
        test: /\.scss$/,
        use: ExtractTextPlugin.extract({
          // use: ['css-loader?modules&importLoaders=1&localIdentName=[name]__[local]', 'sass-loader']
          use: ['css-loader', 'sass-loader']
        })
      },
    ]
  },
  plugins: [
    new ExtractTextPlugin("styles.css", { allChunks: true }),
  ]
};
