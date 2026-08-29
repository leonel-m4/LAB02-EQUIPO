# Sistema de Reserva de Citas Veterinarias

# Integrantes
- Retamozo De la Cruz Leonel Mathias
- Rojas Condor Jose Saith

## Problemática

Una veterinaria puede tener dificultades para organizar las citas de los clientes al momento de registrarlas manualmente o mediante mensajes. Esto puede provocar horarios repetidos, pérdida de información o confusión sobre las mascotas atendidas. Se propone crear una aplicación web que permita registrar y visualizar las citas de manera más sencilla. La utilizarían los trabajadores de la veterinaria para controlar las reservas de atención.

## Requisitos funcionales

- Registrar citas
- Registrar el nombre del dueño de la mascota
- Registrar el nombre de la mascota
- Registrar el tipo servicio solicitado
- Registrar la fecha de la cita
- Mostrar una lista de todas las citas que se han registrado

## App creada

Se creó la App `veterinaria` dentro del proyecto Django.

La aplicación contiene:

- `models.py`: contiene los datos estáticos de las citas.
- `views.py`: contiene las vistas para listar y registrar citas.
- `urls.py`: define las rutas.
- `forms.py`: contiene el formulario de registro.
- `templates/`: contiene las páginas HTML.

## Almacenamiento

La aplicación no utiliza una base de datos ni migraciones. Los registros se almacenan temporalmente en una lista de Python dentro de `models.py`.

Los nuevos registros se pierden cuando se reinicia el servidor.

## Flujo MVT

El usuario realiza una solicitud mediante una URL. Django dirige la solicitud hacia una View. La View obtiene o modifica los datos almacenados en `models.py` y posteriormente envía la información a un Template. El Template genera la respuesta HTML que se muestra en el navegador.

## Convivencia con core

La App `veterinaria` funciona dentro del mismo proyecto Django que la App `core`.

La ruta `/veterinaria/` se dirige a las URLs de la nueva App, mientras que las rutas existentes de `core` permanecen funcionando.

## Pruebas realizadas

### Caso de prueba 1: Listado

Se ingresó a `/veterinaria/` y se verificó que las cinco citas iniciales fueran mostradas correctamente.

### Caso de prueba 2: Formulario

Se ingresó a `/veterinaria/crear/` y se verificó que el formulario permitiera ingresar los datos de una nueva cita.

### Caso de prueba 3: Registro

Se registró una nueva cita con datos válidos y se verificó que apareciera en el listado después de enviar el formulario.

### Caso de prueba 4: Validación

Se intentó enviar el formulario dejando campos obligatorios vacíos.

Resultado: El formulario no registró el dato y aparecieron errores de validación.

### Caso de prueba 5: Reinicio

Se reinició el servidor y se verificó que el registro agregado desapareciera, confirmando que los datos se almacenan únicamente en memoria.

### Caso de prueba 6: Core

Se comprobó que las rutas y funcionalidades existentes de `core` continúan funcionando.
