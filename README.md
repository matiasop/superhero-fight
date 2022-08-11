# superhero-fight

Superhero fight simulator made using the [superhero API](https://www.superheroapi.com/).

## Instrucciones

Para correr el programa correr: `python src/main.py`

**Importante**: es necesario tener un archivo `.env` en el directorio raíz del proyecto con los datos de la API y del mailer.

## Especificación de las Peleas

- Las peleas son por turnos entre el equipo 0 y el equipo 1, ambos compuestos de 5 superheroes elegidos aleatoriamente.
- En cada turno va a haber un equipo que ataca y otro que defiende. El equipo que ataca va a elegir aleatoriamente a un superheroe para atacar, mientras que el equipo que defiende va a elegir a elegir a alguien que va a recibir el daño.
- El atacante va a elegir aleatoriamente entre sus posibles ataces (mental, strong, fast) y le va a hacer daño al superheroe que defiende.
- El equipo que se quede sin integrantes vivos (que tengan hp > 0) pierde.

## Mailer

Como se usó la versión gratuita del Mailgun, solo se pueden enviar correos a cuentas verificadas. Es por esto que de momento todos los mails se mandan a `superheroapitestmail34@yopmail.com`. Para ver los correos, visitar [yopmail.com](https://yopmail.com) e ingresar a `superheroapitestmail34@yopmail.com`. (No es necesario ingresar contraseña).
