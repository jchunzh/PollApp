app.factory('pollService', ['$resource', function ($resource) {
	var url = '/quickpoll/api/poll/';

	return $resource(url, null, { 
		get : { method : 'GET', url : url + ':id' },
		vote : { method : 'POST', url : url + ':id/vote_choice/'}
	}, {
		stripTrailingSlashes : false
	});
}])