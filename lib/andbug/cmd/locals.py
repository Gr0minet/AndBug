'implementation of the "locals" command'

import andbug.command, andbug.options, andbug.util

@andbug.command.action('', name="locals", aliases=('l',), shell=True)
def locals(ctxt):
    'list the locals of a class'
    t = andbug.util.cur_thread

    for f in t.frames:
        name = str(f.loc)
        if f.native:
            name += ' <native>'
        andbug.screed.item(name)
        for k, v in f.values.items():
            andbug.screed.item( "\t%s=%s\n" %(k, v))
