$(document).ready(function(){
	var purr = $(".purrButton");
	var grr = $(".grrButton");
	var noPurr = $(".noPurrButton");
	var noGrr = $(".noGrrButton");
	var more_meows = $(".Add_Post_Button");
	var whoPurred = $(".whoPurredButton");
	long_poll();
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie !== ''){
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
	/* utility for setting the expiration date on a cookie given a number of 
	   seconds to expire and a cookie*/
	// function setCookieExpData(cookie, expSecs) {
 //    	var d = new Date();
 //        d.setTime(d.getTime() + (exSecs * 1000));
 //        var expires = "expires="+d.toUTCString();
 //    	return (cookie + expires);
	// }

	purr.click(function(){

		var csrftoken = getCookie('csrftoken');
		var curr = $(this);
		curr.prop('disabled', true);
		var text = curr.next().first().text();
		var currDislike = curr.next().next().first();
		currDislike.prop('disabled', true);
		console.log(currDislike);
		var n = text.search("Score: ");
		n = n + 7;
		var score = text.substr(n);
		scoreInt = parseInt(score);
		scoreInt = scoreInt + 1;
		var newText = text.substr(0,n) + " " + scoreInt;
		curr.next().first().text(newText);
		var id = curr[0].id;

		var string = "button#" + id;
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

	noPurr.click(function(){
		alert("You cannot purr twice!!!");
	});


	noGrr.click(function(){
		alert("You cannot grrr twice!!")
	});


	grr.click(function(){
		var csrftoken = getCookie('csrftoken');
		var curr = $(this);
		var currLike = curr.prev().prev();
		curr.prop('disabled', true);
		currLike.prop('disabled', true);
		var text = curr.prev().first().text();
		var n = text.search("Score: ");
		n = n + 7;
		var score = text.substr(n);
		scoreInt = parseInt(score);
		scoreInt = scoreInt - 1;
		var newText = text.substr(0,n) + " " + scoreInt;
		curr.prev().first().text(newText);

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

	whoPurred.click(function() {
		var curr = $(this);
	});

	more_meows.click(function() {

		for(var i in newPostStack){
			var test = $("#latest_posts");

			test.prepend(newPostStack[i]);
		}	
		newPostStack = [];
		$('.Add_Post_Button_Container').css("visibility", "hidden");
	});
});