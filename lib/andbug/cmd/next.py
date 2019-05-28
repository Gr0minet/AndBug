'implementation of the "next" command'

import andbug.command, andbug.screed, andbug.options, andbug.util
from classes import get_classes
from methods import get_methods
from method_trace import cmd_hook_methods

@andbug.command.action(
    '', name='next', aliases=('n','next'), shell=True
)
def step_mode(ctxt):
    'step in one time'
    if andbug.util.stepmode_enabled:
      ctxt.sess.resume()
