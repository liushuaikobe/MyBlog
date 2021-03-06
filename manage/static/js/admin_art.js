$(function () {
	// 修改文章
	$("button.btn-warning").click(function (e) {
		e.preventDefault();

        var id = $(this).attr("id");
        var post_no = id.substring(6, id.length);

        window.location.replace("editpost/" + post_no);
	})
})

$(function () {
	// 删除文章
	$("button.btn-danger").click(function (e) {
		e.preventDefault();
		var id = $(this).attr("id");
		var post_no = id.substring(6, id.length);

		var tr_selector = "#tr_" + post_no;
        if (confirm("将删除该文章，此操作不可逆。")) {
    		$.ajax({
    			type:"post",
                url:"delpost/",
                dataType:"text",
                data:{
                    'post_id':post_no,
                    'csrfmiddlewaretoken':getCookie("csrftoken")
                },
                success:function (data) {
                    if (data != "success") {
                        $("#alert").show();
                    } else {
                        // 删除文章表格对应的行
                        $(tr_selector).remove();
                    }
                },
                error:function (XHR,textStatus,errorThrown) {
                    alert("XHR="+XHR+"\ntextStatus="+textStatus+"\nerrorThrown=" + errorThrown);
                },
    		});
        }
	})
})