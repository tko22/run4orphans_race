$(function(){

    //csrf stuff
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
    });
    $('#minor-signup').click(function() {
        if($('#minor-signup').is(':checked')) {
            $('.minor-form').show();
        }
        else{
            $('.minor-form').hide();
        }
    });

    $("#register-btn").click(function(){
        var first_name = $('#fname-form').val();
        var last_name = $('#lname-form').val();
        var email = $('#email-form').val();
        var phone = $('#phone-form').val();
        var address = $('#address-form').val();
        var over_eighteen = $('#over-18').is(':checked');
        var under_eighteen = $('#minor-signup').is(':checked');
        var tshirt_size = $('#shirt-form :selected').attr('id');
        var waiver = $('#terms-condition').is(':checked');
        var minor_name = $('#minority-name-form').val();
        var minor_bday = $('#minority-bday-form').val();
        var gender = $('#gender-form :selected').attr('id');
        var additional_money = 0;
        if (over_eighteen == false && under_eighteen == false){
            $("#error-msg").text("Please mark if you are over 18 and registering for yourself or for a minor").show();
            return;
        }
        else if (over_eighteen == true && under_eighteen==true) {
            $("#error-msg").text("Please mark one option for whether your registering for minor or yourself").show();
            return;
        }
        else if (over_eighteen == false && under_eighteen==true){
            if (minor_name==null || minor_bday==null){
                $("#error-msg").text("Please enter minor name and/or birthday in MM/DD/YYYY format").show();
            }
            return;
        }
        if( first_name == "" || last_name =="" || email==""|| phone=="" || address==""){
            $('#error-msg').text("Please fill everything in this form").show();
            return;
        }
        if($("#10-dollars").is(':checked')){
            additional_money = additional_money + 10;
        } else if($("#20-dollars").is(':checked')){
            additional_money = additional_money + 20;
        } else if($("#50-dollars").is(':checked')){
            additional_money = additional_money + 50;
        }else if($("#100-dollars").is(':checked')){
            additional_money = additional_money + 100;
        }




        if (gender == 'male') gender = true
        if (gender == 'female') gender = false
        $.ajax({
            type:'POST',
            url:'/api/registeruser/',
            data: JSON.stringify({
                code: $('body').attr('id'),
                fname: first_name,
                lname: last_name,
                email: email,
                phone: phone,
                address: address,
                over_eighteen: over_eighteen,
                under_eighteen: under_eighteen,
                tshirt_size: tshirt_size,
                waiver: waiver,
                minor_name: minor_name,
                minor_bday: minor_bday,
                gender: gender,
            }),

            dataType: 'json',
            success: function(data){
                if(data.status == 'failed'){
                    $('#error-msg').text(data.message).show();
                }
                else{
                    var money = 20 + additional_money;
                    window.location.replace("https://www.paypal.me/lightandlovehome/"+money);
                }
            }
        })
    });




});

//csrf stuff
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
