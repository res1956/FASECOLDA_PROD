
select * from [dbo].[seguros_archivos]





begin tran
delete seguros_archivos where nombre='332_Abril_2024_Version17Abr'
commit tran



create table paso_excel  (texto varchar(8000))

alter table paso_archivos alter column nombre varchar(55)

select * from paso_archivos;

select * from paso_excel

--drop table paso_excel 

alter table paso_excel alter column texto varchar(8000)

bulk insert paso_excel   from 'd:\descargas\csv\encabezado_excel.txt'
with ( ROWTERMINATOR ='\n',FIELDTERMINATOR=';')


bulk insert paso_excel   from 'd:\descargas\csv\Guia_Excel_332.csv'
with ( ROWTERMINATOR ='\n',FIELDTERMINATOR=';',FIRSTROW=2)

truncate table  paso_excel;

truncate table paso_archivos;

select * from paso_excel where texto like 'nOVEDAD%'

