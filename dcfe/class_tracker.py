import sys, getopt, io
import requests
import json, csv
import urllib.request
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
        

    def __str__(self):
        pass

    def __eq__(self, other):
        pass

    def set_request(self):
        """ Requests the data and exports it as a json file. """
        pass
        req_data = requests.get()
        return req_data.json()
    
    def set_content(self):
        pass
