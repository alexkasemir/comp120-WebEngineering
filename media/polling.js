
var Template = function(post) {


    var output = "<div class='container-post' id='" + post.id + "'>";
    if(post.text_content) {
        output = output + '<div class="post-content"> <h1>' + post.text_content +'</h1></div>';
    }
    if(post.image_URL) {
        output = output + '<div class="post-content"><img src="https://purrer.s3.amazonaws.com/media/' + post.image_URL + '"/></div>';
    }
    output = output + '<div class="post-info"><div class="post-footer"><button class="btn btn-success purrButton pull-left" id="'+ post.id +'">Purrrr</button><h4 class="postInfo">Created At: '+ post.time_created.toString() + ' | Score: '+ post.score + '</h4><button class="btn btn-danger grrButton pull-right" id="' + post.id + '">Grrrrr!</button></div></div></div>';

    return output;
};

var newPostStack = [];

function long_poll(){

    highest_posted_id = $("#latest_posts").children().first()[0].id;
    highest_posted_id = parseInt(highest_posted_id);
    window.setInterval(function() {
        $.ajax({
            url: '/api/posts',
            data: {
                format: 'json'

            },
            success: function(data){
                console.log(data);
                data_length = data.length;
                newest_post_id = data[0].id;
                if (newest_post_id > highest_posted_id){
                    for(var i in data){
                        if(data[i].id > highest_posted_id){
                            highest_posted_id = data[i].id;
                            var output = Template(data[i]);
                            newPostStack.push(output);
                        }
                    }
                    //make the html for the posts
                    //"this is a string" + var + " more string"
                    //  for loop for all the new posts
                    //make a button appear telling how many are new
                    //prepend onto latest_post
                }
                if(newPostStack.length !== 0){
                    console.log("here");
                    $('.Add_Post_Button_Container').css("visibility","visible");
                }
            }
        });
    }, 5000);
}




