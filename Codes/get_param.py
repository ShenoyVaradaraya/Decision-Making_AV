#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 18:51:14 2021

@author: varad
"""
import numpy as np 
import scipy.linalg
import itertools

def get_param():
    class Group:
        def __init__(self,**kwargs):
            self.__dict__.update(kwargs)
    param = Group(
        w_lane = 5,          # (m) lane width
        l_car = 6 ,          # (m) car length
        w_car = 3 ,          # (m) car width
        l_road = 5000,       # (m)
        v_nominal = 70/3.6,  # (m/s) nominal car speed  
        v_max = 90/3.6,     # (m/s) maximum car speed 
        v_min = 50/3.6,      # (m/s) minimum car speed
        t_step_DT = 0.5,     # (s) 
        t_step_DT_2 = 0.5,   # (s)  # move blocked
        t_step_Sim = 0.5,    # (s)             #0.25
        discount = 0.8,      # discount factor # 0.8
        dR_drop = -1e9,      # ?
        num_cars = 5,        # number of cars
        num_AV = 1 ,
        num_Human =4,
        max_episode = 2,     # number of maximum episode
        num_lanes =3,        # number of lanes
        init_x_range = 30,
        episode = 0,
        lr = 2.5,
        lf = 2.5,
        v_target = 95/3.6,
        outfile = 'Test.mp4',
        plot_fname = 'plot',
        plot_format = '.jpg',
        outdir = 'Images',
        fps = 5,
        sim_case = 1,
        l_car_safe_fac = 1.1,
        w_car_safe_fac = 1.25,
        W_l_car_fac = 1.5,
        W_w_car_fac = 3)

    param.complete_flag = np.zeros((param.max_episode,param.num_cars))
    
    # Disturbances only in inputs
    # Combinations of disturbances = 2^(m)
    param.dist_comb = list(itertools.product([-1, 1], repeat=2))

    return param
