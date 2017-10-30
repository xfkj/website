'use strict';

$(document).ready(function () {

    $('#name, #mobile').on('input', function (e) {
        checkField();
        var label = $(this).prev('label');
        e.target.value.length > 0 ? label.addClass('active') : label.removeClass('active');
    });

    $('.option').on('change', 'input', function (e) {
        checkField();
        $('.option').find('label').css({
            color: '#ADADAD'
        });
        $(this).parent().css({
            color: '#28A4FF'
        });
    });

    function checkField() {
        var fields = {};
        var flag = false;
        $('.form').serializeArray().forEach(function (item) {
            fields[item.name] = item.value;
        });
        if (typeof fields.option !== 'undefined') {
            Object.keys(fields).forEach(function (key) {
                if (typeof fields[key] === 'undefined' || !fields[key].length) {
                    flag = true;
                }
            });
        } else {
            flag = true;
        }
        flag ? $('#submitBtn').attr('disabled', 'disabled') : $('#submitBtn').attr('disabled', null);
    }

    /*$('#submitBtn').on('click', function(e) {
        e.preventDefault();
        var fields = $('.form').serializeArray();
        var data = {};
        fields.forEach(item => {
            data[item.name] = item.value;
        })
        var phoneReg = /^1(3|4|5|7|8)\d{9}$/;
        if (!phoneReg.test(data.mobile)) {
            alert('手机号码不符合格式')
        } else {
            //$('.popup').show();
        }
    })*/
});