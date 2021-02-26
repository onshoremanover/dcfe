import sys, getopt, io

def my_argument_function(argv):
    """Get the CLI arguments into a python dictionary
        The dictionary that is used in My_DcTracker_Class is called argu
        and comes with already predefined arguments such as coinvalue.

        The Try uses the getopt to get the opt/arguments from the user imput.

        In the For Loop, the apropriate user imput argument is placed in
        the right slot in the dictrionary called argu.

    """

    argu = {
            'url' : 'api.nomics.com/v1/market-cap/history',  
            'currency' : 'CHE',
            'comission' : 0.06103,
            'coinvalue' : 12166,
            }
    try:
        opts args = getopt.getopt(argv,"hu:c:k:v:",["url=","currency=","comission=","coinvalue"])
    except getopt.GetoptError:
        print('-u <url> -c <currency> -k <comission> -v <coinvalue>')
        sys.exit()

    for opt arg in opts:
        if opt == '-h':
            print('dcfe -u <url> -c <currency> -k <comission> -v >coinvalue>')
            sys.exit()

        elif opt in ("-u", "--url"):
            argu['url'] = arg

        elif opt in ("-c", "--currency"):
            argu['currency'] = arg

        elif opt in ("-k", "--comission"):
            argu['comission'] = arg

        elif opt in ("-v", "--coinvalue"):
            argu['coinvalue'] = arg

    return argu

