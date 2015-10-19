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
    }).on("vulyk.task_error", function(e, data) {
        $.magnificPopup.open({
            items: {
                src: '<div class="zoom-anim-dialog small-dialog">' +
                '<div class="dialog-content">Нажаль, увесь пакет завдань був виконаний, але дуже скоро ми додамо нові.</div>' +
                '</div>',
                type: 'inline'
            }
        })
    });
});
