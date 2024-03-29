#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-UM-9"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["goods-n-130"] = \
 [ -111610, 111611, 111612, 111614, 111615, -111616, 111618, 111619,
   111620, 111623, 111624, 111625, -111627, 111628, 111629, 111631,
   111632, 111633,
   -112388, 112389, 112390,]

on["goods-n-2592"] = \
 [ 112392, 112393, 112394, 112397, 112398, 112399, 112401, 112402,
   112403,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}

pars1["goods-n-130"] = "speczoom=89,4 badcb=0/5"
pars1["goods-n-2592"] = ""

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}

pars2["goods-n-130"] = ""
pars2["goods-n-2592"] = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, None, sys.argv)
