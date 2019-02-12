# BSD 3-Clause License

# Copyright (c) 2019, FPAI SeriouslyHAO
# Copyright 2013 John Stowers, Strawlab
# Copyright 2015 Netherlands eScience Center

# All rights reserved.


# -*- coding: utf-8 -*-
# port of
# http://pointclouds.org/documentation/tutorials/statistical_outlier.php
# you need to download
# http://svn.pointclouds.org/data/tutorials/table_scene_lms400.pcd

import pcl


p = pcl.load("./examples/pcldata/tutorials/table_scene_lms400.pcd")

fil = p.make_statistical_outlier_filter()
fil.set_mean_k(50)
fil.set_std_dev_mul_thresh(1.0)

pcl.save(fil.filter(), "./examples/pcldata/tutorials/table_scene_lms400_inliers.pcd")

fil.set_negative(True)
pcl.save(fil.filter(), "./examples/pcldata/tutorials/table_scene_lms400_outliers.pcd")
