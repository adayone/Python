drop TABLE resys_user_item;
drop TABLE resys_user_items;
drop TABLE resys_user_minhashs;

-- user item table --
CREATE TABLE resys_user_item(user string, item string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' ;

-- user items table --
-- format : user\titemitem1... --
CREATE TABLE resys_user_items(user string, items string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' ;

-- user minhash table --
-- format : user\tminhashminhash1... --
CREATE TABLE resys_user_minhash(user string, minhash string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' ;

-- minhash users table --
-- format : key\tuseruser1... --
CREATE TABLE resys_user_cluster(key string, users string) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' ;
