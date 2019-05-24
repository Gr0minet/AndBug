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

'implementation of the "methods" command'

import andbug.command, andbug.options

def get_methods(ctxt, cpath, mquery=None):
    'lists the methods of a class'
    methods_list = list()
    cpath, mname, mjni = andbug.options.parse_mquery(cpath, mquery)
    title = "Methods " + ((cpath + "->" + mquery) if mquery else (cpath))
    #with andbug.screed.section(title):
    for m in ctxt.sess.classes(cpath).methods(name=mname, jni=mjni):
        #andbug.screed.item(str(m))
        methods_list.append(str(m))
    return methods_list

@andbug.command.action('<class-path> [<method-query>]')
def methods(ctxt, cpath, mquery=None):
    'lists the methods of a class'
    return get_methods(ctxt, cpath, mquery)
