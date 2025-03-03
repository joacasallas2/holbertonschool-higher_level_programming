#!/usr/bin/node
/*  fetches from https://hellosalut.stefanbohacek.dev/?lang=fr
// and displays the value of hello */
$(function(){
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        method: 'get',
        success: function(data) {
            $('#hello').text(data.hello);
        },
        error: function(err) {
            console.log(err);
        },
    });
});
