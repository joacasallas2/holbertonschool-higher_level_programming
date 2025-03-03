#!/usr/bin/node
/* fetches the character name from this URL:
https://swapi-api.hbtn.io/api/people/5/?format=json */

$(function(){
    $.ajax({
        url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
        method: 'get',
        success: function(data) {
            console.log(data.name);
            $('#character').text(data.name);
        },
        error: function(err) {
            console.log(err);
        },
    })
});
