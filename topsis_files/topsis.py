import numpy as np
import pandas as pd
from math import inf
import numbers
import sys

def main():
    n = len(sys.argv)
    if(n!=5):
        print("Incorrect number of arguments\n")
        return

    data= sys.argv[1]
    weights= sys.argv[2]
    impacts= sys.argv[3]
    score= sys.argv[4]

    data, weights, impacts= error_Handling(data,  weights, impacts, score)    

    weights = [eval(i) for i in weights]
 
    topsis(data, weights, impacts, score)

if __name__ == "__main__":
    main()


def topsis(data, weights, impacts, result):
    normalised = normalise_Data(data)
    normalised= assign_Weights(normalised, weights)
    vjpositive, vjnegative= calculate_VJs(normalised, impacts)
    sipositive, sinegative= calculate_SIs(normalised, vjpositive, vjnegative)
    # Appending new columns in dataset 
    for i in range(0, data.shape[0]):
        data.loc[i,"Topsis Score"]=  sinegative[i] / (sipositive[i] + sinegative[i])
    # calculating the rank according to topsis score
    data["Rank"] = data["Topsis Score"].rank(method ='max')
    print(data)
    data.to_csv(result, index= False)

#normalising the columns
def normalise_Data(data):
    root_sum_square= [0] * (data.shape[1])
    for i in range(1, data.shape[1]):
        sum=0
        for j in range(0, len(data.iloc[:,i])):
            sum+= pow(data.iloc[j,i] ,2)
        root_sum_square[i]= np.sqrt(sum)
    normalised = data.copy()
    for i in range(1, normalised.shape[1]):
        for j in range(0, len(normalised.iloc[:,i])):
            normalised.iloc[j,i]/= root_sum_square[i]
    return normalised

#assigning weights for columns
def assign_Weights(normalised, weights):
    for i in range(1, normalised.shape[1]):
        for j in range(0, len(normalised.iloc[:,i])):
            normalised.iloc[j,i]*= weights[i-1]
    return normalised

#calculating ideal best and ideal worst
def calculate_VJs(norm, impacts):
    vjpositive= [0] * (norm.shape[1]-1)
    vjnegative= [0] * (norm.shape[1]-1)
    for i in range(1, norm.shape[1]):
        if(impacts[i-1] == '+'):
            vjpositive[i-1]= -inf
            vjnegative[i-1]= inf
            for j in range(0, len(norm.iloc[:,i])):
                vjpositive[i-1]= max(vjpositive[i-1], norm.iloc[j,i])
                vjnegative[i-1]= min(vjnegative[i-1], norm.iloc[j,i])
        else:
            vjpositive[i-1]= inf
            vjnegative[i-1]= -inf
            for j in range(0, len(norm.iloc[:,i])):
                vjpositive[i-1]= min(vjpositive[i-1], norm.iloc[j,i])
                vjnegative[i-1]= max(vjnegative[i-1], norm.iloc[j,i])
    return vjpositive, vjnegative

# Calculating distances and Topsis score for each row
def calculate_SIs(norm, vjpos, vjneg):
    sipositive= [0] * (norm.shape[0])
    sinegative= [0] * (norm.shape[0])
    for i in range(0, norm.shape[0]):
        sum1=0
        sum2=0
        for j in range(1, norm.shape[1]):
            sum1+= pow(norm.iloc[i,j] -vjpos[j-1] ,2)
            sum2+= pow(norm.iloc[i,j] -vjneg[j-1] ,2)
        sipositive[i]= np.sqrt(sum1)
        sinegative[i]= np.sqrt(sum2)
    return sipositive, sinegative


def is_numeric(n):
    for i in range(0,len(n)-1):
        if isinstance(n[i], numbers.Real) == False :
            return False
    return True

#error handling
def error_Handling(data, weights, impacts, result):
    if(data.endswith('.csv') == False) :
        sys.exit("Only csv files permitted\n")
    try:
        data = pd.read_csv(data)
    except FileNotFoundError:
        print("File not Found: Wrong file or file path")
    else:
        col = data.shape[1]
        if(col < 3):
            sys.exit("input file must contain 3 or more columns\n")
        for i in range(1 , col):
            if(is_numeric(data.iloc[:,i]) == False):
                sys.exit("Data type should be numeric")
        if(weights.__contains__(',') == False):
            sys.exit("Weights must be separated by comma\n") 
        weights= weights.split(",")
        if(len(weights) != col-1):
            sys.exit(f"Specify {col-1} weights\n")
        if(impacts.__contains__(',') == False):
            sys.exit("Impacts must be separated by comma\n") 
        impacts =impacts.split(",")
        if(len(impacts) != col-1):
            sys.exit(f"Specify {col-1} impacts\n")
        if set(impacts) != {'+', '-'}:
            sys.exit("Only '+', '-' impacts are allowed\n")
        if(result.endswith('.csv') == False) :
            sys.exit("Only csv files permitted\n")
        return data, weights, impacts

