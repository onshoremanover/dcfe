import sys, getopt, io
import requests
import json, csv
import urllib.request
import plotext as plt
import numpy as np
from datetime import datetime

class My_DcTracker_Class():
    """NAME
        My_DcTracker_Class - A Class to display a current figure of dc prices by using a requests function.

        """


    def __init__(self, argu):
        self.argu = argu
        self.url = argu['url']
        self.currency = argu['currency']
        self.comission = argu['comission']
        self.coinvalue = argu['coinvalue']
        self.coinamount = argu['coinamount']
        

    def __str__(self):
        pass

    def __eq__(self, other):
        pass

    def set_request(self):
        """ Requests the data and exports it as a json file. """
        req_data = requests.get(self.argu['url'])
        return req_data.json()

    def set_prices_float(self, data):
        print(data)
        print(data[0]['currency'])
        prices = data[0]['prices']
        for i in range(0, len(prices)): 
            prices[i] = float(prices[i])
        print(prices)
        return prices

    def set_times(self, data):
        time = data[0]['timestamps']
    
    def set_content(self, data):
        for i in range(0, len(data)):
            EBKV = self.coinamount*data[i] 
            EBV = EBKV*(1-self.comission)
            data[i] = EBV-self.coinvalue
        print(" ")
        print(" ")
        print(" ")
        print(data)
        return data

    def set_plot(self, earnings, times):
        y = earnings
        x = times
        listofzeros = [0] * len(earnings)
        plt.plot(y,line_color='red')
        plt.plot(listofzeros,line_color='green')
        plt.ylim(-600, 600)
        plt.grid(True)
        plt.canvas_color("black")
        plt.axes_color("black")
        plt.ticks_color("cloud")
        plt.show()
