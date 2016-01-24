var app = angular.module('pollApp', ['ngResource'], function($locationProvider) {
	$locationProvider.html5Mode({
		enabled: true,
		requireBase: false
		});
});
