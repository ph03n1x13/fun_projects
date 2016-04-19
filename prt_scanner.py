import socket
from datetime import datetime

def scan_port(host, port):
    '''
    this function mainly scans whether a port of the host is open or not
    '''

    report = 1
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    res = skt.connect_ex((host, port))


    if res == 0:
        report = res
    skt.close()

    return report




def run_scanner(host):
    '''
    runs the scanning method under a loop contains int type port numbers
    '''

    st_port = 1
    end_port = 100

    for port in xrange(st_port, end_port+1):

        opn = scan_port(host, port)

        if opn == 0:
            print "[+]Port: %d   State: Open !\n " %port
        '''

        else:
            print "[-]Port: %d is closed\n " %port
        '''



host = raw_input("[*]enter host name: ")


hostIP = socket.gethostbyname(host)
print "\n[*]Host: %s Public IP: %s" % (host, hostIP)
print "port range 1 to 100\n"
print "\n\t[*]scanning started at: %s\n" % (datetime.now())
print "scanning for open ports wait......."

start = datetime.now()
run_scanner(host)
end = datetime.now()
tot_time = end - start


print "\n\n[*]total scanning time: %s " %tot_time





