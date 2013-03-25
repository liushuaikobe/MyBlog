$(function () {
	$("div.cate").show();
	$("div.cate_edit").hide();

	$("button.btn-warning").click(function (e){
		e.preventDefault();
		var id = $(this).attr("id");
		var dp_id = "dp_" + id.substr(6,id.length);
		var ed_id = "ed_" + id.substr(6,id.length);
		if ($("#" + dp_id).width() <= 0 || $("#" + dp_id).height() <= 0) {
			$("#" + dp_id).show();
			$("#" + ed_id).hide();
		} else {
			$("#" + dp_id).hide();
			$("#" + ed_id).show();
			$("#" + ed_id).focus();
			$(id).removeClass("btn-warning");
			$(id).addClass("btn-success");
			
		}
		return false;
	})

	$("input.ip").blur(function () {
		var id = $(this).attr("id");
		var dp_id = "dp_" + id.substr(3,id.length);
		var ed_id = "ed_" + id.substr(3,id.length);

		$("#" + dp_id).show();
		$("#" + ed_id).hide();
	})
})

