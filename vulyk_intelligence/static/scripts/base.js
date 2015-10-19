$(function() {
	var template = Handlebars.compile($('#intelligence_template').html()),
		output = $("#out");

    $(document.body).on("vulyk.next", function(e, data) {
    	output.html(template(data.result.task.data));

    }).on("vulyk.save", function(e, callback) {
    	callback($('textarea').serializeJSON());
    }).on("vulyk.skip", function(e, callback) {
        callback();
    });
});
