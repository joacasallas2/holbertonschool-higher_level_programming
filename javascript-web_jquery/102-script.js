#!/usr/bin/node
// fetch IP code and return hello in the correct language

$(document).ready(function () {
  $("#btn_translate").on("click", function (event) {
    const languageCode = $("#language_code").val();

    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`,
      method: "GET",
      success: function (data) {
        $("#hello").text(data.hello);
      },
      error: function (err) {
        console.error(err);
      },
    });
  });
});
