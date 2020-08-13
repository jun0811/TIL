# 0812_homework



### 1.

```html
    <div class="container">
      <div class="row justify-content-center"> 
        <button type="button" class="col-6 btn btn-success btn-lg">sign in</button>
      </div>
    </div>
```

### 2. 

```html
<div class="fixed-top">
        
        <nav class="navbar navbar-dark bg-dark justify-content-start">
            <img src="./image/ssafy.png" class="img-fluid mr-3">
            <div class="btn-group" role="group" aria-label="Button group with nested dropdown">
                <div class="btn-group" role="group">
                <button id="btnGroupDrop1" type="button" class="btn btn-dark dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    프로젝트
                </button>
                <div class="dropdown-menu" aria-labelledby="btnGroupDrop1">
                    <a class="dropdown-item" href="#">Dropdown link</a>
                    <a class="dropdown-item" href="#">Dropdown link</a>
                </div>

                <div class="btn-group" role="group">
                <button id="btnGroupDrop1" type="button" class="btn btn-dark dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    그룹들
                </button>
                <div class="dropdown-menu" aria-labelledby="btnGroupDrop1">
                    <a class="dropdown-item" href="#">Dropdown link</a>
                    <a class="dropdown-item" href="#">Dropdown link</a>
                </div>
            
                <div class="btn-group" role="group">
                <button id="btnGroupDrop1" type="button" class="btn btn-dark dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    더보기
                </button>
                <div class="dropdown-menu" aria-labelledby="btnGroupDrop1">
                    <a class="dropdown-item" href="#">Dropdown link</a>
                    <a class="dropdown-item" href="#">Dropdown link</a>
                </div>
                </div>
                </div>
                </div>
            </div>
        </nav>
      </div>
```

### 3. 

```html
<nav aria-label="Page navigation example">
  <ul class="pagination">
      <li class="page-item"><a class="page-link text-secondary " href="#">Prev</a></li>
      <li class="page-item "><a class="page-link text-dark" href="#">1<span class="sr-only">(current)</span></a></li>
      <li class="page-item active" aria-current="page"><span class="page-link">
              2
      <span class="sr-only">(current)</span></span></li>
      <li class="page-item"><a class="page-link text-dark" href="#">3</a></li>
      <li class="page-item"><a class="page-link text-dark" href="#">4</a></li>
      <li class="page-item"><a class="page-link text-dark" href="#">5</a></li>
      <li class="page-item"><a class="page-link text-secondary" href="#">...</a></li>
      <li class="page-item"><a class="page-link text-dark" href="#">Next</a></li>
      <li class="page-item"><a class="page-link text-dark" href="#">last</a></li>
    </ul>
</nav>
```



### 4. 

```html
    <div class="container">
      <div class="row justify-content-center">
        <form>
          <div class="box bg-danger text-white pl-2">Invalid Login or password</div>
          <div class="form-group">
            <h1>SSAFY 전용 GitLab 시스템</h1>
            <hr>
            
            <label for="exampleInputEmail1">Username or email</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">Password</label>
            <input type="password" class="form-control" id="exampleInputPassword1">
          </div>
            <div class="form-group form-check d-flex justify-content-between">
              <div>
                <input type="checkbox" class="form-check-input" id="exampleCheck1">
                <label class="form-check-label" for="exampleCheck1">Remember me</label>
              </div>
              <p class="text">Forgot your password?</p>
            </div>
            <button type="button" class=" btn btn-success btn-lg col">sign in</button>
         
       
        </form>
      </div>
    </div>
```

