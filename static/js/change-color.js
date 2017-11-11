$(document).ready(function(){

    console.log('jquery ready');

//    var buttons = $('.btn.btn-primary.cc')
//    for (var i=0; i < buttons; i++){
//        var text = buttons[i].text;
//        var btn = buttons[i];
//        var new_text = text.split(" | ")
//        var likes_value = parseInt(new_text[1]);
//        if(likes_value < 0){
//            //change btn likes to btn btn-danger
//            btn.removeClass('btn-primary');
//
//        }
//    }
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