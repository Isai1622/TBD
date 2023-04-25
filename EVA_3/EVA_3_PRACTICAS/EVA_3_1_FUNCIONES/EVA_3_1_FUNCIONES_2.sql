DELIMITER $$
CREATE DEFINER=`root`@`localhost` FUNCTION `regresa_dos`() RETURNS int
    DETERMINISTIC
return 2$$
DELIMITER ;
create function regresa_mensaje(cade varchar(50))
returns varchar(100) deterministic
return concat("hola", cade);
