from abc import ABCMeta, abstractmethod

#抽象クラス
def __init__(self):
    self.input = ""
    self.output = ""

class AbstractGenerator(metaclass=ABCMeta):
    @abstractmethod
    def set(self,input):
        self.input=input
        self.output=""
    @abstractmethod
    def get(self):
        return self.output
