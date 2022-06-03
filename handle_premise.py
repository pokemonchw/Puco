from types import FunctionType
from functools import wraps
import cache


def add_premise(premise: str) -> FunctionType:
    """
    添加前提
    Keyword arguments:
    premise -- 前提id
    return arguments:
    FunctionType -- 前提处理函数对象
    """

    def decoraror(func):
        @wraps(func)
        def return_wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        cache.config_premise[premise] = return_wrapper
        return return_wrapper

    return decoraror


def handle_premise(premise: str) -> int:
    """
    调用前提id对应的前提处理函数
    Keyword arguments:
    premise -- 前提id
    Return arguments:
    int -- 前提权重
    """
    if premise in cache.config_premise:
        return cache.config_premise[premise]()
    return 0
