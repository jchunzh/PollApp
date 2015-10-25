describe('CreatePollController Tests', function() {
	var ctrl;
	var scope;
	var mockPollService;

	beforeEach(module('pollApp', function($provide) {
		mockPollService = {
			save : jasmine.createSpy('save')
		}
		$provide.value("pollService", mockPollService);
	}));

	beforeEach(inject(function($controller) {
		scope = {};
		ctrl = $controller('CreatePollController', {$scope:scope});
	}));

	it('initializes with 4 choices', function() {
		expect(scope.poll.choices.length).toBe(4);
	});

	it('adds a new choice when using last choice index', function() {
		var initialLength = scope.poll.choices.length;
		scope.addChoice(initialLength - 1);
		var newLength = scope.poll.choices.length;

		expect(newLength).toBe(initialLength + 1);
		expect(scope.poll.choices[newLength - 1].text).toBe(undefined);
	})

	it('does not add a new choice when the last choice is not the index', function() {
		var initialLength = scope.poll.choices.length;
		scope.addChoice(initialLength - 2);
		var newLength = scope.poll.choices.length;

		expect(newLength).toBe(initialLength);
	})

	it('saves via poll service when creating a poll', function() {
		scope.createPoll();

		expect(mockPollService.save).toHaveBeenCalled();
	})

	it('saves via current poll data when saving a poll', function() {
		scope.createPoll();

		expect(mockPollService.save).toHaveBeenCalledWith(scope.poll, jasmine.any(Function));
	})
})