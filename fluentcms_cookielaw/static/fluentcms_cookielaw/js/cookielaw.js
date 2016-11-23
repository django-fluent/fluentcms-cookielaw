var Cookielaw = {

    onReady: function() {
        // Hide the banner when the cookie law is already accepted.
        // This is done client-side so the whole content can be cached server-side.
        var banner = document.getElementById('cookielaw-banner');
        if(document.cookie.indexOf('cookielaw_accepted=1') != -1) {
            banner.style.display = 'none';
        }
        else {
            banner.style.display = 'block';
        }
    },

    createCookie: function(name, value, days) {
        var date = new Date(),
            expires = '';
        if (days) {
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toGMTString();
        } else {
            expires = "";
        }
        document.cookie = name + "=" + value + expires + "; path=/";
    },

    accept: function() {
        this.createCookie('cookielaw_accepted', '1', 10 * 365);

        if (typeof (window.jQuery) === 'function') {
            jQuery('#cookielaw-banner').slideUp();
        } else {
            document.getElementById('cookielaw-banner').style.display = 'none';
        }
    },

    reset: function() {
        // For debugging
        this.createCookie('cookielaw_accepted', '0', -10);

        if (typeof (window.jQuery) === 'function') {
            jQuery('#cookielaw-banner').slideDown();
        } else {
            document.getElementById('cookielaw-banner').style.display = 'block';
        }
    }
};

if (typeof (window.jQuery) === 'function') {
    jQuery.fn.ready(Cookielaw.onReady);
}
else {
    if(document.addEventListener) {
        // Modern browsers
        document.addEventListener("DOMContentLoaded", Cookielaw.onReady);
    }
    else {
        // IE8
        document.attachEvent("onreadystatechange", function(){
            if (document.readyState === "complete"){
                document.detachEvent("onreadystatechange", arguments.callee);
                Cookielaw.onReady();
            }
        });
    }
}
