import os

ret = os.system("nohup flask run &run.log&")
print(ret)
