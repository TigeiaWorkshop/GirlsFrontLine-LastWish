from shutil import move as MOVE
from subprocess import check_call
from linpgtoolkit import Builder

# 编译游戏本体
Builder.delete_file_if_exist(r"Source_pyd")
Builder.delete_file_if_exist(r"src/Source/experimental")
Builder.compile("Source", ignore_key_words=("experimental",))
Builder.delete_file_if_exist(r"src/Source/__init__.py")
MOVE(r"src/Source", r"Source_pyd")
Builder.delete_file_if_exist(r"src")

# 确认是否想要打包
if input("Do you want to generate a package for the game(Y/n):") == "Y":
    # 更新所有第三方库
    Builder.update_all_site_packages()

    # 删除dist文件夹
    Builder.delete_file_if_exist("dist")

    # 打包main文件
    dev_mode = input("If for dev purpose:")
    if dev_mode.lower() == "y":
        check_call(["pyinstaller", "main.spec"])
    else:
        check_call(["pyinstaller", "--noconsole", "main.spec"])

    # 移除移除的缓存文件
    folders_need_remove: tuple[str] = ("build", "logs", "__pycache__", "Source_pyd")
    for folder_p in folders_need_remove:
        Builder.delete_file_if_exist(folder_p)
