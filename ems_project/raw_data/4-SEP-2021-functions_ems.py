#!/usr/bin/env python
# coding: utf-8

# In[3]:


# DEMO OF WEAK TYPING in PYTHON
# int age = 4 <-strongly typed variables, declare type along with id
age = 4; # we CANNOT declare a type for variable age
print(age)
print(type(age))
age = ('calico','calico','himalyian')
print(age)
print(type(age))


# # Allegheny county EMS dispatch analysis

# In[ ]:


# HIGH LEVEL GOAL:
# Source: WPRDC Data set on EMS/Fire dispatch via
# https://data.wprdc.org/dataset/allegheny-county-911-dispatches-ems-and-fire/resource/ff33ca18-2e0c-4cb5-bdcd-60a5dc3c0418?view_id=5007870f-c48b-4849-bb25-3e46c37f2dc7
# Determine the rate of redacted call descriptions across 
# EMS dispatches
# Has the rate of redaction changed year over year?
# if so, how?
# TODO: download CSV file from WPRDC into a raw data directory
# Review the fields in the file on WPRDC




# In[ ]:


# Raw input: CSV file containing a header row of column names
# and 1 or more rows, each row representing a single EMS dispatch
# in Allegheny County in year X


# In[ ]:



def iterate_EMS_records(file_path):
    '''
    Retrieve each record from a CSV of EMS records from the filepath
    
    Intended for use with the WPRDC's record of EMS dispatches
    in Allegheny County and will provide a dictionary of each record
    for use by processing functions
    '''
    # Open file at filepath
    # Use for loop over each record
    


# In[ ]:


def test_for_redacted_description(ems_rec):
    '''
    Examine EMS dispatch record and look for redacted or blank
    descriptions
    '''


# In[ ]:


# Based on record check, increment count by year
def red_year_total(redaction_year):
    '''
    Maintains a dictionary of counts by year passed when called
    
    Assumes that each call corresponds with a single record
    in the EMS dispatch data set, so a call with input of '2019'
    means, add 1 to the 2019 total of redacted records
    '''
    


# In[ ]:


# Based on record check, write record ID to log file
def write_redacted_rec_to_log(ems_rec):
    '''
    Extract record ID and write to log file specific in global dict
    '''
    


# In[ ]:


def display_redaction_count_by_year(year_counts):
    '''
    Given a dictionary of year(key):['total','redactions']
    make a pretty output to the console
    '''
    


# In[ ]:


# Desired output
# 1) Dictionary of format: { year:count_of_removed_records}
# 2) Text file whose rows are the record IDs of EMS
#   dispatches whose description was removed/redacted

