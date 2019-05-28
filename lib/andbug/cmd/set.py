'implementation of the "set" command'

import andbug.command, andbug.options, andbug.util

@andbug.command.action('<field> <value> [method]', name="set", aliases=('s',), shell=True)
def locals(ctxt, field, value):
  'set a field to value'
  t = andbug.util.cur_thread
  d = []

  for f in t.frames:
    if f.native:
      continue
    if f.value(field) is not None:
      d.append(f)

  if len(d) == 0:
    andbug.screed.item("!! no method with %s field name found\n" % field)
  elif len(d) == 1:
    d[0].setValue(field, value)
    andbug.screed.item("%s : %s = %s\n" %(d[0].loc, field, value))
  elif len(d) > 1:
    andbug.screed.item("!! multiple methods with %s field name\n" % field)
    for f in d:
      andbug.screed.item("\t%s\n" % (f))

