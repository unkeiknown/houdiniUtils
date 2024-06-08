#!/bin/bash

for filename in /mnt/nas/lib/tutorials/houdini/REBELWAY/PythonForProduction/work/test_objs/*.obj; do
    hython script.py "/mnt/nas/lib/tutorials/houdini/REBELWAY/PythonForProduction/work/pfp_week4_006_v01.hip" "$filename"
done



