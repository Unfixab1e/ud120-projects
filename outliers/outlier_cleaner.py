#!/usr/bin/python

from operator import itemgetter

def outlierCleaner(predictions, ages, net_worths):
    
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    uncleaned_data = [0] * len(predictions)
    unsorted_data = [0] * len(predictions)
    error = [0] * len(predictions)
    print "Length Predictions: ", len(predictions)
    print "Length Ages: ", len(ages)
    print "Length Net Worths: ", len(net_worths)


    for i in range (len(ages)):
        error[i] = net_worths[i] - predictions[i]
        uncleaned_data[i] = (ages[i], net_worths[i], abs(error[i]))
        unsorted_data[i] = (ages[i], net_worths[i], abs(error[i]))
        

    
    uncleaned_data = sorted(unsorted_data, key=itemgetter(2), reverse=False)
        
    resultSize = len(predictions)* 0.9
    resultSize = int(resultSize) 
    print resultSize
    cleaned_data = [0] * resultSize
    
    for i in range (resultSize):
        cleaned_data[i] = (uncleaned_data[i][0], uncleaned_data[i][1], uncleaned_data[i][2])
    


    
    return cleaned_data

