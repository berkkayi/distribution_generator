import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

import warnings

warnings.filterwarnings( "ignore" )

def distirbution_generator(data, size, dist_list, verbose=False, print_limit=10,int_type=False):
    list_of_dists = dist_list
    sc = StandardScaler()
    data = data.reshape( -1, 1 )
    y_std = sc.fit_transform( data )
    y_std = y_std.flatten()
    results = []
    for i in list_of_dists:
        dist = getattr( stats, i )
        param = dist.fit( y_std )
        a = stats.kstest( y_std, i, args=param )
        results.append( (i, a[0], a[1]) )

    results.sort( key=lambda x: float( x[2] ), reverse=True )
    if verbose == True:
        for j in results[:print_limit]:
            print( "{}: statistic={}, pvalue={}".format( j[0], j[1], j[2] ) )
        dist = getattr( stats, f"{results[0][0]}" )
        param = dist.fit( y_std )
        print( "--------------------------------------\n" )
        print( f"best distirbution :{results[0][0]}" )
        print( "parameters result is (*hyperparameters...,mean,std) " )
        print( "best distirbution params :", param )
        print( "--------------------------------------\n" )
        print("random dataset :")
        print( "--------------------------------------\n" )
    else:
        dist = getattr( stats, f"{results[0][0]}" )
        param = dist.fit( y_std )

    random_data = dist.rvs( *param[0:-2], loc=param[-2], scale=param[-1], size=size )
    random_data = sc.inverse_transform( random_data )
    if int_type == True:
        random_data = random_data.astype(int)

    return random_data



