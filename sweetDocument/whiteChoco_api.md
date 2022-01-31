# API 정의서

## darkChoco (공통)
```
Path: /

Request
Method: [GET]

Response
Render: index.html
```

```
Path: /darkChoco/post

Request
Method: [POST]
Parameters:
    {
        "to_user" : "...",
        "letter_text" : "...",
    }

Response
Redirect: /

```