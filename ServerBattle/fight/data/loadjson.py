import json
import os

from fight.utils.singleton import Singleton


@Singleton
class LoadJson:
    """
    加载Json类
    """
    def __init__(self):
        self.jsonFile = {}

    def getJsonPath(self):
        """
        获取Json文件夹地址
        """
        workpath = os.getcwd()
        jsonpath = workpath + "\\fight\\json"
        return jsonpath

    def getJsonNames(self):
        """
        获取Json文件夹所有文件名
        """
        return os.listdir(self.getJsonPath())

    def __loadJson(self, jsonName):
        """
        读取Json文件数据并储存
        """
        with open(self.getJsonPath() + "\\" + jsonName, "r") as f:
            j = json.load(f)
        self.jsonFile.update({jsonName: dict(j)})

    def loadJsons(self):
        """
        读取所有Json文件数据并储存
        """
        jsonNames = self.getJsonNames()
        for jsonName in jsonNames:
            self.__loadJson(jsonName)

    def get(self, sht: str, id, field: str):
        """获取指定Json的指定数据"""
        shtdata: dict = self.jsonFile.get(sht, [])
        iddata = dict(shtdata.get(id, []))
        keydata = iddata.get(field, None)
        return keydata
