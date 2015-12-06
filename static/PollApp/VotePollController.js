app.controller('VotePollController', ['$scope', 'pollService', function ($scope, pollService) {
	$scope.showResults = false;
	$scope.selectedChoiceMap = [];

	pollService.get( { id: 3 }, null, function(data) {
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

// function createChart(poll) {
// 	var width = 540;
// 	var height = 500;

// 	var y = d3.scale.linear()
// 		.range([height, 0])
// 		.domain([0, d3.max(poll.choices, function(choice) { return choice.votes; })]);

//     var chart = d3.select(".chart")
//     	.attr("width", width)
// 		.attr("height", height);

// 	//move bar to correct position
// 	var barWidth = width / poll.choices.length;

// 	var bar = chart.selectAll("g")
// 		.data(poll.choices)
// 		.enter()
// 		.append("g")
// 		.attr("transform", function(choice, i) { return "translate(" + i * barWidth + ",0)";});

// 	bar.append("rect")
// 		.attr("y", function(choice) { return y(choice.votes); })
// 		.attr("width", barWidth - 1)
// 		.attr("height", function(choice) { return height - y(choice.votes); });

// 	bar.append("text")
// 		.attr("x", barWidth / 2)
// 		.attr("y", function(choice) { return y(choice.votes) + 3; })
// 		.attr("dy", ".75em")
// 		.text(function(choice) { return choice.votes; });
// }