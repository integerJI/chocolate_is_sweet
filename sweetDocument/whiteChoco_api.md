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
{
    "result": "false",
    "error_code": "201",
    "message": "이미 사용중인 아이디 입니다.",
    "return_url": "/",
}
Redirect: /

```