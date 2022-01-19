from uuid import uuid4
import time
for i in range(120):
  uuid = str(uuid4())
  f = open("{}.txt".format(uuid), "a")
  f.write("Now the file has more content! {}".format(uuid))
  f.close()