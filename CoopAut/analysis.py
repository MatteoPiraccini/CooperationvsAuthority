import numpy as np

def frequency_strategies(data_simulation):
    
    """

    Calculus of the frequencies of strategies for a simulation

    Parameters:

    -----------------------------
	
    data_simulation: an array with data from each generation
    
    -----------------------------

    Returns:
        
    frequencies: an array with the strategy frequencies
    """
    
    tot_strategy = np.zeros(12, np.uint64)
    
    only_strategy= data_simulation[:,0,:]
    
    a=np.unique(only_strategy, return_counts=True)
    
    tot_strategy[a[0]]=a[1]
    
    assert len(tot_strategy) == 12
    
    shape=np.shape(data_simulation)
    
    tot_people = shape[0]*shape[2]
    
    inv_tot_p = np.float16(1/tot_people)
    
    frequencies=np.array(tot_strategy*inv_tot_p, np.float16)
    
    assert np.shape(frequencies) == (12,)
    
    return frequencies

def analize_simulations(all_data):
    
    """

    Create the dataframe of the frequencies of strategies for all the simulations

    Parameters:

    -----------------------------
	
    all_data: a list with all the data generated by simulations
    
    -----------------------------

    Returns:
        
    stat_strategies: an array with the frequencies of strategies in all simulation
    
    mean_strategy: an array with the mean strategy of every simulations
    """
    
    stat_strategies=np.array([])
    
    for N_simulation in range(len(all_data)):
        
        stat_strategies=np.array(np.append(stat_strategies, frequency_strategies(all_data[N_simulation]), axis=0), dtype=np.float16)
        
    if np.shape(stat_strategies) == (12,):
        
        stat =[stat_strategies]
    
    else:
        
        stat=stat_strategies
    
    mean_strategy=np.mean(stat, 1, np.float32)
    
    np.savetxt('Results.csv', stat_strategies, delimiter=',',fmt='%10.5f')
        
    return stat_strategies, mean_strategy
    


