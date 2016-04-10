app.factory('utilityService', function(){
	return {
		getPollUniqueId: function(url) {
			var parts = url.split("/");
			var id = parts[parts.length - 1];
			return id;
		}
	};
});