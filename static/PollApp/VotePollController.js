app.controller('VotePollController', ['$scope', 'pollService', function ($scope, pollService) {
	$scope.showResults = false;
	$scope.selectedChoice = {};

	pollService.get('guid', function(data) {
		$scope.poll = data;

		if (!data.isMultiSelect) {
			$scope.selectedChoice.index = getSelectedChoiceIndex($scope.poll);
		}
		// createChart($scope.poll);
	});
	$scope.vote = function() {
		pollService.vote(getSelectedChoices($scope.poll), function(response) {
			$scope.hasVoted = true;
			$scope.selected = getSelectedChoices($scope.poll);
		});
	}

	$scope.toggleShowResults = function() {
		$scope.showResults = !$scope.showResults;
	}
}]);

function getSelectedChoices(poll) {
	var selectedChoices = [];

	for (var i = 0; i < poll.choices.length; i++) {
		if (poll.choices[i].isSelected)
			selectedChoices.push(poll.choices[i]);
	}

	return selectedChoices;
}

function getSelectedChoiceIndex (poll) {
	for (var i = 0; i < poll.choices.length; i++) {
		if (poll.choices[i].isSelected)
			return i;
	}
	return 0;
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