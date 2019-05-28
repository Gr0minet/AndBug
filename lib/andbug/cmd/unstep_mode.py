'implementation of the "unstep_mode" command'

import andbug.command, andbug.screed, andbug.options, andbug.util
from classes import get_classes
from methods import get_methods
from method_trace import cmd_hook_methods

@andbug.command.action(
    '', name='unstep-mode', aliases=('usm','unstepmode'), shell=True
)
def step_mode(ctxt):
    'disable the step by step mode which pauses at each function call'
    andbug.util.stepmode_enabled = False
    print "stepmode: " + str(andbug.util.stepmode_enabled)
