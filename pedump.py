"""
@file:pedump.py
@desc:prepares the dataset by parsing pe files and storing information
        into csv files
@author:piratemad
@license:MIT or UAYSF (use as you see fit)
"""
# imports
import os
import pefile

# File class


class PEFile:
    """
    This Class is constructed by parsing the pe file for the interesting features
    each pe file is an object by itself
    """

    def __init__(self, filename):
        self.pe = pefile.PE(filename, fast_load=True)
        self.filename = filename
        self.DebugSize = self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[6].Size
        self.DebugRVA = self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[
            6].VirtualAddress
        self.ImageVersion = self.pe.OPTIONAL_HEADER.MajorImageVersion
        self.OSVersion = self.pe.OPTIONAL_HEADER.MajorOperatingSystemVersion
       # self.ImportRVA = self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[1].VirtualAddress
        self.ExportRVA = self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[
            0].VirtualAddress
        self.ExportSize = self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[0].Size
        self.IATRVA = self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[12].VirtualAddress
        self.ResSize = self.pe.OPTIONAL_HEADER.DATA_DIRECTORY[2].Size
        self.LinkerVersion = self.pe.OPTIONAL_HEADER.MajorLinkerVersion
        self.NumberOfSections = self.pe.FILE_HEADER.NumberOfSections
        self.StackReserveSize = self.pe.OPTIONAL_HEADER.SizeOfStackReserve
        self.Dll = self.pe.OPTIONAL_HEADER.DllCharacteristics

    def Construct(self):
        sample = {}
        for attr, k in self.__dict__.iteritems():
            if(attr != "pe"):
                sample[attr] = k
        return sample

    def ShowStats(self):
        print "---------------------------------"
        print "Debug Size : ", self.DebugSize
        print "Debug RVA : ", self.DebugRVA
        print "ImageVersion : ", self.ImageVersion
        print "OSVersion : ", self.OSVersion
        # print "Import RVA :", self.ImportRVA
        print "Export RVA :", self.ExportRVA
        print "Export Size: ", self.ExportSize
        print "IAT RVA: ", self.IATRVA
        print "Ressources Size :", self.ResSize
        print "Linker Version:", self.LinkerVersion
        print "Number of Sections:", self.NumberOfSections
        print "Size of Stack Reserve:", self.StackReserveSize
        print "Dll Characteristics:", self.Dll
        print "------------------------------------"
