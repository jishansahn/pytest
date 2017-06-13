import pymysql.cursors
import xlrd

connection = pymysql.connect(host='127.0.0.1',
                             port=12315,
                             user='jishanshan',
                             password='jishanshan',
                             db='dbzhb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     # sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id,
    #     # create_time) VALUES ("alen",18800110001,"alen@mail.com",0,1,NOW());'
    #     sql = ''
    #     cursor.execute(sql)
    #     # connection is not autocommit by default. So you must commit to save
    #     # your changes.
    #     connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        f = xlrd.open_workbook('./frame_list.xlsx')
        table = f.sheets()[1]
        for i in range(table.nrows):
            user_id=table.cell(i,0).value
            target_premium=int(table.cell(i,1).value)
            sql = "select sum(premium) as total_premium from user_order_all where status=7 and underwrite_time>='2016-10-29 00:00:00' and underwrite_time<'2016-12-01 00:00:00' and user_id=%s"
            cursor.execute(sql,(user_id,))
            result = cursor.fetchone()
            if result['total_premium'] is not None:
                if result['total_premium'] >= target_premium:
                    sql2 = "select sum(premium) as total_premium from user_order_all where status=7 and underwrite_time>='2016-11-01 00:00:00' and underwrite_time<'2016-12-01 00:00:00' and user_id=%s"
                    cursor.execute(sql2, (user_id,))
                    result2=cursor.fetchone()
                    # print("user_id:", user_id, "premium:", result2['total_premium'])
                    if result2['total_premium'] is not None:
                        if result2['total_premium']<target_premium:
                            # print("yes")
                            print("user_id,",user_id,",",result['total_premium'],",",result2['total_premium'])
                    else:
                        print("user_id,",user_id,",",result['total_premium'])
            # else:
            #     print("user_id,",user_id)
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
