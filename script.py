import sys
sys.path.append('./lib')

from time import sleep
from andbug import command
from andbug.cmd import method_trace

if len(sys.argv) != 2:
    print "usage: %s [pid]" % sys.argv[0]

pid = sys.argv[1]

command.load_commands()
ctxt = command.Context()
ctxt.set(pid)

act_classes = command.ACTION_MAP.get("classes")
classes = act_classes(ctxt, "fr.haruni")

act_methods = command.ACTION_MAP.get("methods")
act_hook = command.ACTION_MAP.get("method-trace")
cnt = 0
for cla in classes:
    #print cla
    methods = act_methods(ctxt, cla)
    for method in methods:
        act_hook(ctxt, method)
        cnt += 1

print "%d functions hooked!" % cnt
         
while True:
  sleep(3600) 

