drop database if exists banco;
create database banco;
use banco;

create table persona(
	dni int primary key,
    nombre varchar(20)not null,
    apellido varchar(20)not null
);

create table dep_ret(
    deposito float,
    retiro float,
    dni_persona int not null
);


alter table dep_ret
add foreign key (dni_persona)
references persona(dni);

TRUNCATE TABLE dep_ret;
TRUNCATE TABLE persona;

/*insert into persona(dni,nombre,apellido)
values (39770803,"Facundo","Patino");

insert into dep_ret(deposito, retiro, dni_persona)
values(3000,1000,39770803),(3000,5000,39770803);

 
select p.dni, p.nombre, p.apellido, sum(d.deposito), sum(d.retiro), sum(d.deposito) - sum(d.retiro) as saldo
from persona as p join dep_ret as d on p.dni=d.dni_persona;
*/


