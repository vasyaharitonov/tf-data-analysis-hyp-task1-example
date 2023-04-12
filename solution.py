import pandas as pd
import numpy as np

from statsmodels.stats.proportion import proportions_ztest

chat_id = 291445198

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    alpha = 0.05
    _, p_value = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='larger')
    return False if p_value > alpha else True
