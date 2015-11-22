describe('VotePollController Tests', function() {
	var ctrl;
	var scope;
	var mockPollService;

	beforeEach(moduel('app'));

	beforeEach(module('pollApp', function($provide) {
		mockPollService = {
			save : jasmine.createSpy('save'),
			get : function (guid, callback) {
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
		var choices = [data.poll.choices[0], data.poll.choices[2]];
		scope.vote();

		expect(mockPollService.vote).toHaveBeenCalledWith(choices, jasmine.any(Function));
	})

	function getCheckboxStubPollData() {
		return {
			message : {

			},
			poll : {
				pollId : 123,
				choices : [
					{
						text : 'Choice 1',
						isSelected : true,
						votes : 10,
						choiceId : 1,
						pollId : 123
					},
					{
						text : 'Choice 2',
						isSelected : false,
						votes: 1,
						choiceId : 2,
						pollId : 123
					},
					{
						text : 'Choice 3',
						isSelected : true,
						votes : 18,
						choiceId : 3,
						pollId : 123
					},
					{
						text : 'Choice 4',
						isSelected : false,
						votes : 5,
						choiceId : 4,
						pollId : 123
					}
				],
				question : 'Test question',
				useCheckbox: true,
			}
		};	
	}
})