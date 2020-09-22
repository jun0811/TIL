## install_sqlite_windows_10

> windows 10 64bit 기준

### 1. sqlite 공식 홈페이지 접속

![01](https://user-images.githubusercontent.com/52446416/63410179-ab6b0200-c42d-11e9-8621-c6cd72baf713.png)

---

### 2. 파일 다운로드

![02](https://user-images.githubusercontent.com/52446416/63410180-ab6b0200-c42d-11e9-9df7-a74b7ef55792.png)

---

### 3. C드라이브 - sqlite 폴더 생성 후 압축풀기

![03](https://user-images.githubusercontent.com/52446416/63410182-ab6b0200-c42d-11e9-82e5-5f4654d4b8b8.png)

---

### 4. 시스템 환경변수 추가

![04](https://user-images.githubusercontent.com/52446416/63410184-ac039880-c42d-11e9-9b01-3f066e24dbb1.png)
![05](https://user-images.githubusercontent.com/52446416/63410185-ac039880-c42d-11e9-9f5b-1017e7010f9a.png)
![06](https://user-images.githubusercontent.com/52446416/63410186-ac039880-c42d-11e9-8ce7-6cfcc69e0e8d.png)
![07](https://user-images.githubusercontent.com/52446416/63410188-ac9c2f00-c42d-11e9-8d37-0114e881f312.png)

---

### 5. 설치 확인

> 반드시 vscode, git bash 등 터미널 관련 프로그램 모두 종료 후 재시작

```bash
$ winpty sqlite3
```

![08](https://user-images.githubusercontent.com/52446416/63410190-ac9c2f00-c42d-11e9-9c85-1fddec3a89a8.png)

---

### 6. alias 등록

```bash
# ~/.bashrc
alias sqlite3="winpty sqlite3"
```

```bash
$ source ~/.bashrc
```

```bash
$ sqlite3
```

