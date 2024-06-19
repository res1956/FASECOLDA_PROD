
truncate table enaccion.paso
begin tran
delete from  enaccion.seguros_archivos 
commit tran
truncate table enaccion.sg_fasecolda
begin tran
delete from  enaccion.sg_controlfasecolda 
commit tran


select count(1) from enaccion.sg_controlfasecolda
select count(1) from enaccion.sg_fasecolda