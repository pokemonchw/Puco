class Target:

    def __init__(self):
        """ 目标类型 """
        self.uid: str = ""
        """ 目标唯一id """
        self.text: str = ""
        """ 目标描述 """
        self.state_machine_id: str = ""
        """ 执行的状态机id """
        self.premise: dict = {}
        """ 目标的前提集合 """
        self.effect: dict = {}
        """ 目标的效果集合 """
