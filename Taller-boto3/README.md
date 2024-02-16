BOTO3
-----


<br >![ Screenshot of the empty token dialog box ](assets/images/boto3.jpg)


# A first-level heading
## A second-level heading
### A third-level heading

Text that is not a quote

> Text that is a quote
> 
> 
>

Here is a simple footnote[^1].

A footnote can also have multiple lines[^2].

[^1]: My reference.
[^2]: To add line breaks within a footnote, prefix new lines with 2 spaces.
  This is a second line.



@octocat :+1: This PR looks great - it's ready to merge! :shipit:

> - George Washington
> - George Washington
> - George Washington
> - > - George Washington
* John Adams
+ Thomas Jefferson

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

```python

    def hola(nombre="Ceste"):
        return "Hola " + nombre

    print(hola())
    # Salida: 'Hola Ceste'

    # Podemos asignar una función a una variable
    saluda = hola
    # No usamos () porque no la estamos llamando, sino que la estamos
    # asignado a una variable

    print(saluda())
    # Salida: 'Hola Ceste'

    # También podemos eliminar la función asignada a la variable con del
    try:
        del hola
        print(hola())
    except Exception as e:
        print('Ocurrió un Exception. {}'.format(e.args[-1]))
    # Salida: NameError

    print(saluda())
    # Salida: 'Hola Ceste'

```