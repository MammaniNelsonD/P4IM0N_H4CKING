# 👁️ RECONOCIMIENTO PASIVO

## AUDITORIA DE: ((Laboratorio: XSS almacenado en contexto HTML sin nada codificado))

***

***

### RECONOCIMIENTO PASIVO

*   [x] BROWSER --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

    ```python
    <div class="blog-post">
                            <a href="/post?postId=1"><img src="/image/blog/posts/63.jpg"></a>
                            <h2>Shopping Woes</h2>
                            <p>I'm one of those really annoying people you don't want to get stuck behind in the grocery store. I love to chat, and boy can I chat, to the cashier. My money is always at the bottom of my rucksack,...</p>
                            <a class="button is-small" href="/post?postId=1">View post</a>
                            </div>
    ```

    * CONCLUSION:  VEMOS QUE MANEJA CON EL PARAMENTRO POSTID CON NUMEROS CORRELATIVOS CADA POST
    *

        <figure><img src="../../../../.gitbook/assets/Stored XSS into HTML context with nothing encoded.png" alt="" width="356"><figcaption></figcaption></figure>



* [x] BROWSER --------------------------------->[https://www.paimon.com.ar/](https://www.google.com/)

```python
<form action="/post/comment" method="POST" enctype="application/x-www-form-urlencoded">
                            <input required="" type="hidden" name="csrf" value="5aGK2T2ryPOp8qacwVPwWi9aaiShRntn">
                            <input required="" type="hidden" name="postId" value="1">
                            <label>Comment:</label>
                            <textarea required="" rows="12" cols="300" name="comment"></textarea>
                                    <label>Name:</label>
                                    <input required="" type="text" name="name">
                                    <label>Email:</label>
                                    <input required="" type="email" name="email">
                                    <label>Website:</label>
                                    <input pattern="(http:|https:).+" type="text" name="website">
                            <button class="button" type="submit">Post Comment</button>
                        </form>
```

* CONCLUSION:  VEMOS EL FORMULARIO DE QUE POR METODO POST ENVIA LOS COMENTARIOS DE LOS USARIOS EN EL SITIO, VEMOS COMO CON ACTION /post/comment HACE UN LALMADO A LA FUNCION QUE RECIBE LOS DATOS EN EL SERVIDOR
*

    <figure><img src="../../../../.gitbook/assets/Stored XSS into HTML context with nothing encoded (1).png" alt=""><figcaption></figcaption></figure>

