$(function() {
    var topAppBar = $("#topAppBar");
    // "a:not([data-toggle])" - to avoid issues caused
    // when you have dropdown inside navbar
    topAppBar.on("click", "a:not([data-toggle])", null, function() {
        topAppBar.collapse('hide');
    });
});