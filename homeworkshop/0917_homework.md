# 0917_homework

1.

  is_superuser   / is_staff / is_active



2.  255





3. 

   .is_authenticated : 로그인여부 (속성)

   .is_anonymous : 로그아웃 여부 (속성)





4.  

   a) AuthenticationForm

   b) login

   c) request.POST



5. 

   AnnoymousUser



6. 

```python
PBKDF2 , pbkdf2_sha256$36000$<my salt>$<my hash>

class PBKDF2PasswordHasher(BasePasswordHasher):
    """
    Secure password hashing using the PBKDF2 algorithm (recommended)

    Configured to use PBKDF2 + HMAC + SHA256.
    The result is a 64 byte binary string.  Iterations may be changed
    safely but you must rename the algorithm if you change SHA256.
    """
    algorithm = "pbkdf2_sha256"
    iterations = 36000
    digest = hashlib.sha256

    def encode(self, password, salt, iterations=None):
        assert password is not None
        assert salt and '$' not in salt
        if not iterations:
            iterations = self.iterations
        hash = pbkdf2(password, salt, iterations, digest=self.digest)
        hash = base64.b64encode(hash).decode('ascii').strip()
        return "%s$%d$%s$%s" % (self.algorithm, iterations, salt, hash)
```

7. 

이유: logout 함수와 , logout class 명이 겹치게 되면서 오류가 생긴다..

해결방법, import 한 logout  클래스를 as 로 별칭을 바꿔준다.



