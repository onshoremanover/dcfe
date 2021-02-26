#
#
#
#

import sys, getopt, io, re
import requests, logging, time
import json, csv

from .func_arg import my_argument_function
from .class_tracker import My_DcTracker_Class

def main():
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))

    for arg in args:
        print('passed argument :: {}'.format(arg))

    argu = my_argument_function(sys.argv[1:])

    my_object = My_DcTracker_Class(argu)
    

if __name__ == '__main__':
    main()


