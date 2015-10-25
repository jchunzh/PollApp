describe('PollController', function() {
	var ctrl;
	var scope;

	beforeEach(module('pollApp'));
	beforeEach(inject(function($controller) {
		scope = {};
		ctrl = $controller('PollController', {$scope:scope});
	}));

	it('initializes with 4 choices', function() {
		expect(scope.choices.length).toBe(4);
	});

	it('adds a new choice when using last choice index', function() {
		var initialLength = scope.choices.length;
		scope.addChoice(initialLength - 1);
		var newLength = scope.choices.length;

		expect(newLength).toBe(initialLength + 1);
		expect(scope.choices[newLength - 1].text).toBe(undefined);
	})

	it('does not add a new choice when the last choice is not the index', function() {
		var initialLength = scope.choices.length;
		scope.addChoice(initialLength - 2);
		var newLength = scope.choices.length;

		expect(newLength).toBe(initialLength);
	})
})