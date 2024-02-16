BOTO3
-----

.. image:: assets/images/boto3.jpg
    :align: center
    :width: 300px
    :height: 280px

<br >![ Screenshot of the empty token dialog box ](assets/images/boto3.jpg)

.. note::
   This is note text. Use a note for information you want the user to
   pay particular attention to.

   If note text runs over a line, make sure the lines wrap and are indented to
   the same level as the note tag. If formatting is incorrect, part of the note
   might not render in the HTML output.

   Notes can have more than one paragraph. Successive paragraphs must
   indent to the same level as the rest of the note.

.. warning::
    This is warning text. Use a warning for information the user must
    understand to avoid negative consequences.

    Warnings are formatted in the same way as notes. In the same way,
    lines must be broken and indented under the warning tag.

.. code:: python

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