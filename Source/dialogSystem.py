# cython: language_level=3
from .turnBasedBattleSystem import *

#视觉小说系统
class DialogSystem(linpg.DialogSystem):
    def __init__(self): super().__init__()
    #保存数据
    def save_process(self) -> None:
        #确保Save文件夹存在
        if not os.path.exists("Save"): os.makedirs("Save")
        #存档数据
        save_thread = linpg.SaveDataThread("Save/save.yaml",{
            "chapterType": self.chapterType,
            "chapterId": self.chapterId,
            "type": self.part,
            "id": self.dialogId,
            "dialog_options": self.dialog_options,
            "collection_name": self.collection_name
        })
        save_thread.start()
        save_thread.join()
        del save_thread
        #检查global.yaml配置文件
        if not os.path.exists("Save/global.yaml"):
            DataTmp = {"chapter_unlocked":1}
            linpg.saveConfig("Save/global.yaml",DataTmp)