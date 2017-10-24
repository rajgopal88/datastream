-- -----------------------------------------------------
-- Schema metricdb
-- -----------------------------------------------------
-- botcoture_metricdb
-- botcoture_metricdb
-- expconsumerapp_metricdb

DROP DATABASE `jeanie_metricdb`;
CREATE DATABASE `jeanie_metricdb`;
USE `jeanie_metricdb`;

-- -----------------------------------------------------
-- Table `metricdb`.`user`
-- -----------------------------------------------------
CREATE TABLE `user` (
  `user_id` MEDIUMTEXT NULL,
  `first_active_ts` DATETIME NULL,
  `last_name` VARCHAR(50) NULL,
  `first_name` VARCHAR(50) NULL,
  `profile_pic_link` VARCHAR(255) NULL,
  `locale` VARCHAR(50) NULL,
  `timezone` VARCHAR(50) NULL,
  `gender` CHAR(1) NULL,
  `is_payment_enabled` TINYINT(1) NULL,
  `marked_spam` TINYINT(1) NULL,
  `has_blocked` TINYINT(1) NULL,
  PRIMARY KEY (`user_id`));


-- -----------------------------------------------------
-- Table `metricdb`.`chatlog`
-- -----------------------------------------------------
CREATE TABLE `chatlog` (
  `user_id` MEDIUMTEXT NULL,
  `timestamp` DATETIME NULL,
  `channel_id` VARCHAR(20) NULL,
  `session_id` VARCHAR(50) NULL,
  `message_number` INT(11) NULL,
  `message_type` VARCHAR(2) NULL,
  `message_chat` VARCHAR(255) NULL,
  `message_type_flag` VARCHAR(3) NULL,
  `visual_search` INT(11) NULL,
  `product_response_list` JSON NULL,
  `nlp_query_response` VARCHAR(255) NULL,
  `vision_file_link` VARCHAR(255) NULL,
  `vision_engine_response` VARCHAR(255) NULL,
  `quick_reply_button`  VARCHAR(255) NULL,
  SHARD KEY(`user_id`));


-- -----------------------------------------------------
-- Table `metricdb`.`click`
-- -----------------------------------------------------
CREATE TABLE `click` (
  `user_id` MEDIUMTEXT NULL,
  `session_id` VARCHAR(50) NULL,
  `message_number` INT(11) NULL,
  `timestamp` DATETIME NULL,
  `click_item` VARCHAR(50) NULL,
  SHARD KEY(`user_id`));


#ALTER TABLE chatlog MODIFY COLUMN product_response_list varchar(200);