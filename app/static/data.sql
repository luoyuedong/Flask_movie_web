ALTER TABLE user auto_increment=1;

INSERT INTO comment(movie_id,user_id,content,addtime) VALUES (7,1,"好看",now());
INSERT INTO comment(movie_id,user_id,content,addtime) VALUES (7,2,"给力",now());
INSERT INTO comment(movie_id,user_id,content,addtime) VALUES (7,3,"无聊",now());
INSERT INTO comment(movie_id,user_id,content,addtime) VALUES (7,5,"恐怖",now());
INSERT INTO comment(movie_id,user_id,content,addtime) VALUES (6,6,"有趣",now());
INSERT INTO comment(movie_id,user_id,content,addtime) VALUES (6,7,"精彩",now());
INSERT INTO comment(movie_id,user_id,content,addtime) VALUES (7,8,"好看",now());
INSERT INTO comment(movie_id,user_id,content,addtime) VALUES (7,9,"好看",now());
INSERT INTO comment(movie_id,user_id,content,addtime) VALUES (8,10,"好看",now());
INSERT INTO comment(movie_id,user_id,content,addtime) VALUES (9,11,"好看",now());
INSERT INTO comment(movie_id,user_id,content,addtime) VALUES (3,1,"好看",now());
INSERT INTO comment(movie_id,user_id,content,addtime) VALUES (2,34,"好看",now());
INSERT INTO comment(movie_id,user_id,content,addtime) VALUES (3,16,"好看",now());

ALTER TABLE comment auto_increment=1;