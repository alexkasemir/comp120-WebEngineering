[optims]: optimis.png

##Optimizations for Purrer##

Note: The HTML5 Application Cache was giving us problems. We could not figure out
how to get the manifest file to actually work and using the html5_appcache thing
for django was not loading the files we wanted into the cache

###Techniques###

We implemented memcache on our web app that is hosted using amazon webservices.

Other techniques used(so far):

    Minification
    javascipt at the bottom of page
    CDN


To do:
    HTML5 Application Cache

###Tools###
Yslow and Google Developer tools


###Performance Aspects###
The Yslow ratings have not increased too much but the load times have slightly
improved once we added a feature. We tested on an EC2 instance that is half
functioning along with localhost. There was performance increase, but will have
to continue with optimizations over the next week to get this fully functioning.



###Optimizations###
![Optimizations][optims]
