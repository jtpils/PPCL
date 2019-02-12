# BSD 3-Clause License

# Copyright (c) 2019, FPAI SeriouslyHAO
# Copyright 2013 John Stowers, Strawlab
# Copyright 2015 Netherlands eScience Center

# All rights reserved.


import pcl.pcl_grabber

def func(obj):
    print(obj)
    obj.Test()     # Call to a specific method from class 'PyGrabberNode'
    return obj.d_prop

n = pcl.pcl_grabber.PyGrabberNode()    # Custom class of my own
cb = pcl.pcl_grabber.PyGrabberCallback(func)
print(cb.execute(n))