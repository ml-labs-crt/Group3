$(document).ready(function(){
    'use strict';
    new WOW().init();
});

//Counter
$(document).ready(function(){
    $('.counter-num').counterUp({
        delay:10,
        time:2000
    });
});

//News
$(document).ready(function(){
      $(".linkfeat").hover(
        function () {
            $(".textfeat").show(500);
        },
        function () {
            $(".textfeat").hide(500);
        }
    );
});
