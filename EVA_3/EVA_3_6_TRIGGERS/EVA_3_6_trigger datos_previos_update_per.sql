delimiter //
create trigger datos_previos_update_per after update on personas
for each row 
begin
	insert into auditoria_per 
    values(
    old.id, 
    old.nombre,
    old.apellido_pat, 
    old.apellido_mat,
    old.fecha_nac, 
    old.clave_rfc
    );
end //
delimiter ;