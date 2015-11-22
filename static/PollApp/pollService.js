app.factory('pollService', ['$resource', function ($resource) {
	var url = '/quickpoll/api/poll/3';

	return $resource(url, { get: { method : 'GET' }});
}])