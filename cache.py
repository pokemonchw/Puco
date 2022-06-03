from typing import Dict
from types import FunctionType
from PySide6.QtWidgets import QWidget
import puco_type
from puco import Puco

puco:Puco = None
""" 噗可对象 """
status_data:Dict[str,FunctionType] = {}
""" 状态处理函数仓库 """
status_machine_data:Dict[str,FunctionType] = {}
""" 状态机数据 """
config_target:Dict[str,puco_type.Target] = {}
""" 目标配置数据 """
config_premise:Dict[str,FunctionType] = {}
""" 前提配置数据 """
config_effect_target_data: Dict[str,set] = {}
""" 能够满足前提的目标列表 """
