'implementation of the "unhook" command'

import andbug.command, andbug.screed

def find_eids(ctxt, expr):
  eids = list()
  emap = ctxt.sess.emap
  for e in emap:
    if expr in str(emap[e].origin):
      eids.append(e)

  for e in eids:
    print str(emap[e].origin)

  return eids

@andbug.command.action('<expr>', aliases=('uh',), name='unhook', shell=True)
def unhook(ctxt, expr=None):
  'remove hook'
  ctxt.sess.suspend()
  try:
    if not expr:
      with andbug.screed.section('remove all hook'):
        for eid in ctxt.sess.emap.keys():
          ctxt.sess.emap[eid].clear()
          #andbug.screed.item('Hook <%s> removed' % eid)
    else:
      eids = find_eids(ctxt, expr)
      for eid in eids:
        ctxt.sess.emap[eid].clear()
  finally:
    ctxt.sess.resume()
