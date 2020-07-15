# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 16:21:29 2020

@author: aitam
"""
from get_data import *

width=29
height=20


get_data('data_base/avec_feuilleton/',width,height,'avec_feuilleton.csv',1)
get_data('data_base/sans_feuilleton/',width,height,'sans_feuilleton.csv',0)