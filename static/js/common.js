$(document).ready(function () {
    //检测ie 6789
    if (!(/msie [6|7|8|9]/i.test(navigator.userAgent))) {
        window.scrollReveal = new scrollReveal({
            reset: true
        });
    }
    // 弹窗回复评论
    var list = document.getElementsByClassName('replyComment');
    for (var i of list) {
        i.addEventListener("click", function (ev) {
            ev.preventDefault();
            var txt=  "请输入回复：";
            window.wxc.xcConfirm(txt, window.wxc.xcConfirm.typeEnum.input,{
                onOk:function(reply){
                    console.log(reply);
                }
            });
        }, false);
    }

    /*nav show or hide*/
    $('.nav>li').hover(function () {
        $(this).children('ul').stop(true, true).show(400);
    }, function () {
        $(this).children('ul').stop(true, true).hide(400);
    });
    /*search*/
    $('.search_ico').click(function () {
        $('.search_bar').toggleClass('search_open');
        if ($('#keyboard').val().length > 2) {
            $('#keyboard').val('');
            $('#searchform').submit();
        } else {
            return false;
        }
    });
    /*banner*/
    $('#banner').easyFader();

    /*topnav select*/
    var obj = null;
    var allMenu = document.getElementById('topnav').getElementsByTagName('a');
    // console.log(allMenu);
    obj = allMenu[0];
    for (i = 1; i < allMenu.length; i++) {
        if (window.location.href.indexOf(allMenu[i].href) >= 0) {
            obj = allMenu[i];
        }
    }
    obj.id = 'topnav_current';

    /*mnav dl open*/
    var oH2 = document.getElementsByTagName('h2')[0];
    var oUl = document.getElementsByTagName('dl')[0];
    oH2.onclick = function () {
        var style = oUl.style;
        style.display = style.display == 'block' ? 'none' : 'block';
        oH2.className = style.display == 'block' ? 'open' : '';
    };
    //菜单点击效果
    $('.list_dt').on('click', function () {
        $('.list_dd').stop();
        $(this).siblings('dt').removeAttr('id');
        if ($(this).attr('id') == 'open') {
            $(this).removeAttr('id').siblings('dd').slideUp();
        } else {
            $(this).attr('id', 'open').next().slideDown().siblings('dd').slideUp();
        }
    });

    //设置固定关注我们

    if ($('#follow-us')) {
        var followUsPosition = $('#follow-us').offset().top;
        window.onscroll = function () {
            var nowPosition = document.documentElement.scrollTop;
            if (nowPosition - followUsPosition > 0) {
                setTimeout(function () {
                    $('#follow-us').attr('class', 'guanzhu gd');
                }, 150);
            } else {
                $('#follow-us').attr('class', 'guanzhu');
            }
        };
    }


    //回到顶部
    // browser window scroll (in pixels) after which the "back to top" link is shown
    var offset = 300,
        //browser window scroll (in pixels) after which the "back to top" link opacity is reduced
        offset_opacity = 1200,
        //duration of the top scrolling animation (in ms)
        scroll_top_duration = 700,
        //grab the "back to top" link
        $back_to_top = $('.cd-top');

    //hide or show the "back to top" link
    $(window).scroll(function () {
        ($(this).scrollTop() > offset) ? $back_to_top.addClass('cd-is-visible'): $back_to_top.removeClass('cd-is-visible cd-fade-out');
        if ($(this).scrollTop() > offset_opacity) {
            $back_to_top.addClass('cd-fade-out');
        }
    });
    //smooth scroll to top
    $back_to_top.on('click', function (event) {
        event.preventDefault();
        $('body,html').animate({
            scrollTop: 0,
        }, scroll_top_duration);
    });

});



function check_login() {
    var loginStatus =0
    $.get('/check_login/',function (data) {
        html = "";
        if(data.loginStatus == 1){
            html += " <span id='welcome' >用户:";
            html += data.uname
            html += "</span>&nbsp;&nbsp;&nbsp;&nbsp;";
            html += " <a href= '/logout/' id='logout' >退出</a>";
        }else{
            html += " <a href='/login/' id='login' >登录</a>";
            html += "<a href= '/register/' id='register' target='_blank'>注册</a>";
        }
        $("#check_login>li").html(html)
    },'json');
}



function getXhr(){
    //如果浏览器支持XMLHttpRequest,则创建XMLHttpRequest的对象并返回
    if(window.XMLHttpRequest){
        return new XMLHttpRequest();
    }else{
        //如果浏览器不支持XMLHttpRequest的话,则创建ActiveXObject的对象并返回
        return new ActiveXObject("Microsoft.XMLHTTP");
    }
}





$(document).ready(function(){
    // 检查用户的登录状态
    check_login();
    getXhr();
})



