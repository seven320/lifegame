import sys,os
import gui
import core
import argparse

#この部分で定義
parser = argparse.ArgumentParser()
parser.add_argument("-gui","--gui", help="run core with gui",
action='store_true')
args = parser.parse_args()

#with gui
if args.gui:
    gui.main()
else:
    core.main()
