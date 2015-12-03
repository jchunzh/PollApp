app.controller('CreatePollController', ['$scope', '$timeout', 'pollService', function ($scope, $timeout, pollService) {
	$scope.createPollResponse = new PollResponse();
	$scope.loading_gif = '/static/PollApp/ajax-loader.gif';
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
		$scope.createPollResponse.status = 'loading';
		pollService.save($scope.poll, function(link) {
			$timeout(function() {
				$scope.createPollResponse.status = "created";
			}, 2000)
		});
	}
}]);

function PollResponse() {
	this.status = 'creating';
	this.url = 'http://testurl.com/12345'
}

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