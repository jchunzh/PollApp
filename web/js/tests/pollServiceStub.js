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
							text : 'Pizza',
							isSelected : false,
							votes : 10
						},
						{
							text : 'Fries',
							isSelected : false,
							votes: 1
						},
						{
							text : 'Kale',
							isSelected : true,
							votes : 18
						},
						{
							text : 'Chocolate',
							isSelected : false,
							votes : 5
						}
					],
					question : 'What\'s your favorite food?',
					isMultiSelect: true,
				}
			});
		}
	}
}])