import sys, getopt, io
import requests
import json, csv
import urllib.request
import plotext as ptt
import uniplot as uni
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as dts
from matplotlib.dates import DateFormatter




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
        for i in range(0, len(time)):
            time[i]
        print(time)
        return time
    
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
        ptt.plot(y,line_color='red')
        ptt.plot(listofzeros,line_color='green')
        ptt.grid(True)
        ptt.canvas_color("black")
        ptt.axes_color("black")
        ptt.ticks_color("cloud")
        ptt.show()
        print(str(y[-1]))
        print(str(x[-1]))

    def set_uni(self, earnings, times):
        y = earnings
        x = times
        uni.plot(ys=y,lines=1) 
        print("Last Entry: ")
        print(str(y[-1]))
        print(str(x[-1]))

    def set_matplot(self, data, times):
        # plt.plot(data)
        # plt.show()

        # dates=times
        # values=data
        # plt.plot(dates, values, '-o')
        # plt.show()

        ax =plt.plot_date(x=times, y=data, fmt="r-")
        plt.title("Page impressions on example.com")
        plt.ylabel("Page impressions")
        plt.grid(True)
        plt.xticks(rotation=90)
        date_form = DateFormatter("%m-%d")
        plt.show()
