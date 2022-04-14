const request = $.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json'
});

request.done(function (body) {
    $('DIV#character').append('<p>' + body.name + '</p>');
});
