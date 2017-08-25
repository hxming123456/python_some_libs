from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os
import json
import dire_operate
import file_operate

class MyhttprequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        rootdir = 'C:\Users\Administrator\Desktop'
        try:
            #if self.path.endswith('.'):
                #f = open()
                #print self.path
                self.end_headers()
                self.send_response(200)
                self.send_header('Content-type','json')
                self.end_headers()

                #self.wfile.write(f.read())
                #f.close()
                return

        except IOError:
            self.send_error(404,'file not found')

    def do_HOST(self):
        status =  'HTTP/1.1 200 OK\r\n'
        data_len = 0
        rece_head = ''
        rece_data = ''
        send_data = []

        try:
            rece_head =  self.headers
            rece_data =  self.rfile.read(int(self.headers['Content-Length']))
            print rece_head
            print rece_data

            send_data = parsing_rece_data(rece_data)
            send = json.dumps(send_data)
            data_len = len(send)
            print data_len
            self.send_response(200)
            self.end_headers()
            head = [
                        'Content-Type: json',
                        'Content-Length: %d' % (data_len),
                        'Server: httpserver'
                    ]
            head_message = status + '\r\n'.join(head)
            self.wfile.write(head_message)
            self.wfile.write('\n\n')
            self.wfile.write(send)

            return
        except IOError:
            self.send_error(404,'file not found')

def parsing_rece_data(rece_data):
    data = json.loads(rece_data)
    ret = []

    if data[0] == 'mkdir':
        if dire_operate.new_folder(data[1],data[2]):
            ret.append('ret')
            ret.append(0)
        else:
            ret.append('ret')
            ret.append(1)
    elif data[0] == 'rmdir':
        if dire_operate.delete_folder(data[1]):
            ret.append('ret')
            ret.append(0)
        else:
            ret.append('ret')
            ret.append(1)
    elif data[0] == 'pwd':
        ret.append('pwd')
        ret.append(dire_operate.get_present_folder())
    elif data[0] == 'cddir':
        if dire_operate.chdir_new_folder(data[1]):
            ret.append('ret')
            ret.append(0)
        else:
            ret.append('ret')
            ret.append(1)
    elif data[0] == 'listdir':
        buf = dire_operate.get_list_folder_json(data[1])
        if buf != False:
            ret.append('ret')
            ret.append(buf)
        else:
            ret.append('ret')
            ret.append(1)
    elif data[0] == 'find_file':
        buf = dire_operate.find_file_from_directory(data[1],data[2])
        if buf != False:
            ret.append('ret')
            ret.append(buf)
        else:
            ret.append('ret')
            ret.append(1)
    elif data[0] == 'check_file':
        buf = file_operate.check_file_info(data[1])
        if buf != False:
            ret.append('ret')
            ret.append(buf)
        else:
            ret.append('ret')
            ret.append(1)
    elif data[0] == 'newitem':
        if file_operate.new_item_to_file(data[1],data[2],data[3]-1):
            ret.append('ret')
            ret.append(0)
        else:
            ret.append('ret')
            ret.append(1)
    elif data[0] == 'delitem':
        if file_operate.delete_item_to_file(data[1],data[2]-1):
            ret.append('ret')
            ret.append(0)
        else:
            ret.append('ret')
            ret.append(1)
    elif data[0] == 'edititem':
        if file_operate.edit_item_to_file(data[1],data[2],data[3]-1):
            ret.append('ret')
            ret.append(0)
        else:
            ret.append('ret')
            ret.append(1)
    else:
        return ["ret",0]

    return ret

def run():
    server_address = ('127.0.0.1',80)
    http = HTTPServer(server_address,MyhttprequestHandler)
    http.serve_forever()

if __name__ == '__main__':
    run()