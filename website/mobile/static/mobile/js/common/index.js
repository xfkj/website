'use strict';

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

$(document).ready(function () {
    /**
     * 返回history back
     */
    $('#back').on('click', function () {
        window.history.back();
    });

    /**
     * fastclick
     */
    FastClick.attach(document.body);

    /**
     * headRoom
     */
    if ($('.headroom').length) {
        var headroom = new Headroom($('.headroom')[0]);
        headroom.init();
    }
});