CKEDITOR.replace('blogeditor');

var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
	mode: "text/x-c++src",
	styleActiveLine: true,
	lineNumbers: true,
	lineWrapping: true
});

$.ajaxSetup({
  cache: true
});

$(document).ready(function() {
	$("#insert_code").bind("click",function(){

	})
})

$(document).ready(function() {
	$("#lang").change(function() {
		var lang = $("#lang").find("option:selected").text();
		switch (lang) {
			case "C/C++":
				editor.setOption("mode","text/x-c++src");
				break;
			case "Java":
				editor.setOption("mode", "text/x-java");
				break;
			case "C#":
				editor.setOption("mode", "text/x-csharp");
				break;
			case "Python":
				editor.setOption("mode", "python");
				break;
			case "html/xml":
				editor.setOption("mode", "xml");
				break;
			case "JavaScript":
				editor.setOption("mode", "javascript");
				break;
			case "Go":
				editor.setOption("mode", "go");
				break;
			case "php":
				editor.setOption("mode", "application/x-httpd-php");
				break;
			case "SQL":
				editor.setOption("mode", "text/x-mariadb");
				break;
			case "Shell":
				editor.setOption("mode", "shell");
				break;
			case "MarkDown":
				editor.setOption("mode", "markdown");
				break;
			default :
				editor.setOption("mode","text/x-c++src");
		}
	})
})

function getScriptPath (lang) {
	return "static/codemirror/mode/" + lang + "/" + lang + ".js";
}