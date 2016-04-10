describe('CreatePollController Tests', function() {
	var ctrl;
	var scope;
	var mockPollService;

	// beforeEach(module('app'));	

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
})