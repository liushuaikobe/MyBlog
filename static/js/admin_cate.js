$(function () {
	$("button.btn-warning").click(function (e){
		e.preventDefault();

		var id = $(this).attr("id");

		var cate_no = id.substr(6, id.length);

		var dp_id_selector = "#dp_" + cate_no;
		var ed_id_selector = "#ed_" + cate_no;
		var ip_id_selector = "#ip_" + cate_no;

		if (!($(dp_id_selector).width() <= 0 || $(dp_id_selector).height() <= 0)) {
			$(dp_id_selector).hide();
			$(ed_id_selector).show();
			$(ip_id_selector).focus();
		} 
		return false;
	})
})

$(function () {
	$("input.ip").blur(function () {
		// the id of the input that lose foucs
		var id = $(this).attr("id");

		var cate_no = id.substr(3, id.length);

		var dp_id_selector = "#dp_" + cate_no;
		var ed_id_selector = "#ed_" + cate_no;
		var m_btn_id_selector = "#m_btn_" + cate_no;
		var ip_id_selector = "#ip_" + cate_no;

		var old_cate_name = $(dp_id_selector).html();
		var new_cate_name = $.trim($(this).val());

		if (old_cate_name != new_cate_name && new_cate_name != "") {
			if (confirm("Are you sure to change \"" + old_cate_name + "\" to \"" + $(this).val() + "\"?")) {
				var csrftoken = getCookie('csrftoken');
				$.ajax({
					type:"post",
					url:"modifycate/",
					dataType:"text",
					data:{
						new_cate_name:new_cate_name, 
						cate_id:cate_no
					},
					success:function (data) {
						if (data == "success") {
							// alert("Modify sucessfully!");
							$(dp_id_selector).html(new_cate_name);
							$(ip_id_selector).val(new_cate_name);
						} else {
							alert("Modify fail,please try later...");
							$(ip_id_selector).val(old_cate_name);
						}
					},
					error:function (XHR,textStatus,errorThrown) {
						alert("XHR="+XHR+"\ntextStatus="+textStatus+"\nerrorThrown=" + errorThrown);
						$(ip_id_selector).val(old_cate_name);
					},
					headers:{
						"X-CSRFToken":csrftoken
					}
				})
			} else {
				$(ip_id_selector).val(old_cate_name);
			}
		} else {
			$(ip_id_selector).val(old_cate_name);
		}
		$(dp_id_selector).show();
		$(ed_id_selector).hide();
	})
})

$(function () {
	$("button.btn-danger").click(function (e) {
		e.preventDefault();

		var id = $(this).attr("id");

		var cate_no = id.substring(6, id.length);

		var tr_selector = "#tr_" + cate_no;
		var dp_id_selector = "#dp_" + cate_no;

		if(confirm("Are you sure to delete the category " + $(dp_id_selector).html() + " ?")) {
			var csrftoken = getCookie('csrftoken');

			$.ajax({
				type:"post",
				url:"delcate/",
				dataType:"text",
				data:{
					cate_id:cate_no
				},
				success:function (data) {
					if(data == "success") {
						$(tr_selector).remove();
						// location.reload();
					} else {
						alert("Delete fail,please try later...");
					}
				},
				error:function (XHR,textStatus,errorThrown) {
					alert("XHR="+XHR+"\ntextStatus="+textStatus+"\nerrorThrown=" + errorThrown);
				},
				headers:{
						"X-CSRFToken":csrftoken
				}
			})
		}
	})
})

$(function () {
	$("#add_btn").click(function (e) {
		e.preventDefault();

		var new_cate_name = $.trim($("#new_cate_name").val());
		if (new_cate_name == "") {
			$("#alert").show();
			return;
		}

		var csrftoken = getCookie('csrftoken');

		$.ajax({
			type:"post",
			url:"addcate/",
			dataType:"text",
			data:{
				new_cate_name:new_cate_name
			},
			success:function (data) {
				if (data == "success") {
					location.reload();
				} else {
					$("#alert").html("Add fail,pleasr try later..");
				}
			},
			error:function (XHR,textStatus,errorThrown) {
				alert("XHR="+XHR+"\ntextStatus="+textStatus+"\nerrorThrown=" + errorThrown);
			},
			headers:{
				"X-CSRFToken":csrftoken
			}
		})
	})
})

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