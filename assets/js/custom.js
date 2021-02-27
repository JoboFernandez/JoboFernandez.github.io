(function() {
    $("#personal_project1.gif").hover(
        function() {
            $(this).attr("src", "images/personal_project1.gif");
        },
        function() {
            $(this).attr("src", "images/personal_project1.png");
        }
    );
});