add file minhash.py;
add file map_minhash.py;
#insert overwrite table resys_user_item select uid as user, pid as item from test_resys_kevin_new_resys_log_info where dt='20120426' and hour='18' and type='browse' and source='cnzz';
#insert overwrite table resys_user_items select user, wm_concat('', item) as item_list from resys_user_item group by user;
insert  overwrite table resys_user_minhash select transform(user, item_list) using 'source ~/.bashrc && tee input |python2.5 map_minhash.py 2>stderr |tee output' from resys_user_items;
#insert overwrite table resys_user_cluster select minhash as key, wm_concat('', user) as users from resys_user_minhash group by minhash;
