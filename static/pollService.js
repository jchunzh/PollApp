app.factory('pollService', ['$resource', function ($resource) {
	return {
		save : function(poll, callback) {
			var link = "test url";
			callback(link);
		},
		vote : function(votes, callback) {
			callback(
			{
				success : true,
				message : ''
			});
		},
		get : function(guid, callback) {
			callback(
			{
				message : {

				},
				poll : {
					choices : [
						{
							text : 'Choice 1',
							isSelected : false,
							votes : 10
						},
						{
							text : 'Choice 2',
							isSelected : false,
							votes: 1
						},
						{
							text : 'Choice 3',
							isSelected : true,
							votes : 18
						},
						{
							text : 'Choice 4',
							isSelected : false,
							votes : 5
						}
					],
					question : 'Test question',
					useCheckbox: true,
				}
			});
		}
	}
}])