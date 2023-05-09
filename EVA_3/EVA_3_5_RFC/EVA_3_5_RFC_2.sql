DELIMITER $$
CREATE PROCEDURE actualizar_rfc()
BEGIN
  DECLARE done INT DEFAULT FALSE;
  DECLARE ap_paterno VARCHAR(255);
  DECLARE ap_materno VARCHAR(255);
  DECLARE nombre VARCHAR(255);
  DECLARE fecha_nac DATE;
  DECLARE rfc VARCHAR(255);
  DECLARE cur CURSOR FOR SELECT apellido_pat, apellido_mat, nombre, fecha_nac FROM personas;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  
  OPEN cur;
  
  read_loop: LOOP
    FETCH cur INTO ap_paterno, ap_materno, nombre, fecha_nac;
    
    IF done THEN
      LEAVE read_loop;
    END IF;
    
    SET rfc = generaar_rfc(ap_paterno, ap_materno, nombre, fecha_nac);
    
    UPDATE personas SET clave_rfc = rfc WHERE apellido_pat = ap_paterno AND apellido_mat = ap_materno AND nombre = nombre AND fecha_nac = fecha_nac;
  END LOOP;
  
  CLOSE cur;
END $$
DELIMITER ;
