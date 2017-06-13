import xlrd

model_url='https://www.zuihuibao.cn/yiiapp/car-info/query-model-info'

try:
    f = xlrd.open_workbook('./frame_list.xlsx')
    table=f.sheets()[0]
    print(table.nrows)
    for i in range(table.nrows):
        print(table.cell(i,0).value)

except Exception as e:
    print('exception:',e)




# frame_list=['LSGXE83L8FD087298','LGWEF4A58EF007053','LZWADAGA9F6118788','LGWEF4A58EF007053','LSVWL2184FN229274','LJDEAA298A0130242']
# try:
#     # read from file
#     f=open("./db_frame.txt",'r', encoding='utf-8',errors='ignore')
#         frame_list=f.readlines()
#         for frame_no in frame_list:
#             r3=s.post(model_url,{'frame_no':frame_no.strip()},verify=False)
#             raw_json=r3.json()
#             print(r3.status_code)
#
#             print(type(raw_json))
#             print(frame_no,'return_code:',raw_json['return_code'])
#             if raw_json['return_code']==0:
#                 print('length',len(raw_json['data']))
#
# finally:
#     f.close()

# url="http://www.baidu.com"
# response=requests.get(url)
# print(response.status_code)