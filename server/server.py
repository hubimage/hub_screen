# from hub_screen.app.pyserver import model_run, path_enums, path_list, path_join, model_init, get_service,receive_img,get_stream,parse_stream
from hub_screen.app import pyserver_ext as psver
import time
from hub_screen.app import pyserver
pyserver.__debug__console__ = True
pyserver.console_log('dddd')
pyserver.__debug__console__ = False
try:
    for obj, predict in psver.model_run("./config_server.yaml"):
        # print(obj, predict)
        try:
            time.sleep(1)
#             # 从文件读取坐标
            with open("coordinates.txt", "r") as f:
                lines = f.readlines()
                # print(lines)
#             # 裁剪每个区域
            for i, line in psver.model.path_enums(lines):
                left, top, right, bottom = map(int, line.strip().split(','))
                cropped = obj.crop((left, top, right, bottom))
                cropped.save(f"./rec_img/region_{i}.png")
#
            result_dict = {}
            # try:
            for index, img_path in psver.model.path_enums(psver.model.path_list("./rec_img")):
                result = predict(psver.model.path_join(("./rec_img", img_path)))
                result_dict[index] = result[0][0]
            print(result_dict)
            # except Exception as e:
            #     print(e)
        except Exception as e:
            print("parse_err", e)
except Exception as e:
    print(e)

input("无需执行下面的代码。。。。。")

