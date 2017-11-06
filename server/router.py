'''
The free.dm Router daemon.
@author: Thomas Wanderer
'''

# free.dm Imports
from freedm.daemons import NodeDaemon
from freedm.data import SQLStore


class RouterDaemon(NodeDaemon):
    '''
    The free.dm Router manages a local router system OS.
    It connects and communicates with a free.dm Server.
    '''
    
    _role = 'router'
    
    _port = 4510