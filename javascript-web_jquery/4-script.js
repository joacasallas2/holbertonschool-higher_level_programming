#!/usr/bin/node
// Toggle classes
$("#toggle_header").on("click", function (event) {
  if ($("#toggle_header").hasClass("red"))
    $("#toggle_header").removeClass("red").addClass("green");
  else
    $("#toggle_header").removeClass("green").addClass("red");
});
