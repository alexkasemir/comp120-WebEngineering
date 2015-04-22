function endOut() {
	output = "<div id='no-more'><h1>There seems to be no more purrs...Want to create a new one?<h1><a href='#myModal' role='button' class='btn btn-large btn-primary' data-toggle='modal'>Create Purr</a></div>";
	return output;
}
$(window).scroll(function() {
   if($(window).scrollTop() + window.innerHeight == $(document).height()) {
   	lowest_posted_id = $("#latest_posts").children().last()[0].id;
   	$.ajax({
            url: 'api/posts_group/'+lowest_posted_id,
            data: {
                format: 'json'

            },
            success: function(data){
                //alert(data)
                if (data.length > 0){
                	var newPostStack = [];
                    for(var i in data){
                        var output = Template(data[i]);
                        newPostStack.push(output);
                    }
                    last = '#' + $("#latest_posts").children().last()[0].id;
                    console.log(last);
                    for(var i = newPostStack.length; i >= 0; i--){
						$("#latest_posts").append(newPostStack[i]);
					}
					purrUpdate();
					grrUpdate();
				}
				else {
					if (!document.getElementById("no-more")) {
  						var out = endOut();
						$("#latest_posts").parent().append(out);
					} 
				}
            }
        });
   }
});