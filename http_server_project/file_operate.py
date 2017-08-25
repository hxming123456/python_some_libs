# -*- coding: UTF-8 -*-
import time
import json
import dire_operate

def file_info_to_json(data):                                                      #文件内容转为json数据
    file_json  = {"file_type":"","part":"","tag":[],"item":[]}
    begin = data.find("FILE_TYPE")
    file_json["file_type"] = data[begin:find_endindex('\n',data,begin)]
    begin = data.find("PART \'")
    file_json["part"] = data[begin:find_endindex('\n',data, begin)]
    begin = data.find("\n:")
    file_json["tag"] = get_tag_value_operate(data[begin+1:])
    begin = data.find('}\n ')
    print data[begin+2:]
    file_json['item'] = get_item_value_operate(data[begin+2:])

    return file_json

def check_file_info(file_name):                                                     #查看文件的信息，并返回
    try:
        fp = dire_operate.open_file_for_directory(file_name, 'r+')
        list = fp.read()
        dire_operate.close_file_for_directory(fp)
        #return dire_operate.getjson(file_info_to_json(list))
        return file_info_to_json(list)
    except Exception:
        return False

def new_item_to_file(file_name,item,item_number):                                   #在指定文件新建item项
    data = ''
    item_list = []
    file_dirt = {}

    try:
        fp = dire_operate.open_file_for_directory(file_name, 'a+')
        data = fp.read()

        file_dirt = file_info_to_json(data)
        file_dirt['item'] = insert_one_item_to_list(file_dirt['item'],item,item_number)

        json_to_file_info(file_name,dire_operate.getjson(file_dirt))
        dire_operate.close_file_for_directory(fp)

        return True
    except Exception:
        return False

def delete_item_to_file(file_name,item_number):                                     #在指定文件中删除item项
    data = ''
    item_list = []
    file_dirt = {}
    try:
        fp = dire_operate.open_file_for_directory(file_name, 'a+')
        data = fp.read()

        file_dirt = file_info_to_json(data)
        file_dirt['item'] = delete_one_item_to_list(file_dirt['item'],item_number)

        json_to_file_info(file_name,dire_operate.getjson(file_dirt))
        dire_operate.close_file_for_directory(fp)
        return True
    except Exception:
        return  False

def edit_item_to_file(file_name,item_list,item_number):                             #在指定文件中编辑item项
    data = ''
    file_dirt = {}
    try:
        fp = dire_operate.open_file_for_directory(file_name, 'a+')
        data = fp.read()

        file_dirt = file_info_to_json(data)
        file_dirt['item'] = edit_one_item_to_list(file_dirt['item'], item_list, item_number)

        json_to_file_info(file_name, dire_operate.getjson(file_dirt))
        dire_operate.close_file_for_directory(fp)
        return True
    except Exception:
        return False

def get_tag_value_operate(data):                                                    #获取文件中的tag项
    tag_list = []
    key_list = ['', '', '', '', '']
    line_old_index = 0
    line_new_index = 0
    old_index = 0
    new_index = 0
    j = 0

    while True:
        line_new_index = data[line_old_index:].find('\n')
        if data[line_old_index:line_new_index + line_old_index].find('{=') == -1:
            for i in xrange(5):
                print'i=' + str(i)
                if i == 4:
                    new_index = data[old_index:].find('\n')
                    key_list[i] = data[old_index:new_index + old_index]
                    old_index = new_index + old_index + 1
                else:
                    new_index = data[old_index:].find('|')
                    key_list[i] = data[old_index:new_index + old_index]
                    old_index = new_index + old_index + 1
                if key_list[0] != '':
                    tag_list.append(key_list[i])
            key_list = ['', '', '', '', '']
            line_old_index = line_new_index + line_old_index + 1
        else:
            return tag_list

def get_item_value_operate(data):                                                   #获取文件中的item项
    item_list = []
    key_list = ['','','','','']
    line_old_index = 0
    line_new_index = 0
    old_index = 0
    new_index = 0
    j = 0

    while True:
        line_new_index = data[line_old_index:].find('\n')
        if data[line_old_index:line_new_index+line_old_index].find('END_PART') == -1:
            for i in xrange(5):
                print'i='+str(i)
                if i == 4:
                    new_index = data[old_index:].find('\n')
                    key_list[i] = data[old_index:new_index + old_index]
                    print key_list[i]
                    old_index = new_index + old_index + 1
                else:
                    new_index = data[old_index:].find('|')
                    key_list[i] = data[old_index:new_index+old_index]
                    print key_list[i]
                    old_index = new_index+old_index+1
            if key_list[0] != '':
                item_list.append(key_list)
                print item_list
            key_list = ['', '', '', '', '']
            line_old_index = line_new_index + line_old_index+1
        else:
            return item_list

def find_endindex(index,data,begin):                                                    #找出下个目标项的位置，并返回
    end = 0
    while True:
        if data[begin+end] == index:
            break
        else:
            end += 1
    return end+begin

def json_tag_to_array(buf):                                                             #把tag项的json数据转为数组
    tmp = ''

    for i in xrange(5):
        tmp += buf[i]
        if i != 4:
            tmp += '|'
    return tmp

def json_item_to_array(buf):                                                            #把item项的json数据转为数组
    tmp = ''
    list_len = len(buf)
    for x in xrange(list_len):
        for i in xrange(5):
            tmp += buf[x][i]
            if i != 4:
                tmp += '|'
        tmp += '\n'

    return tmp

def insert_one_item_to_list(item_list,tmp_item,tmp_number):                             #往item项队列新建一个子项
    new_list = []

    new_list = item_list
    item_len = len(item_list)
    if item_len < tmp_number:
        tmp_number = item_len
    if tmp_item in item_list:
        return new_list
    else:
        new_list.insert(tmp_number,tmp_item)

    return new_list

def delete_one_item_to_list(item_list,tmp_item):                                        #删除item项队列中的子项
    new_list = []

    new_list = item_list
    list_len = len(item_list)
    if tmp_item <= list_len:
        del new_list[tmp_item]

    return new_list

def edit_one_item_to_list(item_list,tmp_item,tmp_number):                                #编辑item项队列的子项
    new_list = []

    new_list = item_list
    list_len = len(item_list)
    if tmp_number <= list_len:
        new_list[tmp_number] = tmp_item

    return new_list

def json_to_file_info(file_name,json_data):                                             #把json数据转为字符串并写进文件
    tmp = '{========================================================================================}\n'
    end = 'END_PART\n\nEND.'
    data = json.loads(json_data)
    item = ''
    tag = ''

    fp = dire_operate.open_file_for_directory(file_name,'w+')
    dire_operate.clean_file_content(fp)

    dire_operate.write_file_for_directory(fp,data['file_type']+'\n\n')
    dire_operate.write_file_for_directory(fp,data['part']+'\n\n')
    dire_operate.write_file_for_directory(fp,tmp)
    tag = json_tag_to_array(data['tag'])
    dire_operate.write_file_for_directory(fp, tag+'\n')
    dire_operate.write_file_for_directory(fp, tmp)
    item = json_item_to_array(data['item'])
    dire_operate.write_file_for_directory(fp, item)
    dire_operate.write_file_for_directory(fp, end)
    dire_operate.close_file_for_directory(fp)

if __name__ == '__main__':
    #json = {"item":[[1,2,3,4],[5,6,7,8]]}
    #json['item'].append([9,10,11,12])
    #print json['item']
 print