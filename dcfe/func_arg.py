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
            'url' : 'https://api.nomics.com/v1/currencies/sparkline?key=6ac1de3c9ef25232936d8d43fe0cb35c&ids=DOGE&start=2021-02-09T00%3A00%3A00Z&convert=CHF',
            'currency' : 'CHF',
            'comission' : 0.06103,
            'coinvalue' : 1000,
            'coinamount' : 12166
            }
    try:
        opts, args = getopt.getopt(argv,"hu:c:k:v:a:",["url=","currency=","comission=","coinvalue=","coinamount="])
    except getopt.GetoptError:
        print('-u <url> -c <currency> -k <comission> -v <coinvalue> -a <coinamount>')
        sys.exit()

    for opt, arg in opts:
        if opt == '-h':
            print('dcfe -u <url> -c <currency> -k <comission> -v <coinvalue> -a <coinamount>')
            sys.exit()

        elif opt in ("-u", "--url"):
            argu['url'] = arg

        elif opt in ("-c", "--currency"):
            argu['currency'] = arg

        elif opt in ("-k", "--comission"):
            argu['comission'] = arg

        elif opt in ("-v", "--coinvalue"):
            argu['coinvalue'] = arg

        elif opt in ("-a", "--coinamount"):
            argu['coinamount'] = arg

    return argu

