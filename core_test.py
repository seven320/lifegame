#encoding utf-8

import argparse

#この部分で定義
parser = argparse.ArgumentParser()

#
# parser.add_argument("echo", help="echo the string you use here")

#
parser.add_argument("-gui", help="run core with gui")

#この部分で構文解析
args = parser.parse_args()


#with gui
if args.gui:
    print("gui available")

#without gui
