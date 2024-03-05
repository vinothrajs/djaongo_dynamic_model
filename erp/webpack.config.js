const path = require('path');

module.exports = {
    // entry: './sample/assets/scripts/index.js',
    // output: {
    //     'path': path.resolve(__dirname, 'sample', 'static'),
    //     'filename': 'index.js'
    // }

    entry: {
        index: "./sample/assets/scripts/index.js",
        home: "./sample/assets/scripts/home.js",
    },
    output: {
        'path': path.resolve(__dirname, 'sample', 'static'),
        filename: "scripts/[name].min.js"
    },
}