var gulp = require('gulp');
var sass = require('gulp-sass');
var runSequence = require('run-sequence');
var del = require('del');
var watch = require('gulp-watch');

var localDeploymentFolder = 'static/PollApp/';

gulp.task('default', function(callback) {
	runSequence('clean:static', ['sass', 'lib', 'js', 'img', 'watch'], callback);
});

gulp.task('watch', ['clean:static'], function() {
	gulp.watch('web/css/*.scss', ['sass']);
	gulp.watch('web/js/lib/**', ['lib']);
	gulp.watch(['web/js/**/*.js', '!web/js/!lib/', '!web/js/!tests/'], ['js']);
	gulp.watch('web/img/**', ['img']);
})

gulp.task('sass', function() {
	return gulp.src('web/css/*.scss')
	.pipe(sass())
	.pipe(gulp.dest(localDeploymentFolder + 'css'));
});

gulp.task('lib', function() {
	return gulp.src('web/js/lib/**/*.min.js')
	.pipe(gulp.dest(localDeploymentFolder + 'js/lib'));
});

gulp.task('js', function() {
	return gulp.src(['web/js/**/*.js', '!web/js/lib/**', '!web/js/tests/**', ])
	.pipe(gulp.dest(localDeploymentFolder + 'js'));
});

gulp.task('img', function() {
	return gulp.src('web/img/**')
	.pipe(gulp.dest(localDeploymentFolder + 'img'));
});

gulp.task('clean:static', function() {
	return del.sync(localDeploymentFolder);
});