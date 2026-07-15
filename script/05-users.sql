use INOVE_CONTABILIDADE;

# Criação de usuários
create USER 'douglas'@'%' IDENTIFIED by 'douglas123';
create USER 'amanda'@'%' IDENTIFIED by 'amanda123';
create USER 'emanuel'@'%' IDENTIFIED by 'emanuel123';
create USER 'augusto'@'%' IDENTIFIED by 'augusto123';

#Dando privilégios
GRANT all ON INOVE_CONTABILIDADE.* TO 'douglas'@'%';
GRANT SELECT,DELETE,UPDATE,INSERT ON INOVE_CONTABILIDADE.* TO 'amanda'@'%';
GRANT SELECT,DELETE,UPDATE,INSERT ON INOVE_CONTABILIDADE.* TO 'emanuel'@'%';
GRANT SELECT ON INOVE_CONTABILIDADE.* TO 'augusto'@'%';

#Recaregando sistema
FLUSH PRIVILEGES;

SELECT * FROM mysql.user;

#Mostrando os usuários e seus privilégios
SHOW GRANTS FOR 'douglas'@'%';
SHOW GRANTS FOR 'amanda'@'%';
SHOW GRANTS FOR 'emanuel'@'%';
SHOW GRANTS FOR 'augusto'@'%';
