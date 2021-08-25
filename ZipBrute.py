import optparse
import threading
import zipfile
import time
import pyfiglet


def extractzip(filezipobj, password):
    """Extract zip file"""

    try:
        filezipobj.extractall(pwd=password)
        print('[+] Password Found ' + password + '\n')
    except BaseException:
        pass


def main():
    """Main function of tool"""

    ascii_banner = pyfiglet.figlet_format("ZipBrute")
    print(ascii_banner)
    print("calfcrusher@inventati.org | For educational use only.")
    print("*****************************************************\n")

    parser = optparse.OptionParser("./ZipBrute.py -f <zipfile> -d <wordlist>")
    parser.add_option('-f', dest='filezip', type='string', help='specify zip file')
    parser.add_option('-d', dest='wordlist', type='string', help='specify dictionary file')

    (options, args) = parser.parse_args()

    if options.filezip is None or options.wordlist is None:
        print(parser.usage)
        exit(0)
    else:
        filezip = options.filezip
        wordlist = options.wordlist

    filezipobj = zipfile.ZipFile(filezip, 'r')
    wlist = open(wordlist)

    for line in wlist.readlines():
        password = line.strip('\n')
        t = threading.Thread(target=extractzip, args=(filezipobj, password))
        t.start()

    wlist.close()


if __name__ == '__main__':
    start = time.time()
    main()

print('It took {0:0.1f} seconds'.format(time.time() - start))
