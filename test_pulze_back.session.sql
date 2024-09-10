ALTER TABLE `pulze_back`.`users` 
ADD COLUMN `public_id` VARCHAR(45) NOT NULL AFTER `uuid`,
CHANGE COLUMN `public_key` `uuid` VARCHAR(2048) NOT NULL;