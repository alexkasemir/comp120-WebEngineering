function getAllPosts() {
    return httpGet('http://blueberry-cake-2991.herokuapp.com/api/posts/?format=json');
}

function getPostById(id) {
    return httpGet('http://blueberry-cake-2991.herokuapp.com//api/posts/' + id.toString() +'?format=json');
}

function getUserByUsername(username) {
    return httpGet('http://blueberry-cake-2991.herokuapp.com//api/users/' + username.toString() +'?format=json');
}


function createUser(username, password, email) {
    var header = "username=" + username + "&email=" + email;
    return httpPost('http://blueberry-cake-2991.herokuapp.com/api/users/', header);
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