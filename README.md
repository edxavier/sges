Note that if deploying to Apache using mod_wsgi, the authorization header is not passed through to a WSGI application by default, as it is assumed that authentication will be handled by Apache, rather than at an application level.

If you are deploying to Apache, and using any non-session based authentication, you will need to explicitly configure mod_wsgi to pass the required headers through to the application. This can be done by specifying the WSGIPassAuthorization directive in the appropriate context and setting it to 'On'.

# this can go in either server config, virtual host, directory or .htaccess
WSGIPassAuthorization On