# API 정의서

## whiteChoco (회원관리)
```
Path: /whiteChoco/signup

Request
Method: [GET]

Response
Render: signup.html
```

```
Path: /whiteChoco/signup

Request
Method: [POST]
Parameters:
    {
        "username" : "...",
        "password1" : "...",
        "password2" : "...",
        "nickname" : "...",
    }

Response
Redirect: /whiteChoco/userpage/nickname

```

```
Path: /whiteChoco/login

Request
Method: [GET]

Response
Render: login.html

```

```
Path: /whiteChoco/login

Request
Method: [POST]
Parameters:
    {
        "username" : "...",
        "password2" : "...",
    }

Response
Redirect: /whiteChoco/userpage/nickname

```

```
Path: /whiteChoco/logout

Request
Method: [GET]

Response
Render: /

```