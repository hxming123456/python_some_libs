# -*- coding: utf-8 -*-

data_list = []

def find_error():
    file = open('log.txt', 'a+')
    lines = file.readlines()
    old_data = ''
    data_cnt = 0
    for i in lines:
        if i[0:4] == 'data':
            data = i[5:]
            data_cnt += 1
            if data in data_list:
                print data
            else:
                data_list.append(data)

    print data_cnt
    file.close()

def find_ok():
    file = open('log.txt', 'a+')
    lines = file.readlines()
    old_data = ''
    data_cnt = 0
    for i in lines:
        if "download ok" in i:
            data_cnt += 1

    print data_cnt
    file.close()

def find_data_from_exl():
    csv_list = []
    data_list = []
    len = 0
    xls_file = open('data.csv', 'a+')
    csv_file = open('Sonoff 4CH_PSF-A04-GL_15000_2017-06-19.csv', 'a+')
    xls_lines = xls_file.readlines()
    csv_lines = csv_file.readlines()
    xls_file.close()
    csv_file.close()

    #for i in xls_lines:
    for j in csv_lines:
            csv_list.append(j[2:12])

    for i in xls_lines:
            data_list.append(i[0:10])

    print csv_list
    print data_list

    for i in xrange(80):
        for j in xrange(15000):
            if data_list[i] == csv_list[j]:
                print csv_list[j]
                len += 1

    print len

if __name__=='__main__':
    find_error()