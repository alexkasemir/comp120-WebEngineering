$(document).ready(function(){
	var purr = $(".purrButton");
	var grr = $(".grrButton");
	function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie != '') {
	        var cookies = document.cookie.split(';');
	        for (var i = 0; i < cookies.length; i++) {
	            var cookie = jQuery.trim(cookies[i]);
	            if (cookie.substring(0, name.length + 1) == (name + '=')) {
	                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                break;
	            }
	        }
	    }
	    return cookieValue;
	}

	purr.click(function(){
		var csrftoken = getCookie('csrftoken');
		var curr = $(this);
		var text = curr.next().first().text();
		var n = text.search("Score: ");
		n = n + 7;
		var score = text.substr(n);
		scoreInt = parseInt(score);
		scoreInt = scoreInt + 1;
		var newText = text.substr(0,n) + " " + scoreInt;
		curr.next().first().text(newText);
		var id = curr[0].id;

		function csrfSafeMethod(method) {
		    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}
		$.ajaxSetup({
		    beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
		    }
		});

		$.ajax({
    			url:'like/' + id + "/",
		    	type: "POST",
		    	success:function(response){console.log("Liked!")},
		    	error:function (xhr, textStatus, thrownError){console.log("Like Failed :(")}
		});
	});
	
	grr.click(function(){
		var csrftoken = getCookie('csrftoken');
		var curr = $(this);
		var text = curr.prev().first().text();
		var n = text.search("Score: ");
		n = n + 7;
		var score = text.substr(n);
		scoreInt = parseInt(score);
		scoreInt = scoreInt - 1;
		var newText = text.substr(0,n) + " " + scoreInt;
		curr.prev().first().text(newText);
		console.log(newText);
		var id = curr[0].id;

		function csrfSafeMethod(method) {
		    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}
		$.ajaxSetup({
		    beforeSend: function(xhr, settings) {
		        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
		            xhr.setRequestHeader("X-CSRFToken", csrftoken);
		        }
		    }
		});

		$.ajax({
    			url:'dislike/' + id + "/",
		    	type: "POST",
		    	success:function(response){console.log("disLiked!")},
		    	error:function (xhr, textStatus, thrownError){console.log("disLike Failed :(")}
		});
	});
});