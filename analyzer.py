"""
@file:analyzer.py
@desc:Construct Dataset from a directory of samples
@author:notarbart
@license:MIT or UAYSF
"""
import os
import pedump
import pandas as pd

#globals
directory = 'samples/zippedMalware/'
samples = os.listdir(directory)
#write PE Information 

dataset = {}
def pe2vec():
    """
    dirty function (handling all exceptions) for each sample
    it construct a dictionary of dictionaries in the format:
        sample x : pe informations
    PEFile fails to parse some files gonna try to fix it
    """
    for i in range(0,len(samples)):
        try:
            pe = pedump.PEFile(directory+samples[i])
            dataset['sample'+str(i)] = pe.Construct()
        except:
            pass

#now that we have a dictionary let's put it in a clean csv file
def vec2csv(dataset):
    df = pd.DataFrame(dataset)
    df.transpose() #transpose to have the features as rows 
    #utf-8 is prefered from what i've seen
    df.to_csv('dataset.csv',sep=',',encoding='utf-8')

