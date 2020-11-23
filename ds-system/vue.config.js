module.exports = {
    indexPath: 'index.html',//html 的输出路
    runtimeCompiler: false,
    publicPath: './',
    outputDir: 'dist',
    // 放置静态资源的地方 (js/css/img/font/...)
    assetsDir: 'static',
    //以多页模式构建应用程序。
    pages: undefined,
    //是否使用包含运行时编译器的 Vue 构建版本
    parallel: require('os').cpus().length > 1,
    // 是否为生产环境构建生成 source map？
    productionSourceMap: false,
    transpileDependencies: [],//babel-loader 默认会跳过 node_modules 依赖。
    

}