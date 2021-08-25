var checkID1 = true;
var checkID2 = true;
var checkID3 = true;

$(document).ready(function() {
 

    document.getElementById("savebtn").disabled = true;

    $('#idcard2').on('keyup', function() {
        if ($.trim($(this).val()) != '' && $(this).val().length == 13) {
            id = $(this).val().replace(/-/g, "");
            var result = Script_checkID(id);
            if (result === false) {
                $('span.error2').removeClass('true').text('เลขบัตรผิด');
                checkID3 = false;
            } else {
                $('span.error2').addClass('true').text('เลขบัตรถูกต้อง');
                checkID3 = true;

            }
            if (checkID1  == false || checkID2 == false || checkID3 == false)
            {
                document.getElementById("savebtn").disabled = true;
            }
            if (checkID1  == true && checkID2 == true && checkID3 == true)
            {
                document.getElementById("savebtn").disabled = false;
            }        

        } else {
            $('span.error2').removeClass('true').text('');
            document.getElementById("savebtn").disabled = true;
            checkID3 = false;
        }
    })
});

$(document).ready(function() {
    $('#idcard1').on('keyup', function() {
        if ($.trim($(this).val()) != '' && $(this).val().length == 13) {
            id = $(this).val().replace(/-/g, "");
            var result = Script_checkID(id);
            if (result === false) {
                $('span.error1').removeClass('true').text('เลขบัตรผิด');
                checkID2 = false;
            } else {
                $('span.error1').addClass('true').text('เลขบัตรถูกต้อง');
                checkID2 = true;
            }
            if (checkID1  == false || checkID2 == false || checkID3 == false)
            {
                document.getElementById("savebtn").disabled = true;
            } 
            if (checkID1  == true && checkID2 == true && checkID3 == true)
            {
                document.getElementById("savebtn").disabled = false;
            }                         
        } else {
            $('span.error1').removeClass('true').text('');
            document.getElementById("savebtn").disabled = true; 
        }
    })
});

$(document).ready(function() {
    $('#idcard').on('keyup', function() {        
        if ($.trim($(this).val()) != '' && $(this).val().length == 13) {
            id = $(this).val().replace(/-/g, "");
            var result = Script_checkID(id);
            if (result === false) {
                $('span.error').removeClass('true').text('เลขบัตรผิด');
                checkID1 = false;
            } else {
                $('span.error').addClass('true').text('เลขบัตรถูกต้อง');
                checkID1 = true;
            }
            if (checkID1  == false || checkID2 == false || checkID3 == false)
            {
                document.getElementById("savebtn").disabled = true;
            } 
            if (checkID1  == true && checkID2 == true && checkID3 == true)
            {
                document.getElementById("savebtn").disabled = false;
            }                          
        } else {
            $('span.error').removeClass('true').text('');
            document.getElementById("savebtn").disabled = true;

        }
    })


});

function Script_checkID(id) {
    if (!IsNumeric(id)) return false;
    if (id.substring(0, 1) == 0) return false;
    if (id.length != 13) return false;
    for (i = 0, sum = 0; i < 12; i++)
        sum += parseFloat(id.charAt(i)) * (13 - i);
    if ((11 - sum % 11) % 10 != parseFloat(id.charAt(12))) return false;
    return true;
}

function IsNumeric(input) {
    var RE = /^-?(0|INF|(0[1-7][0-7]*)|(0x[0-9a-fA-F]+)|((0|[1-9][0-9]*|(?=[\.,]))([\.,][0-9]+)?([eE]-?\d+)?))$/;
    return (RE.test(input));
}

