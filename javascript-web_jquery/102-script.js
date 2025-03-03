#!/usr/bin/node
// fetch IP code and return hello in the correct language

$(document).ready(function () {
  $("#btn_translate").on("click", function () {
    const languageCode = $("#language_code").val();
    console.log(languageCode);
    const proxyUrl = "https://api.allorigins.win/get?url=";
    const apiurl = `https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`;
    $.get(proxyUrl + encodeURIComponent(apiurl), function (data) {
        const response = JSON.parse(data.contents);
      $("#hello").text(response.hello);
    }).fail(function (error) {
      console.error("Error fetching translation", error);
    });
  });
});
