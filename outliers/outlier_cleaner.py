#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    errors = [(i, abs(predictions[i]-net_worths[i])) for i in range(0,len(predictions))]
    maxErrors = sorted(errors, cmp=lambda x,y: cmp(x[1][0], y[1][0]))[-9:]
    maxErrorsIndexs = map(lambda x:x[0], maxErrors)
    # print 'predictions', predictions
    # print 'networth', net_worths
    print 'errors:', errors
    print 'maxErrors', maxErrors
    print 'maxErrorsIndexs', maxErrorsIndexs

    cleaned_data = [(ages[i][0], net_worths[i][0], errors[i][0]) for i in range(0, len(predictions)) if i not in maxErrorsIndexs]
    print 'data count:', len(cleaned_data)
    ### your code goes here

    
    return cleaned_data

