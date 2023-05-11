create trigger mensaje after insert on personas
for each row
set @mensaje = 'personas insertada con exito';