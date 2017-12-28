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
        test: /\.(png|jpg|jpeg|ttf)$/,
        use: [
         { loader: 'url-loader', options: { limit: 8192 } }
         // limit => file.size =< 8192 bytes ? DataURI : File
        ]
      },
      {
        test: /\.(js|jsx)$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader',
      },
      {
        test: /\.(scss|sass)$/,
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
