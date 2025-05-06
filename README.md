Sistema de Votación:  Django + MySQL + Python

Este es un proyecto de API REST para gestionar un sistema de votación con autenticación JWT y restricciones de lógica de negocio 

Tecnologías Usadas

Django = 4.x
djangorestframework
mysqlclient
djangorestframework-simplejwt
django-cors-headers
python 3.x
Visual Studio Code
MysqlWorkbeach 8.0

Instalacion: 

1) Clona el repositorio
2) Crea un entorno virtual en la terminal e instalalo (puede ser visual studio code)

python -m venv env
source env/bin/activate

3) Configura la base de datos (dejo mi base ya que falto crear el .env)

4. Ejecuta la migraciones y crea el superusuario (JWT)

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

5) Ejecuta el servidor 

python manage.py runserver

se puede probar con la extension de postman que viene en visual studio para hacer las pruebas



1. Modelos:

Voter: id (autoincrementado), name, email, has_voted

Candidate: id (autoincrementado), name, email, party, votes

Vote: id (autoincrementado), voter, candidate


Restricciones implementadas:

1) Un usuario no puede estar en ambas tablas: votante y candidato. Se valida con el email ya que el id siempre va cambiando automaticamente

2) Un votante solo puede emitir un voto (has_voted = True después de votar).

3) Se actualiza automáticamente el conteo de votos del candidato.

4) Se valida que el candidate_id sea válido antes de votar.


Endpoints Disponibles:

la Base de la URL siempre sera: /api/

Autenticación:

Método	    URL	                    
POST	 /api/token/	            para obtener token JWT
POST	/api/token/refresh/	    para refrescar token

Votantes:

"name"
"email"
	        
POST	/voters/	para crear un nuevo votante
GET	/voters/	para listar todos los votantes
GET	/voters/id/	para obtener detalle de un votante
DELETE	/voters/id/	para eliminar un votante

Candidatos: 

"name"
"party"
"email"

POST	/candidates/		para crear nuevo candidato
GET	/candidates/		para listar todos los candidatos
GET	/candidates/{id}/	para obtener detalle del candidato
DELETE	/candidates/{id}/	para eliminar candidato


Votos:

"voter"
"candidate"

POST	/votes/	                para emitir voto
GET	/votes/	                para ver todos los votos
GET	/votes/statistics/	para ver estadísticas de votación


Postdata: Si durante la ejecucion del servidor hay errores de mysqlcliente o el rest framwork del jwt se ejecutan estos dos comandos


para instalar el mysqlclient: pip install mysqlclient


rest_framework_simplejwt: pip install djangorestframework-simplejwt
