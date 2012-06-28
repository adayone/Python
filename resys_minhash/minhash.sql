add file minhash.py;
add file map_minhash.py;
insert overwrite resys_user_items select user, wm_concat('', item) as items from resys_user_item group by user;
insert  overwrite resys_user_minhash select tranform(user, items) using './map_minhash.py' as user, minhash from resys_user_items;
insert overwrite resys_user_cluster select minhash as key, wm_concat('', user) as users from resys_user_minhash group by minhash;
