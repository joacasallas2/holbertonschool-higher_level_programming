#!/usr/bin/node
/* fetches and lists the title for all movies by using this URL:
https://swapi-api.hbtn.io/api/films/?format=json */
$(function(){
    $.ajax({
        url: 'https://swapi-api.hbtn.io/api/films/?format=json',
        method: 'get',
        success: function(data){
            for (movie of data.results) {
                $('#list_movies').append(`<li>${movie.title}</li>`)
            }
        },
        error: function(err){
            console.log (err);
        },
    });
});
