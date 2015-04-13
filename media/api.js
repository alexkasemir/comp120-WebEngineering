function getAllPosts() {
    return httpGet('https://banana-cake-3532.herokuapp.com/meows/api/posts/?format=json');
}

function getPostById(id) {
    return httpGet('https://banana-cake-3532.herokuapp.com/meows/api/posts/' + id.toString() +'?format=json');
}

function getUserByUsername(username) {
    return httpGet('https://banana-cake-3532.herokuapp.com/meows/api/users/' + username.toString() +'?format=json');
}


function createUser(username, password, email) {
    var header = "username=" + username + "&email=" + email;
    return httpPost('https://banana-cake-3532.herokuapp.com/meows/api/users/', header);
}
function httpGet(url)
{
    var xmlHttp = null;
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", url, false );
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function httpPost(url, header)
{
    var xmlHttp = null;
    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "POST", url, false );
    xmlHttp.setRequestHeader("Content-type","application/json");
    xmlHttp.send(header);
    return xmlHttp.responseText;
}