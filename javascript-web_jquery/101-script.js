#!/usr/bin/node
// adds, removes and clears LI on click event

$(document).ready(function(){
    $('#add_item').on('click', function(event){
        $('ul.my_list').append('<li>Item</li>');
    });
    $('#remove_item').on('click', function(event){
        $('ul.my_list li:last-child').remove();
    });
    $('#clear_list').on('click', function(event){
        $('ul.my_list').empty();
    });
});
