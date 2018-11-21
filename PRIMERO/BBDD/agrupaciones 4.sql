select * from CLIENTS
select * from COMANDES
select * from EMPLEATS
select * from OFICINES
select * from PRODUCTES


1.Quantes comandes hi ha del fabricant aci?

select count(distinct numcomanda) as 'Numero de pedidos' from COMANDES where fab like 'aci'

2.Obtenir el nom dels tres empleats més majors

select top 3 nom from EMPLEATS order by edat desc

3.Obtenir l'identificador dels productes que s'han demanat dues o més vegades. 
Mostra també les vegades que s'han demanat.'

select  producte, fab, count(producte) as 'Veces que se ha prdido' from comandes 
group by producte, fab having count(producte) >=2


4.Mostrar el nom i l'edat dels 2 empleats que fa més temps que treballen a l'empresa

select top 2 nom, edat from EMPLEATS order by contracte asc

5.Obtenir la ciutat a què pertanyen les oficines que no han realitzat cap venda. 
El nom de la ciutat ha d'aparèixer una única vegada en el resultat. Consulta només les dades de la taula oficines.'

select distinct ciutat from OFICINES where vendes = 0

6.Conta el número de clients que han realitzat alguna comanda.

select count(distinct cl.numclie) as 'Numero de clientes' from CLIENTS as cl join COMANDES as co on cl.numclie = co.clie

7.Donar el dia i els mesos de l'any 1997 en els que el client amb codi 2111 
ha fet alguna comanda.'

select DAY(datacomanda) as 'Día', MONTH(datacomanda) as 'Mes' from COMANDES where clie = 2111 and YEAR(datacomanda) = 1997
