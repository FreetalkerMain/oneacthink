from datetime import datetime

class log():
 def __init__(self):
  self.start()
 def start(self):
  while True:
   dt=datetime.now()
   d=dt.strftime('%Y%m%d%H%M%S')
   inp=str(input())
   with open("log",mode="a",encoding="utf-8")as f:
    	f.write(d+":"+inp+"\n")
log()
		
