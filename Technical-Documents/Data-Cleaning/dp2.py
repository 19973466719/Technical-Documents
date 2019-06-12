# coding: utf-8
# 筛选MAC地址中包含字母的信息
import xlrd
import xlwt
import os
import sys
import tkinter
import geoip2.database   #pip install geoip2 安装该模块
import re


def read(file, sheet_index=0):
    """
    :param file: 文件路径
    :param sheet_index: 读取的工作表索引
    :return: 二维数组
    """
    workbook1 = xlrd.open_workbook(file)
    # all_sheets_list = workbook.sheet_names()
    # print("本文件中所有的工作表名称:", all_sheets_list)
    # 按索引读取工作表
    sheet1 = workbook1.sheet_by_index(sheet_index)
    print("工作表名称:", sheet1.name)
    print("行数:", sheet1.nrows)
    print("列数:", sheet1.ncols)

    datas = []
    for j in range(0, sheet1.ncols):
        datas.append("".join(sheet1.row_values(0)[j]))
    count = 1
    try:
        for i in range(1, sheet1.nrows):
            if (sheet1.row_values(i)[21] != "" and '.' in sheet1.row_values(i)[21] and sheet1.row_values(i)[21] != '0.0.0.0' and re.search('[a-zA-Z]',sheet1.row_values(i)[23])):  #判断“ip地址”列不为空，并且不是0.0.0.0，并且mac地址中包含字母
                count += 1
                for j in range(0, 22):
                    datas.append("".join(sheet1.row_values(i)[j]))

                #判断ip地址归属地代码，并讲结果写入第22列
                gi = geoip2.database.Reader('./GeoLite2-City.mmdb')
                aim_ = gi.city(sheet1.row_values(i)[21])
                temp = str(aim_)
                #print(temp)  # 打印出归属地

                tr = temp.split('(')[1]
                info = tr.split(', [')[0]
                aim = eval(info)
                #print("aim:", aim)
                des = str(aim['subdivisions'][0]['names']['zh-CN']) + str(aim['city']['names']['zh-CN'])
                datas.append(des)

                for j in range(23, sheet1.ncols):
                    datas.append("".join(sheet1.row_values(i)[j]))
            else:
                continue
    except:
        print("Unexpected error:", sys.exc_info())# sys.exc_info()返回出错信息
        input('press enter key to exit') #这儿放一个等待输入是为了不让程序退出

    workbook2 = xlwt.Workbook()
    sheet2 = workbook2.add_sheet(u'MAC地址为非手机号码',cell_overwrite_ok=True) #创建sheet
    # 将结果保存到新的excel文件中
    for i in range(0, count):
        for j in range (0, sheet1.ncols):
            sheet2.write(i, j, datas[(i * sheet1.ncols)+j])
    workbook2.save(path_output)

    return datas

if __name__ == '__main__':

    path_input = input("请输入需要清洗的数据文件路径：")
    # input_flag = os.path.exists(path_input)
    while (True):
        input_flag = os.path.exists(path_input)
        if (input_flag):
            break
        else:
            path_input = input("请重新输入需要清洗的数据文件路径：")

    path_output = input("请输入保存清洗后文件的路径：")
    output_flag = os.path.exists(path_output)
    read(path_input)
