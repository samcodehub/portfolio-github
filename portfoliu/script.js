

$(document).ready(function () {
    'use strict';

    setTimeout(function () {
        $('.loader_bg').fadeToggle();
    }, 1500);
alert("Welcome to my page :) Be patient it will take some times to load everything. ")
    $(window).on('scroll', function () {
        if ($(document).scrollTop() > 200) {
            $(".navbar").css({ "background-color": "#ffffff", "transition": "all 0.8s ease-in-out", "box-shadow": "0px 3px 4.6px 0.3px rgba(0, 0, 0, 0.25)" });
            $(".navbar-collapse").css("background-color", "transparent");
        } else {
            $(".navbar").css({ "background-color": "transparent", "box-shadow": "none" });
        }
    });

    var element = $(".text-affect");
    $(function () {
        element.typed({
            strings: ["Designer", "Developer", "Freelancer"],
            loop: true,
            typeSpeed: 90
        });
    });
    $('.skillbar').each(function () {
        $(this).find('.skillbar-bar').animate({
            width: $(this).attr('data-percent')
        }, 6000);
    });

    $('.view').magnificPopup({
        type: 'image',
        gallery: {
            enabled: true
        },
        zoom: {
            enabled: true,
            duration: 300,
            opener: function (element) {
                return element.find('img');
            }
        }
    });

    
    
    $("#collapsibleNavbar").click(function(){
    $("#collapsibleNavbar").hide();
  });
    $("#colnav").click(function(){
    $("#collapsibleNavbar").toggle();
  });

});

const form = document.querySelector('#contact-form');
function sendMsg(e){
    e.preventDefault();

const name = document.querySelector('#form_name'),
      email = document.querySelector('#form_email'),
      msg = document.querySelector('#form_message');

      Email.send({
        SecureToken : "f05cc1c6-2297-4f20-a418-e50753d4504d",
        To : 'samcodehub@outlook.com',
        From : email.value,
        Subject : "Contact Form",
        Body : msg.value
    }).then(
      message => alert(message)
    );
}

form.addEventListener('submit',sendMsg) ;

