"INSERT INTO `user` (`user_id`, `first_active_ts`, `first_name`, `last_name`, `profile_pic_link`, `locale`, `timezone`, `gender`, `is_payment_enabled`, `marked_spam`, `has_blocked`) VALUES ('" + userId + "' , '" + firstActiveTs+ "' , '" + firstName+ "' , '" + lastName+ " ',' " + profilePicLink+ " ', '" + locale+ " ', '" + timezone+ " ', '" + gender+ " ', '" + isPaymentEnabled+ " ', '" + markedSpam+ " ', '" + hasBlocked+ "')"



"INSERT INTO `chatlog` (`user_id`, `timestamp`, `channel_id`, `user_session_number`, `user_message_number`, `message_type`, `message_chat`, `message_type_flag`, `visual_search`, `product_response_list`, `nlp_query_response`, `vision_file_link`, `vision_engine_response` ) VALUES ('" + userId + "' , '" + timestamp + "' , '" + channelId + "' , '" + userSessionNumber + "' , '" + userMessageNumber + "' , '" + messageType + "' , '" + messageChat + "' , '" + messageTypeFlag + "' , '" + visualSearch + "' , '" + productResponseList + "' , '" + nlpQueryResponse + "' , '" + visionFileLink + "' , '" + visionEngineResponse + "')"


"INSERT INTO `click` (`user_id`, `session_number`, `message_number`, `timestamp`, `click_item`) VALUES ('" + user + "' , '" + userId + "' , '" + sessionNumber + "' , '" + messageNumber + "' , '" + timestamp + "' , '" + clickItem + "')"