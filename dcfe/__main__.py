import sys, getopt, io, re
import requests, logging, time
import json, csv

from .class_tracker import My_DcTracker_Class
from .func_arg import my_argument_function

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))

    for arg in args:
        print('passed argument :: {}'.format(arg))

    argu = my_argument_function(sys.argv[1:])

    my_object = My_DcTracker_Class(argu)
    my_dict = my_object.set_request()
    my_prices_float = my_object.set_prices_float(my_dict)
    my_times = my_object.set_times(my_dict)
    my_earnings = my_object.set_content(my_prices_float)
    my_plot = my_object.set_plot(my_earnings, my_times)
    #print(my_plot)

if __name__ == '__main__':
    main()


