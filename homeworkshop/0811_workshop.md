# 0811_workshop

```css
body {
  font-family: Arial;
  width: 800px;
  border : 4px;
}

.semantic { 
  border : 4px;
  margin : 4px;
  padding: 4px;
  background-color: lightgray;
}
h1 {
  text-align: center;
}

.section{
  border : 4px;
  margin : 4px;
  padding: 4px;
  background-color: lightgray;
  display: inline-block;
  width: 482px;
  height: 300px;
}
.aside{
  border : 4px;
  margin : 4px;
  padding: 4px;
  background-color: lightgray;
  display: inline-block;
  width: 280px;
  height: 300px;
  vertical-align: top;
}


.article {
  border : 4px;
  margin : 4px;
  padding: 4px;
  background-color: white;
}
```

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="semantic.css">
  <title>Layout Practice</title>
</head>
<body>
  <header class="semantic">
    <h1>header</h1>
  </header>
  <nav class='semantic'>
    <h2>nav</h2>
  </nav>
  <section class="section">
    <h2>section</h2>
    <article class="article">
      <h3>article1</h3>
      <h3>article2</h3>
    </article>
  </section>
  <aside class = "aside">
    <h2>aside</h2>
  </aside>
  <footer class ="semantic">
    <h2>footer</h2>
  </footer>
</body>
</html>

```

