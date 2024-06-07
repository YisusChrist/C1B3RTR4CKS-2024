Challenge: Inspector Gadget
Category: Web
Points: 10

¿Tienes lo necesario para convertirte en el Inspector Web Gadget y encontrar lo que buscas en este desafío de ciberseguridad? Demuestra tus habilidades detectivescas y desentraña el misterio en línea!

Flag: `LetsCTF{alw4y5_ch3ck_th3_s0urce_343532}`

Solución: Al inspeccionar el código fuente de la página, se encuentra la flag en un comentario HTML:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>web 20 @ Shellmates Infinite CTF 2k20</title>
    <link rel="stylesheet" href="style.css" />
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" />
    <link rel="icon" href="/favicon.ico" type="image/x-icon" />
  </head>

  <body>
    <div class="splash">
      <h1 class="splash-head">Heyy, It's <u>Inspector</u> gadget here</h1>
      <h2 style="color:white; background-color: red;">
        I always check the <u>source</u> of the problem
      </h2>
      <img src="inspector_gadget.jpg" class="img-responsive" />
    </div>
  </body>

  <!-- Here is your flag -->
  <!-- LetsCTF{alw4y5_ch3ck_th3_s0urce_343532} -->

  <!-- It's always a good idea to check the source code of a page -->
</html>
```
