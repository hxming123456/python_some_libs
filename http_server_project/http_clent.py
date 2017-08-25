import httplib
import sys
import urllib
import json

http_server = ('127.0.0.1',80)

param = json.dumps(["newitem","C:\Users\Administrator\Desktop\logic.txt",[" 'TBD/0905' "," '1'(!)   = '1' "," 'SMT'     "," 'STD0905'  "," '/' "],3])

heads = {'Content-Type':'json','Content-Length':'%s'%(len(param))}


connect = httplib.HTTPConnection('127.0.0.1',80)
connect.request('HOST','/',param,heads)
rsp = connect.getresponse()

json =  rsp.read()
print json
connect.close()

