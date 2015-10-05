var del = require('del'),
  express = require('express'),
  execSync = require('child_process').execSync
  gulp = require('gulp'),
  livereload = require('connect-livereload'),
  lrserver = require('tiny-lr')(),
  path = require('path'),
  $ = require('gulp-load-plugins')();

var config = {
  livereloadPort: 35728,
  serverPort: 8080
};

var server = express();
server.use(livereload({
  port: config.livereloadPort
}));
server.use(express.static('./build'));


gulp.task('clean', function(){
  return del(['build']);
});


gulp.task('build', ['clean'], function(){
  execSync('sphinx-build docs build');
  $.livereload(lrserver);
});


gulp.task('serve', function(){
  server.listen(config.serverPort);
  lrserver.listen(config.livereloadPort);
});


gulp.task('watch', function(){
  var tasks = ['clean', 'build'];
  gulp.watch('./_static/**/*', tasks);
  gulp.watch('./_templates/**/*', tasks);
  gulp.watch('./docs/**/*', tasks);
  gulp.watch('./granite/**/*', tasks);
  gulp.watch('./gulpfile.js', tasks);
});


gulp.task('default', ['build', 'serve', 'watch']);
