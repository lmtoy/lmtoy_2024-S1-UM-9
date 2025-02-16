#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-UM-9"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["goods-n-130"] = \
 [-111610, 111611, 111612, 111614, 111615,-111616, 111618, 111619,
   111620, 111623, 111624, 111625,-111627, 111628, 111629, 111631,
   111632, 111633,
  -112388, 112389, 112390,
   116742, 116743, 116744, 116746, 116747, 116748,]

on["goods-n-14914"] = \
 [ 114470, 114471, 114472, 117193, 117194, 117195,-117197, 117198,
   117199, 117201, 117202, 117203, 117206, 117207, 117208, 117497,
   117498, 117499, 117501, 117502, 117503, 117505, 117506, 117507,]

on["goods-n-18911"] = \
 [ 126737, 126738, 126739,
   127242, 127243, 127244, 127246, 127247, 127248, 127250, 127251, 
   127252, 127256, 127257, 127258, 127260, 127261, 127262,]

on["goods-n-2592"] = \
 [ 112392, 112393, 112394, 112397, 112398, 112399, 112401, 112402,
   112403, 113225, 113226, 113227, 113887, 113888, 113889, 113891,
   113892, 113893, 113895, 113896, 113897, 114466,]

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}

pars1["goods-n-130"]   = "speczoom=89,4 badcb=0/5"
pars1["goods-n-14914"] = ""
pars1["goods-n-18911"] = ""
pars1["goods-n-2592"]  = ""
#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}

pars2["goods-n-130"]   = ""
pars2["goods-n-14914"] = ""
pars2["goods-n-18911"] = ""
pars2["goods-n-2592"]  = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, None, sys.argv)
