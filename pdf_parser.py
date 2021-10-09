################################################################################
#                                                                              #
#   PDF parser                                                                 #
#     Convert a PDF document into a gigantic text blob                         #
#                                                                              #
################################################################################

import os
import pdftotext

class converter(fname):

    def __init__(self, fname):
        self.currentdir = 'something'
        self.inputpath = 'something'
        self.outputpath = 'something'
        self.inputfile = self.inputpath + fname + '.pdf'
        self.outputfile = self.outputpath + fname + '.txt'

    def convert(self):
        with open(self.inputfile, 'r') as infile:
            with open(self.outputfile, 'w+') as outfile:
                pdf = pdftotext.PDF(infile)

                contents = ''
                for page in pdf:
                    contents += page
                contents = contents.replace('/n', ' ')

                outfile.write(contents)
                outfile.close()
            infile.close()


# EOF
