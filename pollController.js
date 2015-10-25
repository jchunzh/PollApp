var app = angular.module('pollApp', []);

app.controller('PollController', function ($scope) {
	$scope.title;
	$scope.choices = initializeChoices();

	$scope.addChoice = function(index) {
		if (index < ($scope.choices.length - 1))
			return;

		$scope.choices.push(new Choice());
	}
});

function initializeChoices() {
	var choices = [];

	for (var i = 0; i < 4; i++) {
		choices.push(new Choice());
	}

	return choices;
}

function Choice(text) {
	this.text = text;
}