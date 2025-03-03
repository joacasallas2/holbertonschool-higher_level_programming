#!/usr/bin/node
// append <li> element to list
$('#add_item').on('click', function(event){
    $('ul.my_list').append('<li>Item</li>');
});
