// xheditor全局变量
var editor;

$(function () {
	editor = $('#blogeditor').xheditor({plugins: getCodePlugin(), tools:'mfull'})
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

// 上传图片
$(function () {
    $('#btn_addimg').click(function (e) {
        e.preventDefault();
        window.frames["uploadframe"].document.forms[0].submit();
    });
})

$(function () {
    // post new article之前检查本地检测数据是否完整
    $('#btn_post').click(function (e) {
        var flag = 0;
        if ($.trim($('#articlename').val()) == '') {
            showErr("Please input the title.");
            flag = 1;
        } else if ($.trim($('#blogeditor').val() === '')) {
            showErr("Please input the content of your alticle.");
            flag = 1;
        }
        if (flag) {
            e.preventDefault();
        }
    })
})

// 显示博客编辑相关的错误信息
function showErr (msg) {
    $('#edit_alert').html(msg);
    $('#edit_alert').show();
}

// 上传图片成功后，将图片的URL附加到图片列表中
function setPath (path) {
    id = getid(path);
    $('#imgs').append('<tr><td>' + path + '</td><td><div class="form-inline"><button type="submit" class="btn btn-warning btn-small" id="i_btn_' + id + '" onclick="insertimg(this);">I</button><button type="submit" class="btn btn-danger btn-small" id="d_btn_' + id + '" onclick="delimg(this);">D</button></div></td></tr>');
}

// 根据服务器对图片的重命名获得图片的ID
function getid (path) {
    imgName = path.substr(path.lastIndexOf("/")+1);
    // return imgName.substr(0, imgName.lastIndexOf("."));
    return imgName
}

// 将图片插入到xheditor
function insertimg(e) {
    // alert(e.parentNode.parentNode.previousSibling.innerHTML);
    var url = e.parentNode.parentNode.previousSibling.innerHTML;
    var str = "<img src='" + url + "' />";
    if (editor) {
        editor.loadBookmark();
        editor.pasteHTML(str);
    } else {
        $('#blogeditor').val($('#blogeditor').val() + str);
    }
}

// 特别注意e是xml DOM对象
function delimg(e) {
    if ($("#blogeditor").val().indexOf(e.parentNode.parentNode.previousSibling.innerHTML) > 0) {
        alert("This image was in your article, you cannot delete it.");
        return;
    }

    var img_name = e.id.substr(6,id.length);

    if (confirm("Are you sure to delete this image?")) {
        $.ajax({
            type:"post",
            url:"delimg/",
            dataType:"text",
            data:{
                'img_id':img_name,
                'csrfmiddlewaretoken':getCookie("csrftoken")
            },
            success:function (data) {
                if (data != "success") {
                    $("#alert").show();
                } else {
                    // 删除图片表格对应的行
                    e.parentNode.parentNode.parentNode.remove();
                }
            },
            error:function (XHR,textStatus,errorThrown) {
                alert("XHR="+XHR+"\ntextStatus="+textStatus+"\nerrorThrown=" + errorThrown);
            },
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