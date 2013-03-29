$(function () {
	var editor = $('#blogeditor').xheditor({plugins: getCodePlugin(), tools:'mfull'})
})

function getCodePlugin() {
	var codeArr1 = ["html", "javascript", "css", "php", "csharp", "cpp", "java", "python", "ruby", "vb", "delphi", "sql", "plain"]
	var codeArr2 = ["HTML/XML", "JavaScript", "CSS", "PHP", "C#", "C++", "Java", "Python", "Ruby", "Visual Basic", "Delphi", "SQL", "其它"]
	var opts = ''
	for (var i = 0; i < codeArr1.length; i++) {
        opts += '<option value="' + codeArr1[i] + '">' + codeArr2[i] + '</option>';
    }
    var htmlCode = '<div><select id="xheCodeType">' + opts + '</select></div>'
        + '<div><textarea id="xheCodeCon" rows=6 cols=40></textarea></div>'
        + '<div style="text-align:right;"><input type="button" id="xheSave" value="确定" /></div>';
    var codePlugin = {
        Code: { c: 'btnCode', t: '插入代码', h: 1, e: function () {
            var _this = this;
            var jTest = $(htmlCode);
            var jSave = $('#xheSave', jTest);
            jSave.click(function () {
                var sel_code = $("#xheCodeType").val();
                var str = '<pre name="code" class="' + sel_code + '">' + _this.domEncode($("#xheCodeCon").val()) + '</pre><br />';
                _this.loadBookmark();
                _this.pasteHTML(str);
                _this.hidePanel();
                return false;
            });
            _this.saveBookmark();
            _this.showDialog(jTest);
        }
        }
    };
    return codePlugin;
}

$(function () {
    $('#btn_addimg').click(function (e) {
        e.preventDefault();

        window.frames["uploadframe"].document.forms[0].submit();
    });
})

function setPath (path) {
    id = getid(path);
    $('#imgs').append('<tr id="tr_' + id + '"><td>' + path + '</td><td><div class="form-inline"><button type="submit" class="btn btn-warning btn-small" id="i_btn_' + id + '">I</button><button type="submit" class="btn btn-danger btn-small id="d_btn_' + id + '" onclick="delimg();">D</button></div></td></tr>');
}

function getid (path) {
    imgName = path.substr(path.lastIndexOf("/")+1);
    // return imgName.substr(0, imgName.lastIndexOf("."));
    return imgName
}

function delimg() {
    var id = $(this).attr("id");

    var imgName = id.substr(6, id.length);

    var trSelector = "#tr_" + imgName;


    if (confirm("Are you sure to delete this image?")) {
        var csrftoken = getCookie('csrftoken');
        $.ajax({
            type:"post",
            url:"delimg/",
            dataType:"text",
            data:{
                'img_id':id,
                'csrfmiddlewaretoken':getCookie("csrftoken")
            },
            success:function (data) {
                if (data != "success") {
                    $("#alert").show();
                }
            },
            error:function (XHR,textStatus,errorThrown) {
                alert("XHR="+XHR+"\ntextStatus="+textStatus+"\nerrorThrown=" + errorThrown);
            },
            headers:{
                "X-CSRFToken":getCookie('csrftoken')
            }
        });
    }
}

// Get cookie by cookie_name
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

















