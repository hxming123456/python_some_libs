# -*- coding: UTF-8 -*-
import os.path
import shutil
import json
import fnmatch
import file_operate

def list_folder_contents(path_name,path_dirt):
    pathlist = os.listdir(path_name)
    item = ''

    for i, item in enumerate(pathlist):
        if isDir(getJoinpath(path_name,item)):
            path_name = getJoinpath(path_name,item)
            path_dirt[str(item)] = {}
            list_folder_contents(path_name,path_dirt[item])
            path_name = '\\'.join(path_name.split('\\')[:-1])
        else:
            path_dirt[str(item)]='file'

def getJoinpath(path_name,dire_name):
    return os.path.join(path_name,dire_name)

def isDir(path_name):
    if os.path.isdir(path_name):
        return True
    else:
        return False

def getjson(dict):
    return json.dumps(dict,ensure_ascii=False,indent=4)

def new_folder(path_name,dir_name):                                  #创建目录
    try:
        isExists = os.path.exists(os.path.join(path_name,dir_name))
        if not isExists:
            os.makedirs(os.path.join(path_name,dir_name))
            print '目录新建成功！'
            return True
        else:
            print '目录已存在！'
            return False
    except Exception:
        return False

def delete_folder(path_name):                                         #删除目录
    try:
        isExists = os.path.exists(os.path.join(path_name))
        if isExists:
            shutil.rmtree(os.path.join(path_name))
            print '目录删除成功！'
            return True
        else:
            print '目录不存在！'
            return False
    except Exception:
        return False

def find_file_from_directory(path_name, file_name):                   #从目录中寻找指定文件，返回文件的路径
    ret_path = ''

    try:
        for filename in os.listdir(path_name):
            fp = os.path.join(path_name, filename)
            if os.path.isfile(fp) and file_name in filename:
                # print fp
                return path_name
                # return fp
            elif os.path.isdir(fp):
                ret_path = find_file_from_directory(fp, file_name)
                if (ret_path != '') and (ret_path != None):
                    return ret_path
    except Exception:
        return False

def get_present_folder():                                          #获取当前的目录
    return os.path.abspath('.')

def chdir_new_folder(path_name):     #切换目录
    try:
        os.chdir(path_name)
        if get_present_folder() == path_name:
            return True
        else:
            return False
    except Exception:
        return False

def get_list_folder_json(path_name):                #遍历目录，生成对应的json数据
    path_dict = {}

    try:
        list_folder_contents(path_name, path_dict)
        #return getjson(path_dict)
        return path_dict
    except Exception:
        return False

def open_file_for_directory(path_name, open_way):                      #打开/创建文件
    fp = open(path_name, open_way)
    print '文件已创建！'
    return fp

def close_file_for_directory(file_fp):                                  #关闭文件
    file_fp.close()

def delete_file_for_directory(path_name, file_name):                    #删除目录下的某个文件
    isExists = os.path.exists(os.path.join(path_name, file_name))

    if isExists:
        os.remove(os.path.join(path_name, file_name))
        print '文件已删除！'
    else:
        print '文件不存在！'

def write_file_for_directory(file_fp, buf):                              #往文件写进内容
    file_fp.writelines(buf)


def clean_file_content(file_fp):
    file_fp.truncate()

def ispath(path_name):
    return os.path.exists(path_name)

if __name__ == '__main__':
    item = [" 'TBD/2202' "," '1'(!)   = '1' "," 'SMT'     "," 'STD2202'  "," '/' "]
    #file_operate.new_item_to_file('C:\Users\Administrator\Desktop\logic.txt',item,6)
    #print file_operate.check_file_info('C:\Users\Administrator\Desktop\logic.txt')


