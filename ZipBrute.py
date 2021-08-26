# Multi-Threaded ZIP files bruteforce tool
# calfcrusher@inventati.org
# Usage: ./ZipBrute.py -f file.zip -d wordlist.txt

import optparse
import threading
import zipfile
import time
import pyfiglet
import os
import psutil


def extractzip(zipfilepath, password, startedtime):
    """Extract zip file"""

    try:
        with zipfile.ZipFile(zipfilepath) as file:
            file.extractall(pwd=str.encode(password))
            print("[+] PASSWORD FOUND -> " + password)
            print("[+] Files extracted in current directory")
            print('It took {0:0.1f} seconds'.format(time.time() - startedtime))
            # Terminate process pid to kill all threads
            current_system_pid = os.getpid()
            terminator = psutil.Process(current_system_pid)
            terminator.terminate()
    except BaseException:
        pass


def main():
    """Main function of tool"""

    ascii_banner = pyfiglet.figlet_format("ZipBrute")
    print(ascii_banner)
    print("calfcrusher@inventati.org | For educational use only.")
    print("*****************************************************\n")

    start = time.time()

    parser = optparse.OptionParser("./ZipBrute.py -f <zipfile> -d <wordlist>")
    parser.add_option('-f', dest='filezip', type='string', help='specify zip file')
    parser.add_option('-d', dest='wordlist', type='string', help='specify dictionary file')

    (options, args) = parser.parse_args()

    if options.filezip is None or options.wordlist is None:
        print(parser.usage)
        exit(0)
    else:
        pathzip = options.filezip
        wordlist = options.wordlist

    if zipfile.is_zipfile(pathzip):
        print('running...')
        with open(wordlist) as wlist:
            for line in wlist.readlines():
                password = line.strip('\n')
                t = threading.Thread(target=extractzip, args=(pathzip, password, start))
                t.start()


if __name__ == '__main__':
    main()

print("No valid password found!")
