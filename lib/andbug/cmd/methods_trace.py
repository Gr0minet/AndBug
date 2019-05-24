
'implementation of the "mtrace" command'

import andbug.command, andbug.screed, andbug.options
from classes import get_classes
from methods import get_methods
from method_trace import cmd_hook_methods

@andbug.command.action(
    '<methods>', name='methods-trace', aliases=('mtst','mtstrace'), shell=True
)
def methods_trace(ctxt, expr=None):
    'reports calls to several dalvik method'
	
    class_list = get_classes(ctxt, expr)
    for cla in class_list:
        method_list = get_methods(ctxt, cla)
        for method in method_list:
            cpath, mname, mjni = andbug.options.parse_mquery(".".join(method.split('.')[0:-1]), method.split('.')[-1])
            cmd_hook_methods(ctxt, cpath, mname)
            #print(mname)

    #ctxt.block_exit()
