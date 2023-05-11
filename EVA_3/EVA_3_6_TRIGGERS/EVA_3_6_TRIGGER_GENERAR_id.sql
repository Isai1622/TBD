DELIMITER //
CREATE TRIGGER GENERAR_id BEFORE INSERT ON actor
FOR EACH ROW
BEGIN
  DECLARE nuevo_id int;
  declare calcular_id int;
  SELECT ultimo_actor_id  INTO nuevo_id;
  if nuevo_id = null then
	SET calcular_id = 1;
  else
	set calcular_id =nuevo_id= 1;
  end if;
  SET NEW.actor_id = nuevo_id;
END; //
DELIMITER ;
