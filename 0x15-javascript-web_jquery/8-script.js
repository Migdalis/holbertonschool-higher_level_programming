const request = $.ajax({
    url: 'https://swapi-api.hbtn.io/api/films/?format=json'
});

request.done(function (body) {
    for (const film of body.results) {
        $('UL#list_movies').append('<li>' + film.title + '</li>');
    }
});
