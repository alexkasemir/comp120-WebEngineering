var Template = function(post) {
	var output = "<div class='container-post' id= 'post" + post.id + "''>";
	if(post.text_content) {
		output = output + '<div class="post-content"> <h1>' + post.text_content +'</h1></div>';
	}
	if(post.image_URL) {
		output = output + '<div class="post-content"><img src="https://purrer.s3.amazonaws.com/media/' + post.image_URL + '"/></div>';
	}
	output = output + '<div class="post-info"><div class="post-footer"><button class="btn btn-success purrButton pull-left" id="'+ post.id +'">Purrrr</button><h4 class="postInfo">Last edited: '+ post.time_edited + ' | Score: '+ post.score + '</h4><button class="btn btn-danger grrButton pull-right" id="' + post.id + '">Grrrrr!</button></div></div></div>';

	return output;
};


var post = {
	'id' : '1',
	'text_content': 'belh dksjflds sdkfl',
	'image_URL': 'https://slkfjls.sdflkjsdlkf.dsf',
	'time_edited': 'now',
	'score': '100'
}
