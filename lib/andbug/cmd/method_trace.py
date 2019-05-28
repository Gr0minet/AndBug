## Copyright 2011, IOActive, Inc. All rights reserved.
##
## AndBug is free software: you can redistribute it and/or modify it under 
## the terms of version 3 of the GNU Lesser General Public License as 
## published by the Free Software Foundation.
##
## AndBug is distributed in the hope that it will be useful, but WITHOUT ANY
## WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
## FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for 
## more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with AndBug.  If not, see <http://www.gnu.org/licenses/>.

'implementation of the "mtrace" command'

import andbug.command, andbug.screed, andbug.options, andbug.util
from Queue import Queue

def report_hit(t):
    t = t[0]
    t = andbug.util.cur_thread
    logfile = "./logs"
    try:
        if andbug.util.stepmode_enabled:
            t.sess.suspend()
        #with andbug.screed.section("trace %s" % t):
        f = t.frames[0]
        name = str(f.loc)
        if f.native:
            name += ' <native>'
        with open(logfile, 'a') as logf:
            logf.write(name + '\n')
            for k, v in f.values.items():
                logf.write( "\t%s=%s\n" %(k, v))

        #andbug.screed.item(name)
    finally:
        t.resume()

def cmd_hook_methods(ctxt, cpath, mpath, verbose=False):
    for c in ctxt.sess.classes(cpath):
        for m in c.methods(mpath):
            l = m.firstLoc
            if l.native:
                andbug.screed.item('Could not hook native %s' % l)
                continue
            l.hook(func = report_hit)
            if verbose:
                andbug.screed.item('Hooked %s' % l)

@andbug.command.action(
    '<method>', name='method-trace', aliases=('mt','mtrace'), shell=True
)
def method_trace(ctxt, mpath):
    'reports calls to specific dalvik method'
	
    cpath, mname, mjni = andbug.options.parse_mquery(".".join(mpath.split('.')[0:-1]),  mpath.split('.')[-1])

    #with andbug.screed.section('Setting Hooks'):
    cmd_hook_methods(ctxt, cpath, mname)

    #ctxt.block_exit()
