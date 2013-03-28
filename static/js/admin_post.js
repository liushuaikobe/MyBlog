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