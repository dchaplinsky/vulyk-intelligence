$(function() {
    var template = Handlebars.compile($('#intelligence_template').html()),
        output = $("#out");

    $(document.body).on("vulyk.next", function(e, data) {
        output.html(template(data.result.task.data));       
    }).on("vulyk.save", function(e, callback) {
        callback($('textarea, input[type=checkbox]').serializeJSON());
        $("html, body").animate({ scrollTop: 0 }, "slow");
    }).on("vulyk.skip", function(e, callback) {
        callback();
        $("html, body").animate({ scrollTop: 0 }, "slow");
    });
});
