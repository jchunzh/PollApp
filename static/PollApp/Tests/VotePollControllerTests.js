describe('VotePollController Tests', function() {
	var ctrl;
	var scope;
	var mockPollService;

	beforeEach(module('pollApp', function($provide) {
		mockPollService = {
			save : jasmine.createSpy('save'),
			get : function (id, paramDefaults, callback) {
				callback(getCheckboxStubPollData());
			},
			vote : jasmine.createSpy('saveVotes')
		}
		$provide.value("pollService", mockPollService);
	}));

	beforeEach(inject(function($controller) {
		scope = {};
		ctrl = $controller('VotePollController', {$scope:scope});
	}));

	it('sends choices when voting', function() {
		var data = getCheckboxStubPollData();
		var choices = {
			hasVoted : true,
			selected : [data.choices[0], data.choices[2]]
		};

		var params = {
			id: 123
		}
		scope.vote();

		expect(mockPollService.vote).toHaveBeenCalledWith(params, null, jasmine.any(Function));
	})

	function getCheckboxStubPollData() {
		return {
			id : 123,
			choices : [
				{
					text : 'Choice 1',
					isSelected : true,
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
					isSelected : true,
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