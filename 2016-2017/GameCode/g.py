    # we are assumIng the grid will be a two dimensional array of booleans, true for empty and false for wall
from variables import *

grid = [[I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I],
        [I,o,o,o,o,o,o,o,o,o,o,o,o,I,I,o,o,o,o,o,o,o,o,o,o,o,o,I],
        [I,o,I,I,I,I,o,I,I,I,I,I,o,I,I,o,I,I,I,I,I,o,I,I,I,I,o,I],
        [I,O,I,I,I,I,o,I,I,I,I,I,o,I,I,o,I,I,I,I,I,o,I,I,I,I,O,I],
        [I,o,I,I,I,I,o,I,I,I,I,I,o,I,I,o,I,I,I,I,I,o,I,I,I,I,o,I],
        [I,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,I],
        [I,o,I,I,I,I,o,I,I,o,I,I,I,I,I,I,I,I,o,I,I,o,I,I,I,I,o,I],
        [I,o,I,I,I,I,o,I,I,o,I,I,I,I,I,I,I,I,o,I,I,o,I,I,I,I,o,I],
        [I,o,o,o,o,o,o,I,I,o,o,o,o,I,I,o,o,o,o,I,I,o,o,o,o,o,o,I],
        [I,I,I,I,I,I,o,I,I,I,I,I,e,I,I,e,I,I,I,I,I,o,I,I,I,I,I,I],
        [I,I,I,I,I,I,o,I,I,I,I,I,e,I,I,e,I,I,I,I,I,o,I,I,I,I,I,I],
        [I,I,I,I,I,I,o,I,I,e,e,e,e,e,e,e,e,e,e,I,I,o,I,I,I,I,I,I],
        [I,I,I,I,I,I,o,I,I,e,I,I,I,n,n,I,I,I,e,I,I,o,I,I,I,I,I,I],
        [I,I,I,I,I,I,o,I,I,e,I,n,n,n,n,n,n,I,e,I,I,o,I,I,I,I,I,I],
        [I,I,I,I,I,I,o,e,e,e,I,n,n,n,n,n,n,I,e,e,e,o,I,I,I,I,I,I],
        [I,I,I,I,I,I,o,I,I,e,I,n,n,n,n,n,n,I,e,I,I,o,I,I,I,I,I,I],
        [I,I,I,I,I,I,o,I,I,e,I,I,I,I,I,I,I,I,e,I,I,o,I,I,I,I,I,I],
        [I,I,I,I,I,I,o,I,I,e,e,e,e,e,e,e,e,e,e,I,I,o,I,I,I,I,I,I],
        [I,I,I,I,I,I,o,I,I,e,I,I,I,I,I,I,I,I,e,I,I,o,I,I,I,I,I,I],
        [I,I,I,I,I,I,o,I,I,e,I,I,I,I,I,I,I,I,e,I,I,o,I,I,I,I,I,I],
        [I,o,o,o,o,o,o,o,o,o,o,o,o,I,I,o,o,o,o,o,o,o,o,o,o,o,o,I],
        [I,o,I,I,I,I,o,I,I,I,I,I,o,I,I,o,I,I,I,I,I,o,I,I,I,I,o,I],
        [I,o,I,I,I,I,o,I,I,I,I,I,o,I,I,o,I,I,I,I,I,o,I,I,I,I,o,I],
        [I,O,o,o,I,I,o,o,o,o,o,o,o,e,e,o,o,o,o,o,o,o,I,I,o,o,O,I],
        [I,I,I,o,I,I,o,I,I,o,I,I,I,I,I,I,I,I,o,I,I,o,I,I,o,I,I,I],
        [I,I,I,o,I,I,o,I,I,o,I,I,I,I,I,I,I,I,o,I,I,o,I,I,o,I,I,I],
        [I,o,o,o,o,o,o,I,I,o,o,o,o,I,I,o,o,o,o,I,I,o,o,o,o,o,o,I],
        [I,o,I,I,I,I,I,I,I,I,I,I,o,I,I,o,I,I,I,I,I,I,I,I,I,I,o,I],
        [I,o,I,I,I,I,I,I,I,I,I,I,o,I,I,o,I,I,I,I,I,I,I,I,I,I,o,I],
        [I,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,I],
        [I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I,I]]
