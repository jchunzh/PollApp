app.controller('VotePollController', ['$scope', 'pollService', function ($scope, pollService) {
	$scope.showResults = false;
	$scope.selectedChoiceMap = [];

	pollService.get( { id: 3 }, function(data) {
		$scope.poll = data;
		$scope.selectedChoiceMap = createSelectedChoiceMap(data.choices);
	});
	
	$scope.vote = function() {
		var selectedChoices = getSelectedChoiceIndexes($scope.selectedChoiceMap, $scope.poll.choices);

		pollService.vote({
				id: $scope.poll.id,
				selectedChoices : selectedChoices
			}, null, function(response) {
			});
	};

	$scope.radioSelectionChanged = function(index) {
		selectNonMultiSelectChoice(index, $scope.selectedChoiceMap);
	}

	$scope.toggleShowResults = function() {
		$scope.showResults = !$scope.showResults;
	}
}]);

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
			choiceIndexes.push(choices[i].id);
		}
	}

	return choiceIndexes;
}