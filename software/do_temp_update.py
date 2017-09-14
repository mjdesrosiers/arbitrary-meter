import os
import sys

cmds = ["export LD_LIBRARY_PATH=/usr/local/lib", "cd RF24/librf24-bbb/librf24/examples/"]


TEMPERATURE = int(sys.argv[1])
cmds.append("./update_temp {}".format(TEMPERATURE))

cmd = ";".join(cmds)

print(cmd)

os.system(cmd)