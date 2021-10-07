################################################################################
#                                                                              #
#   PDF parser                                                                 #
#     Convert a PDF document into a gigantic text blob                         #
#                                                                              #
################################################################################

import os

class converter(fname):

    def __init__(self, fname):
        self.currentdir = 'something'
        self.inputpath = 'something'
        self.outputpath = 'somethong'
        self.inputfile = self.inputpath + fname + '.pdf'
        self.outputfile = self.outputpath + fname + '.txt'

    def convert(self):
        with open(self.inputfile, r) as infile:
            with open(self.outputfile, w+) as outfile:
                # Do the conversion


# EOF
