import argparse
from core.colors import green, end,back,red
import argparse
import threading
import requests
import warnings
import core.config as mem
from core.exporter import exporter
from core.bruter import bruter
from core.utils import prepare_requests,grouped_parameters

warnings.filterwarnings('ignore') 
parser = argparse.ArgumentParser() # defines the parser
# Arguments that can be supplied

result=[]
killed_Urls=[]



parser.add_argument('-o', help='Path for text output file.', dest='text_file')
parser.add_argument('-t', help='Number of concurrent threads. (default: 5)', dest='threads', type=int, default=5)
parser.add_argument('-m', help='Environment mode . (default: linux)', dest='mode', type=str, default='L')
parser.add_argument('-i', help='Import target URLs from file.', dest='import_file', nargs='?', const=True)
parser.add_argument('-w', help='Wordlist file path.', dest='wordlist')
parser.add_argument('-c', help='Chunk size. The number of parameters to be sent at once', type=int, dest='chunks', default=250)
parser.add_argument('--disable-redirects', help='disable redirects', dest='disable_redirects', action='store_true')
args = parser.parse_args() # arguments to be parsed
mem.var = vars(args)


def narrower(request, param_groups):
    """
    takes a list of parameters and narrows it down to parameters that cause anomalies
    returns list
    """

   
    for params in param_groups:
       is_reflected= bruter(request,params)
       if is_reflected:
           print(request)
           print("*"*10)
           result.append(request,"\n")

def initialize(url,param_groups):
    """
    handles parameter finding process for a single request object
    """
    
    response=requester(url)   
    if type(response) != str:
        narrower(url, param_groups)
        
def requester(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1'
    }
 

    session=requests.Session()
    try:
        response = session.get(url,
            headers=headers,
            verify=False,
            allow_redirects=False,
            timeout=5
            )
        return response
    except Exception as e:
        return str(e)

def worker(url,param_groups):
    # Wrapper function for threading, calls initialize
    try:
        initialize(url,param_groups) 
    except Exception as e:
        return str(e)




def main():
    num_threads = mem.var['threads']
    thread_list = []
    if mem.var['wordlist']:
        param_groups = grouped_parameters(mem.var['wordlist'],mem.var['chunks'])
        while urls:
            for _ in range(num_threads):
                if urls:
                    u = urls.pop(0) 
                    thread = threading.Thread(target=worker, args=(u,param_groups))
                    thread_list.append(thread)


            for thread in thread_list:
                thread.start()


            for thread in thread_list:
                thread.join()

                thread_list = []  # Clear the thread_list after joining threads




if __name__ == '__main__':
    if not mem.var['text_file']:
        print("Please add output file")
        exit()
    if not mem.var['wordlist']:
        print("Please add wordlist of parameter ")
        exit()
        
    urls = prepare_requests(args)
    if len(urls) == 0:
        print("import_file has no any url")
        exit()
    else:
        print(f"count of urls:{green}{len(urls)}")

    main()

    if len(result) !=0:
        exporter(result)