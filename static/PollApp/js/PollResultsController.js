app.controller('PollResultsController', ['$scope', 'pollService', 'utilityService', '$location', function($scope, pollService, utilityService, $location) {
	var uniqueId = utilityService.getPollUniqueId($location.path());
	pollService.get( { uuid: uniqueId }, function(data) {
		$scope.poll = data.poll;
		$scope.total = totalVotes($scope.poll.choices);
		addChoicePercentages(data.poll.choices, $scope.total)
		createChart($scope.poll.choices);
	});

}]);

function totalVotes(choices) {
	var total = 0;
	
	for (var i = 0; i < choices.length; i++) {
		total += choices[i].votes;
	}
	
	return total;
}

function addChoicePercentages(choices, total) {
	for (var i = 0; i < choices.length; i++) {
		var choice = choices[i];
		
		choice.percent = Math.round(100 * choice.votes / total) + '%';
	}
}

function createChart(choices) {
	var width = 360;
    var height = 360;
    var radius = Math.min(width, height) / 2;

    var color = d3.scale.category20c();

    var svg = d3.select('#chart')
      .append('svg')
      .attr('width', width)
      .attr('height', height)
      .append('g')
      .attr('transform', 'translate(' + (width / 2) + 
        ',' + (height / 2) + ')');

    var arc = d3.svg.arc()
      .outerRadius(radius);

    var pie = d3.layout.pie()
      .value(function(d) { return d.votes; })
      .sort(null);

    var arcs = svg.selectAll('path')
      .data(pie(choices))
      .enter()
      .append("svg:g")
      .attr("class", "slice");
      
      arcs.append('path')
      .attr('d', arc)
      .attr('fill', function(d, i) {
	      console.log(d);
        return color(d.data.text);
      });
      
      arcs.append("svg:g")
      .attr("class", "slice");

/*
	var path = svg.selectAll('path')
	  .data(pie(choices))
	  .enter()
	  .append('path')
	  .attr('d', arc)
	  .attr('fill', function(d, i) { 
	    return color(d.data.text);
	  });
*/
   	arcs.append("svg:text")                                     //add a label to each slice
    .attr("transform", function(d) {                    //set the label's origin to the center of the arc
	    //we have to make sure to set these before calling arc.centroid
	    d.innerRadius = 0;
	    d.outerRadius = radius;
	    return "translate(" + arc.centroid(d) + ")";        //this gives us a pair of coordinates like [50, 50]
    })
    .attr("text-anchor", "middle")                          //center the text on it's origin
    .text(function(d, i) {
	    if (choices[i].votes <= 0)
	    	return '';
	    
	    return choices[i].text; 
	});      //get the label from our original data array

}