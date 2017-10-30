'''
Created on 29-Oct-2017

@author: linux
'''
import psutil
from time import sleep


def get_ram_usage():
    return psutil.virtual_memory()

def get_root_disk_usage():
    return psutil.disk_usage('/')

def get_home_disk_usage():
    return psutil.disk_usage('/home')

def print_system_stats(cpu_usage, ram_usage, root_disk_usage, home_disk_usage):
    print "i = %d" %i
    print "========================="
    print "CPU usage: %s " % cpu_usage
    print "ram usage --- total: %d, used: %d, free: %d" % (((float(ram_usage.total) / 1024) / 1024) / 1024, \
                                             ((float(ram_usage.used) / 1024) / 1024) / 1024, \
                                             ((float(ram_usage.free) / 1024) / 1024) / 1024)
    print "root disk --- total: %s, used: %s, free: %s" %(((float(root_disk_usage.total)/1024)/1024)/1024, \
                                            ((float(root_disk_usage.used)/1024)/1024)/1024, \
                                            ((float(root_disk_usage.free)/1024)/1024)/1024)
    print "home disk --- total: %s, used: %s, free: %s" %(((float(home_disk_usage.total)/1024)/1024)/1024, \
                                            ((float(home_disk_usage.used)/1024)/1024)/1024, \
                                            ((float(home_disk_usage.free)/1024)/1024)/1024)
    print "========================="
    
    
    
if __name__ == "__main__":
    print "Number of logical CPUs %d"  %psutil.cpu_count(True)
    print "Number of Physical CPUs %d"  %psutil.cpu_count(False)
    
    cpu_usages = 0
    free_ram = 0
    used_ram= 0
    free_root = 0
    used_root = 0
    free_home = 0
    used_home = 0
    for i in range(1, 61):
        cpu_usage = psutil.cpu_percent(1, False)
        cpu_usages += cpu_usage
        
        ram_usage = get_ram_usage() 
        free_ram += ((float(ram_usage.free) / 1024) / 1024) / 1024
        used_ram += ((float(ram_usage.used) / 1024) / 1024) / 1024
        
        root_disk_usage = get_root_disk_usage()
        free_root += ((float(root_disk_usage.free)/1024)/1024)/1024
        used_root += ((float(root_disk_usage.used)/1024)/1024)/1024
        
        home_disk_usage = get_home_disk_usage()
        free_home += ((float(home_disk_usage.free)/1024)/1024)/1024
        used_home += ((float(home_disk_usage.used)/1024)/1024)/1024
        
        print_system_stats(cpu_usage, ram_usage, root_disk_usage, home_disk_usage)
        
        sleep(5)
        if i==6 or i==12 or i==60:
            print "CPU avg usage: %s" %str(float(cpu_usages)/i)
            print "RAM avg usage: %s" %str(float(used_ram)/i)
            print "Root avg usage: %s" %str(float(used_root)/i)
            print "Home avg usage: %s" %str(float(used_home)/i)