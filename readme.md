el proyecto esta formado por:

- 4 modelos: Course, Assignment, Student y Teacher
- 18 urls
- 1 modulo que ya trae la indormacion de los cursos disponibles de la DB
- 4 buscadores para cada tipo de modelo
- 4 formularios: uno para crear cada tipo de los modelos

Crear cursos y chequear los cursos disponibles en la pestania de cursos! habra un curso de
cada tipo, ejemplo si hay  cursos de Python, 2 de Java y 1 de Data, va a mostrar 1 curso de cada
tipo. Solo se brinda la informacion del curso sin la comision.

Para consultar los cursos y las comisiones ir al buscador de cursos y escribir el curso previamente
visualizado en la pestaña de cursos y mostrara los cursos disponibles con las comisiones
correspondientes.

Crear estudiantes y consultarlos desde el buscador de estudiantes para poder ver nombre completo
y email

Crear profesores y consultarlos desde el buscador de profesores para poder ver nombre completo,
profesor de que curso es y el mail

luego en la parte de creacion de estudiantes hay otra opcion llamada Assignment que es para entregar
los trabajos practicos. Se completa con los datos solicitados y se puede tildar si esta el trabajo
completo o no.

las busquedas tambien tienen validaciones de que minimo tengan que tener 3 caracteres de cualquier
campo. Se puede buscar por cada campo independiente y conseguira la informacion correspondiente
en base a la busqueda. Ejemplo, si hay 2 cristian y busca desde "cri" ya le traera la informacion
de ambos. Mientras mas completa sea la busqueda mas acertada será.

las creaciones de cursos, estudiantes y profesores y entregables se guardan en la base de datos
todo en minuscula. 

el template tiene modificaciones tanto de reformas visuales para una mejor visibilidad en la web
como bloques de divisiones.

tambien se agrego una redireccion en la parte de registro de estudiante, profesores, cursos y entregables
el cual informa si se creo con exito o no y si se hace con exito te redirecciona al inicio a los 5 segundos
