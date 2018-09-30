import pandas as pd
import re

import codecs

def convert(file, in_enc="GBK", out_enc="UTF-8"):
    """
    该程序用于将目录下的文件从指定格式转换到指定格式，默认的是GBK转到utf-8
    :param file:    文件路径
    :param in_enc:  输入文件格式
    :param out_enc: 输出文件格式
    :return:
    """
    in_enc = in_enc.upper()
    out_enc = out_enc.upper()
    try:
        print("convert [ " + file.split('\\')[-1] + " ].....From " + in_enc + " --> " + out_enc )
        f = codecs.open(file, 'r', in_enc)
        new_content = f.read()
        codecs.open(file, 'w', out_enc).write(new_content)
    # print (f.read())
    except IOError as err:
        print("I/O error: {0}".format(err))

# ---------------------
#
# 本文来自 祥知道 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/humanking7/article/details/78501474?utm_source=copy
def filt(path_name):
    '''
    将kindle mate 导出的生词本转为纯净txt
    :param path_name: 文件路径
    :return: 空
    '''


    #获得路径名及后缀
    pathAndNameAndPostfix=re.split('\.',path_name)
    postfix=pathAndNameAndPostfix[-1]
    pathAndName=''
    for str in pathAndNameAndPostfix[:-2]:
        pathAndName+=str+'.'
    else:
        pathAndName+=pathAndNameAndPostfix[-2]
    print(pathAndName)
    print(postfix)

    #转换格式
    # convert(path_name,in_enc='unicode')

    data = pd.read_csv(path_name, sep='\n', header=None)
    # 去掉句子
    odd_number = [x for x in range(1, list(data.count().values)[0], 2)]  # list(data.count().values)[0]获取data行数
    data.drop(odd_number, inplace=True)
        # 提取括号中的单词原型
    patt = r'\W+'
    new_data = pd.DataFrame()
    new_data[0] = data[0].str.split(patt, expand=True)[2]
    new_data[1] = new_data[0].str.contains(r'[a-z]+')
    new_data = new_data[new_data[1].isin([True])]
    # 排序
    print(new_data.sort_values(by = 0 , inplace=True))

    #去重
    new_data.drop_duplicates(0, keep='first', inplace=True)
    new_data[0].to_csv(pathAndName+'_filted.'+postfix, encoding='utf-8', index=False)

# ---------------------11
#  本文来自 火羽 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/rwangnqian/article/details/79000134?utm_source=copy

if __name__ == '__main__':
    filt('kindle2016.12.6.txt')
    filt('kindle2018.9.29.txt')
