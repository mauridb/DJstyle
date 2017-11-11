$(document).ready(function(){

    console.log('jquery ready');

//    $.getJSON( "api/v1/projects", function( data ) {
//      var items = [];
//      $.each( data, function( key, val ) {
//        items.push( "<li id='" + key + "'>" + val + "</li>" );
//      });
//
//      $( "<ul/>", {
//        "class": "my-new-list",
//        html: items.join( "" )
//      }).appendTo( "body" );
//    });

    function split_btns(list_buttons){
        var btns_under = []
        var btns_over = []
        for (var i=0; i < list_buttons.length; i++){
            text_btn = list_buttons[i].text.split('|');
            value = parseInt(text_btn[1])
            if (value < 0){
                btns_under.push(list_buttons[i])
                $(btns_under).removeClass('btn-primary').addClass('btn-danger');
            }else{
                btns_over.push(list_buttons[i])
            }
        }
    }

    split_btns($('.cc'))
});