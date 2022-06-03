import random
import time
from typing import Dict
from PySide6.QtCore import QThread, Signal
import cache
import handle_premise
import puco_type
import constant
import value_handle


class AIThread(QThread):

    status_signal = Signal(str)
    target_signal = Signal(str)

    def __init__(self):
        """ ai线程 """
        super(AIThread,self).__init__()

    def run(self):
        """ 查询噗可可用目标活动并执行 """
        while 1:
            premise_data = {}
            targe_weight_data = {}
            target, _, judge = search_target(list(cache.config_target.keys()),set(),premise_data,targe_weight_data)
            if judge:
                self.target_signal.emit(target)
            else:
                self.status_signal.emit(constant.PucoStatus.STATUS_ARDER)
            time.sleep(1)


def search_target(
    target_list:list,
    null_target:set,
    premise_data:Dict[str,int],
    target_weight_data:Dict[int,int]
) -> (int,int,bool):
    """
    查找可用目标
    Keyword arguments:
    target_list -- 检索的目标列表
    null_target -- 被排除的目标集合
    premise_data -- 已算出权重的前提列表
    target_weight_data -- 已算出权重的目标列表
    Return arguments:
    int -- 目标id
    int -- 目标权重
    bool -- 前提是否能够被满足
    """
    target_data = {}
    for target in target_list:
        if target in null_target:
            continue
        if target in target_weight_data:
            target_data.setdefault(target_weight_data[target], set())
            target_data[target_weight_data[target]].add(target)
            continue
        target_config = cache_config.config_target[target]
        if not len(target_config.premise):
            target_data.setdefault(1, set())
            target_data[1].add(target)
            target_weight_data[target] = 1
            continue
        now_weight = 0
        now_target_pass_judge = 0
        now_target_data = {}
        premise_judge = 1
        for premise in target_config.premise:
            premise_judge = 0
            if premise in premise_data:
                premise_judge = premise_data[premise]
            else:
                premise_judge = handle_premise.handle_premise(premise)
                premise_judge = max(premise_judge, 0)
                premise_data[premise] = premise_judge
            if premise_judge:
                now_weight += premise_judge
            else:
                if premise in cache.config_effect_target_data and premise not in premise_data:
                    now_target_list = cache.config_effect_target_data[premise] - null_target
                    now_target, now_target_weight, now_judge = search_target(
                        now_target_list,
                        null_target,
                        premise_data,
                        target_weight_data,
                    )
                    if now_judge:
                        now_target_data.setdefault(now_target_weight, set())
                        now_target_data[now_target_weight].add(now_target)
                        now_weight += now_target_weight
                    else:
                        now_target_pass_judge = 1
                        break
                else:
                    now_target_pass_judge = 1
                    break
        if now_target_pass_judge:
            null_target.add(target)
            target_weight_data[target] = 0
            continue
        if premise_judge:
            target_data.setdefault(now_weight, set())
            target_data[now_weight].add(target)
            target_weight_data[target] = now_weight
        else:
            now_value_weight = value_handle.get_rand_value_for_value_region(now_target_data.keys())
            target_data.setdefault(now_weight, set())
            target_data[now_weight].add(random.choice(list(now_target_data[now_value_weight])))
    if target_data:
        value_weight = value_handle.get_rand_value_for_value_region(target_data.keys())
        return random.choice(list(target_data[value_weight])), value_weight, 1
    return "", 0, 0
