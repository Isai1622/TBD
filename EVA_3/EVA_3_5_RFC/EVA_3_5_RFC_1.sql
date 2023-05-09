DELIMITER $$
CREATE FUNCTION generaar_rfc(apellido_pat VARCHAR(255), apellido_mat VARCHAR(255), nombre VARCHAR(255), fecha_nac DATE)
RETURNS VARCHAR(255)
deterministic
BEGIN
  DECLARE rfc VARCHAR(255);

  SET rfc = CONCAT(SUBSTR(apellido_pat, 1, 2), IFNULL(SUBSTR(apellido_mat, 1, 1), 'X'), SUBSTR(nombre, 1, 1), DATE_FORMAT(fecha_nac, '%Y%m%d'));

  RETURN rfc;
END $$
DELIMITER ;
