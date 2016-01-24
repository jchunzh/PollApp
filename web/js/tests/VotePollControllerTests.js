describe('VotePollController Tests', function() {
	var ctrl;
	var scope;
	var mockPollService;
	var poll = {};

	beforeEach(module('pollApp', function($provide) {
		poll = getStubPollData();
		mockPollService = {
			save : jasmine.createSpy('save'),
			get : function (id, callback) {
				callback(poll);
			},
			vote : jasmine.createSpy('saveVotes')
		}
		$provide.value("pollService", mockPollService);
	}));

	beforeEach(inject(function($controller) {
		scope = {};
		ctrl = $controller('VotePollController', {$scope:scope});
	}));

	it('sends all choices when voting a multiselect poll', function() {
		var pollId = 123;
		poll.isMultiSelect = true;

		selectPollData([0, 2], scope.selectedChoiceMap);

		poll.id = pollId;

		var params = {
			id: pollId,
			selectedChoices: [poll.choices[0].id, poll.choices[2].id]
		}
		scope.vote();

		expect(mockPollService.vote).toHaveBeenCalledWith(params, null, jasmine.any(Function));
	});

	it('sends single choice when voting nonmultiselect poll', function () {
		var pollId = 123;
		poll.isMultiSelect = false;

		selectPollData([0], scope.selectedChoiceMap);
		poll.id = pollId;

		var params = {
			id: pollId,
			selectedChoices: [poll.choices[0].id]
		};
		scope.vote();

		expect(mockPollService.vote).toHaveBeenCalledWith(params, null, jasmine.any(Function));
	});

	function selectPollData(choiceIndexes, choiceMap) {
		for (var i = 0; i < choiceIndexes.length; i++) {
			choiceMap[choiceIndexes[i]] = true;
		}
	}

	function getStubPollData() {
		return {
			id : 123,
			choices : [
				{
					text : 'Choice 1',
					isSelected : false,
					votes : 10,
					id : 1,
					pollId : 123,
				},
				{
					text : 'Choice 2',
					isSelected : false,
					votes: 1,
					id : 2,
					pollId : 123,
				},
				{
					text : 'Choice 3',
					isSelected : false,
					votes : 18,
					id : 3,
					pollId : 123
				},
				{
					text : 'Choice 4',
					isSelected : false,
					votes : 5,
					id : 4,
					pollId : 123
				}
			],
			question : 'Test question',
			useCheckbox: true,
			isMultiSelect : true
		};	
	}
})