# 🐣 LOGON AUTOSTART EXECUTION - inicio automático de inicio de sesión debido a las claves de ejecución

Si un atacante encuentra un servicio que tiene todos los permisos y está vinculado con la clave de ejecución del Registro, puede realizar escalada de privilegios o ataques de persistencia. Cuando un usuario legítimo inicia sesión, el enlace del servicio con el registro se ejecutará automáticamente y este ataque se conoce como Ejecución de inicio automático de inicio de sesión debido a las claves de ejecución del registro.

Las claves de registro Run y RunOnce hacen que los programas se ejecuten cada vez que un usuario inicia sesión. Las claves de registro Ejecutar ejecutarán la tarea cada vez que se inicie sesión. Las claves de registro RunOnce ejecutarán las tareas una vez y luego eliminarán esa clave. Luego están Run y RunOnce; la única diferencia es que RunOnce eliminará automáticamente la entrada tras una ejecución exitosa

Veremos mas ampliamente este tema en este PDF:

<figure><img src="../../../.gitbook/assets/Logon-Autostart-Execution-Registry-Run-Keys-pdf.png" alt=""><figcaption></figcaption></figure>



{% file src="../../../.gitbook/assets/Logon Autostart Execution (Registry Run Keys).pdf" %}



{% file src="../../../.gitbook/assets/Logon Autostart Execution (Registry Run Keys) (español).pdf" %}
