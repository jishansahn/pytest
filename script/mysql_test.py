import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
                             port=12318,
                             user='zhb',
                             password='zuihuibao2015',
                             db='dbzhb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        # sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id,
        # create_time) VALUES ("alen",18800110001,"alen@mail.com",0,1,NOW());'
        sql = 'update car_ins_date set ins_start_date=%s where frame_no=%s;'
        cursor.execute(sql, ('2016-12-27','LBV5S1105ESH54933',))
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM car_ins_date where frame_no=%s"
        cursor.execute(sql, ('LBV5S1105ESH54933',))
        result = cursor.fetchone()
        print(result['id'])
finally:
    connection.close()
#
# 'default': {
#     # 'ENGINE': 'django.db.backends.sqlite3',
#     # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     'ENGINE': 'django.db.backends.mysql',
#     'DB': 'dbzhb',
#     'HOST': '127.0.0.1',
#     'PORT': 12318,
#     'USER': 'zhb',
#     'PASSWORD': 'zuihuibao2015',
# }
