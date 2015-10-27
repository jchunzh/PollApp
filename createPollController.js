app.controller('CreatePollController', ['$scope', 'pollService', function ($scope, pollService) {
	$scope.poll = {
		choices : initializeChoices(),
		question : '',
		useCheckbox : false,
		link : ''
	};

	$scope.hasCreated = false;

	$scope.addChoice = function(index) {
		if (index < ($scope.poll.choices.length - 1))
			return;

		$scope.poll.choices.push(new Choice());
	}

	$scope.createPoll = function() {
		pollService.save($scope.poll, function(link) {
			$scope.hasCreated = true;
			$scope.poll.link = link;
		});
	}
}]);

function initializeChoices() {
	var choices = [];

	for (var i = 0; i < 4; i++) {
		choices.push(new Choice());
	}

	return choices;
}

function Choice(text) {
	this.text = text;
	this.isSelected = false;
	this.votes = 0;
	this.choiceId = 0;
	this.pollId = 0;
}

function Poll() {
	this.choices = [];
	this.question = '';
	this.useCheckbox = false;
	this.guid = '';
	this.link = '';
	ths.pollId = 0;
}