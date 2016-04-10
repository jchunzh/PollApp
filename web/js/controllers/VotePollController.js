app.controller('VotePollController', ['$scope', 'pollService', '$location', 'utilityService', '$window', function ($scope, pollService, $location, utilityService, $window) {
	$scope.showResults = false;
	$scope.selectedChoiceMap = [];

	$scope.pollId = utilityService.getPollUniqueId($location.path());
	pollService.get( { uuid: $scope.pollId }, function(data) {
		$scope.poll = data.poll;
		$scope.selectedChoiceMap = createSelectedChoiceMap($scope.poll.choices);
	});
	
	$scope.vote = function() {
		var selectedChoices = getSelectedChoiceIndexes($scope.selectedChoiceMap, $scope.poll.choices);

		pollService.vote({
				id: $scope.poll.uniqueId,
				selectedChoices : selectedChoices
			}, null, function(response) {
				gotoResults($window, $scope.pollId);
			});
	};

	$scope.radioSelectionChanged = function(index) {
		selectNonMultiSelectChoice(index, $scope.selectedChoiceMap);
	}

	$scope.gotoResults = function() {
		gotoResults($window, $scope.pollId);
	}
}]);

function gotoResults($window, pollId) {
	$window.location.href = '/quickpoll/results/' + pollId;
}

function createSelectedChoiceMap(choices) {
	var choiceMap = [];
	for (var i = 0; i < choices.length; i++) {
		if (choices[i].isSelected) {
			choiceMap.push(true);
		}
		else {
			choiceMap.push(false);
		}
	}

	return choiceMap;
}

function selectNonMultiSelectChoice(index, choiceMap) {
	for (var i = 0; i < choiceMap.length; i++) {
		if (i === index) {
			choiceMap[i] = true;
		}
		else {
			choiceMap[i] = false;
		}
	}
}

function getSelectedChoiceIndexes(choiceMap, choices) {
	var choiceIndexes = [];

	for (var i = 0; i < choiceMap.length; i++) {
		if (choiceMap[i]) {
			choiceIndexes.push(choices[i].uniqueId);
		}
	}

	return choiceIndexes;
}