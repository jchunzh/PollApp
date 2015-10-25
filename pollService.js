app.factory('pollService', ['$resource', function ($resource) {
	return {
		save : function(poll, callback) {
			var link = "test url";
			callback(link);
		}
	}
}])