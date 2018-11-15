$(function () {
    $('#predict').click(function () {
        data = {
            'inputPredict': $('#inputPredict').val()
        }
        $('#loader').prop("hidden", false)
        $.get("save-predict", data, function (result, status) {
            if (jQuery.isEmptyObject(result) !== true) {
                var textGood = "";
                var textBad = "";
                var textNormal = "";
                $.each(result['good'], function (key, value) {
                    console.log(key + ": " + value['text']);
                    textGood = textGood + "<div class=\"form-group\">\n" +
                        "<label><input type=\"checkbox\" class=\"mr-3\" value='" + value['text'] + "' >" + value['text'] + "</label>\n" +
                        "</div>"

                });
                $('#good').html(textGood)
                $.each(result['bad'], function (key, value) {
                    console.log(key + ": " + value['text']);
                    textBad = textBad + "<div class=\"form-group\">\n" +
                        "<label><input type=\"checkbox\" class=\"mr-3\" value='" + value['text'] + "'>" + value['text'] + "</label>\n" +
                        "</div>"

                });
                $('#bad').html(textBad)
                $.each(result['normal'], function (key, value) {
                    console.log(key + ": " + value['text']);
                    textNormal = textNormal + "<div class=\"form-group\">\n" +
                        "<label><input type=\"checkbox\" class=\"mr-3\" value='" + value['text'] + "'>" + value['text'] + "</label>\n" +
                        "</div>"
                });
                $('#normal').html(textNormal)
                $('#loader').prop("hidden", true)
                alert("Status: " + status);
                $('#inputPredict').val('')
            } else {
                alert("Status: Error");
            }

        })
    })

    $('#saveGood').click(function () {
        var list_input = $("input[type='checkbox']");
        var data = {}
        var i = 0
        for( i;i<list_input.length;i++){
            if (list_input[i].checked){
               data[i] = list_input[i].defaultValue;
            }
        }
        $.get("save-good", data, function (result, status) {
            if (jQuery.isEmptyObject(result) !== true) {

            } else {
                alert("Status: Error");
            }

        })
    })
})


