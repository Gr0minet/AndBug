'implementation of the "step_mode" command'

import andbug.command, andbug.screed, andbug.options, andbug.util
from classes import get_classes
from methods import get_methods
from method_trace import cmd_hook_methods

@andbug.command.action(
    '', name='step-mode', aliases=('sm','stepmode'), shell=True
)
def step_mode(ctxt):
    'enable the step by step mode which pauses at each function call'
    andbug.util.stepmode_enabled = True
    print "stepmode: " + str(andbug.util.stepmode_enabled)
