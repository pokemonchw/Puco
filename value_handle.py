import math
import random
import itertools
import bisect
from typing import Dict, List


def get_rand_value_for_value_region(value_list: List[int]) -> int:
    """
    以列表中每个元素的值作为权重随机获取一个元素
    Keyword arguments:
    value_list -- 要计算的列表
    Return arguments:
    int -- 获得的元素
    """
    key_list = [math.ceil(i) for i in value_list]
    now_data = dict(zip(itertools.accumulate(key_list),value_list))
    weight_max = sum(key_list)
    weiget_region_list = list(now_data.keys())
    now_weight = random.randint(0,weight_max-1)
    weiget_region = get_next_value_for_list(now_weight,weiget_region_list)
    return now_data[weiget_region]


def get_next_value_for_list(now_int: int,int_list:List[int]) -> int:
    """
    获取列表中第一个比指定值大的数
    Keyword arguments:
    now_int -- 作为获取参考的指定数值
    int_list -- 用于取值的列表
    """
    now_id = bisect.bisect_left(int_list,now_int)
    return int_list[now_id]
