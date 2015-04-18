// Prevent XSS Attacks
var entityMap = {
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': '&quot;',
    "'": '&#39;',
    "/": '&#x2F;'
};

var months = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
};

function escapeHtml(string) {
    return String(string).replace(/[&<>"'\/]/g, function (s) {
        return entityMap[s];
    });
}

function fixDate(date) {
    var d = new Date(date);
    console.log(d.toString());
    date = d.toString();
    var year  = date.substring(11,15);
    var month = date.substring(4,7);
    var day   = date.substring(8,10);
    var hour  = parseInt(date.substring(16,18));
    var min   = date.substring(19,21);
    var am_pm = (hour >= 12) ? "p.m. " : "a.m. ";
    var real_hour = (hour > 12) ? hour - 12 : hour;

    return months[month] + " " + day + ", " + year + ", " + real_hour + ":" + min + " " + am_pm;


}

var Template = function(post) {


    var output = "<div class='container-post' id='" + post.id + "'>";
    output = output + '<div class="well"> Created by: ' + post.creator + '</div>';
    if(post.text_content) {

        output = output + '<div class="post-content"> <h1>' + escapeHtml(post.text_content) +'</h1></div>';
    }
    if(post.image_URL) {
        output = output + '<div class="post-content"><img src="https://purrer.s3.amazonaws.com/media/' + post.image_URL + '"/></div>';
    }
    output = output + '<div class="post-info"><div class="post-footer"><button class="btn btn-success purrButton pull-left" id="'+ post.id +'">Purrrr</button><h4 class="postInfo">Created At: '+ fixDate(post.time_created) + ' | Score: '+ post.score + '</h4><button class="btn btn-danger grrButton pull-right" id="' + post.id + '">Grrrrr!</button></div></div></div>';

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
                data_length = data.length;
                newest_post_id = data[0].id;
                if (newest_post_id > highest_posted_id){
                    for(var i in data){
                        if(data[i].id > highest_posted_id){
                            highest_posted_id = data[i].id;
                            console.log(data[i].creator);
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

                    $('.Add_Post_Button_Container').css("visibility","visible");
                }
            }
        });
    }, 5000);
}




