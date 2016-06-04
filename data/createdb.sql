create DATABASE scanomatic;
use scanomatic;
create table alimentos (
	id int PRIMARY KEY auto_increment,
	Alimento varchar (64),
	Calorias float (4), 
	Grasas_total float (4),
	Acidos_grasos_saturados float (4),
	Acidos_grasos_poliinsaturados float (4),
	Acidos_grasos_monoinsaturados float (4),
	Colesterol float (4),
	Sodio float (4),
	Potasio float (4),
	Carbohidratos float (4),
	Fibra float (4),
	Azucares float (4),
	Proteinas float (4),
	Hierro float (4),
	Calcio float (4),
	Magnesio float (4),
	VitaminA float (4),
	VitaminB6 float (4),
	VitaminB12 float (4),
	VitaminC float (4),
	VitaminD float (4),
	VitaminE float (4),
	VitaminF float (4))
