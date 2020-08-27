**Authentication**

Authentication in GridAPPS-D is handled using JSON Web Tokens (JWT).  This allows the user to obtain a token, and continue to use it for the duration of their session.  

*Retrieving and using a token*

1. Send a token request to "/topic/pnnl.goss.token.topic"  with the content a base64 encrypted version of the <username>:<password>   
	The credentials for this request will be the username/password
2. You will receive a token back on /queue/temp.token_resp.<username>    The response will be only the token, no json wrapping.
3. Use the token in place of the username for all future requests, the password can be empty.  Note: if the server restarts or the token expires you will need to retrieve a new token.


*Anatomy of a token*

We use JSON web tokens, for more details view - https://jwt.io/introduction/  A JSON Web Token consists of three parts: Header, Payload and Signature. The header and payload are Base64 encoded, then concatenated by a period, finally the result is algorithmically signed producing a token in the form of header.claims.signature. The header consists of metadata including the type of token and the hashing algorithm used to sign the token. The payload contains the claims data that the token is encoding. 
  
  The payload will look something like this 
  
::
  
	{"sub":"operator1","nbf":1597702372898,"iss":"GridOPTICS Software System","exp":1598134372898,"iat":1597702372898,"jti":"6b615b4c-e51d-4241-9d3f-96eb29dbc8bb","roles":["testmanager","application","service","admin","operator","evaluator"]}
  
The elements included in the token are:
	- sub contains the username of the authenticated user
	- nbf, not before, or when the token is first valid.  This will generally be the same as when it was issued
	- iss, who issued the token
	- exp, when the token expires
	- iat, when the token was issued
	- jti, the token identifier uuid
	- roles, the authenticated roles for that user.  






