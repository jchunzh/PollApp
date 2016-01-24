var gulp = require('gulp');
var sass = require('gulp-sass')
var runSequence = require('run-sequence');
var del = require('del');

gulp.task('default', function(callback) {
	runSequence('clean:static', ['sass', 'lib', 'js', 'img', 'watch'], callback);
});

gulp.task('watch', ['clean:static'], function() {
	gulp.watch('web/css/*.scss', ['sass']);
	gulp.watch('web/js/bower_components/**', ['lib']);
	gulp.watch(['web/js/**/*.js', '!web/js/!bower_components/', '!web/js/!tests/'], ['js']);
	gulp.watch('web/img/**', ['img']);
})

gulp.task('sass', function() {
	return gulp.src('web/css/*.scss')
	.pipe(sass())
	.pipe(gulp.dest('static/PollApp/css'));
});

gulp.task('lib', function() {
	return gulp.src('web/js/bower_components/**/*.min.js')
	.pipe(gulp.dest('static/PollApp/lib/'));
});

gulp.task('js', function() {
	return gulp.src(['web/js/**/*.js', '!web/js/bower_components/**', '!web/js/tests/**', ])
	.pipe(gulp.dest('static/PollApp/'));
});

gulp.task('img', function() {
	return gulp.src('web/img/**')
	.pipe(gulp.dest('static/PollApp/'));
});

gulp.task('clean:static', function() {
	return del.sync('static/PollApp/');
})