from uuid import uuid4
for i in range(100000):
  uuid = str(uuid4())
  f = open("{}.txt".format(uuid), "a")
  f.write("Now the file has more content! {}".format(uuid))
  f.close()
