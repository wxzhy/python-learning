import numpy as np
def studen(input_data,num):
    '''
    将ipnut_data转换成ndarray后筛选出大于num的元素组成新的ndarray并排序
    :param input_data: 测试用例，类型为list
    :param num: 测试用例，类型为int
    :return: result，类型为ndarray
    '''
    result=[]
    #********* Begin *********#
    result=np.array(input_data)
    result=result[np.where(result>num)]
    result.sort()
    #********* End *********#
    return  result
