const request = $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr'
});

request.done(function (body) {
    $('DIV#hello').append('<p>' + body.hello + '</p>');
});
