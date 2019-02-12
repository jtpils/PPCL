# -*- coding: utf-8 -*-
# Euclidean Cluster Extraction
# http://pointclouds.org/documentation/tutorials/cluster_extraction.php#cluster-extraction
import numpy as np
import pcl

_data = np.array(
    [[0.0080142, 0.694695, -0.26015, 0.1],
     [-0.342265, -0.446349, 0.214207, 0.1],
     [0.173687, -0.84253, -0.400481, 0.1],
     [-0.874475, 0.706127, -0.117635, 0.1],
     [0.908514, -0.598159, 0.744714, 0.1]], dtype=np.float32)



cloud = pcl.load('/home/li/PROJECTS/TRAIN/PPCL-master/examples/tests/tutorials/table_scene_lms400.pcd')
print('type(cloud)',type(cloud))
data=np.array(cloud)
print('data.shape',data.shape)
data2=np.zeros((460400,1),dtype=np.float32)
data=np.column_stack((data,data2))
print('data.shape',data.shape)



cloud = pcl.PointCloud_PointXYZI(data)
# cloud = pcl.PointCloud_PointXYZI(_data)






#   // Create the filtering object: downsample the dataset using a leaf size of 1cm
#   pcl::VoxelGrid<pcl::PointXYZ> vg;
#   pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_filtered (new pcl::PointCloud<pcl::PointXYZ>);
#   vg.setInputCloud (cloud);
#   vg.setLeafSize (0.01f, 0.01f, 0.01f);
#   vg.filter (*cloud_filtered);
#   std::cout << "PointCloud after filtering has: " << cloud_filtered->points.size ()  << " data points." << std::endl; //*
vg = cloud.make_voxel_grid_filter()
vg.set_leaf_size (0.1, 0.1, 0.1)
cloud_filtered = vg.filter ()

print('cloud_filtered.size',cloud_filtered.size)




#   // Create the segmentation object for the planar model and set all the parameters
#   pcl::SACSegmentation<pcl::PointXYZ> seg;
#   pcl::PointIndices::Ptr inliers (new pcl::PointIndices);
#   pcl::ModelCoefficients::Ptr coefficients (new pcl::ModelCoefficients);
#   pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_plane (new pcl::PointCloud<pcl::PointXYZ> ());
#   pcl::PCDWriter writer;
#   seg.setOptimizeCoefficients (true);
#   seg.setModelType (pcl::SACMODEL_PLANE);
#   seg.setMethodType (pcl::SAC_RANSAC);
#   seg.setMaxIterations (100);
#   seg.setDistanceThreshold (0.02);
seg = cloud.make_segmenter()
seg.set_optimize_coefficients (True)
seg.set_model_type (pcl.SACMODEL_PLANE)
seg.set_method_type (pcl.SAC_RANSAC)
seg.set_MaxIterations (100)
seg.set_distance_threshold (0.02)

#   int i=0, nr_points = (int) cloud_filtered->points.size ();
#   while (cloud_filtered->points.size () > 0.3 * nr_points)
#   {
#     // Segment the largest planar component from the remaining cloud
#     seg.setInputCloud (cloud_filtered);
#     seg.segment (*inliers, *coefficients);
#     if (inliers->indices.size () == 0)
#     {
#       std::cout << "Could not estimate a planar model for the given dataset." << std::endl;
#       break;
#     }
#     // Extract the planar inliers from the input cloud
#     pcl::ExtractIndices<pcl::PointXYZ> extract;
#     extract.setInputCloud (cloud_filtered);
#     extract.setIndices (inliers);
#     extract.setNegative (false);
# 
#     // Get the points associated with the planar surface
#     extract.filter (*cloud_plane);
#     std::cout << "PointCloud representing the planar component: " << cloud_plane->points.size () << " data points." << std::endl;
# 
#     // Remove the planar inliers, extract the rest
#     extract.setNegative (true);
#     extract.filter (*cloud_f);
#     *cloud_filtered = *cloud_f;
#   }

i = 0
nr_points = cloud_filtered.size
# while nr_points > 0.3 * nr_points:
#     # Segment the largest planar component from the remaining cloud
#     [inliers, coefficients] = seg.segment()
#     # extract = cloud_filtered.extract()
#     # extract = pcl.PointIndices()
#     cloud_filtered.extract(extract)
#     extract.set_Indices (inliers)
#     extract.set_Negative (false)
#     cloud_plane = extract.filter ()
#     
#     extract.set_Negative (True)
#     cloud_f = extract.filter ()
#     cloud_filtered = cloud_f


# Creating the KdTree object for the search method of the extraction
# pcl::search::KdTree<pcl::PointXYZ>::Ptr tree (new pcl::search::KdTree<pcl::PointXYZ>);
# tree->setInputCloud (cloud_filtered);

tree = cloud_filtered.make_kdtree()
# tree = cloud_filtered.make_kdtree_flann()


# std::vector<pcl::PointIndices> cluster_indices;
# pcl::EuclideanClusterExtraction<pcl::PointXYZ> ec;
# ec.setClusterTolerance (0.02); // 2cm
# ec.setMinClusterSize (100);
# ec.setMaxClusterSize (25000);
# ec.setSearchMethod (tree);
# ec.setInputCloud (cloud_filtered);
# ec.extract (cluster_indices);
ec = cloud_filtered.make_EuclideanClusterExtraction()
ec.set_ClusterTolerance (0.02)
ec.set_MinClusterSize (100)
ec.set_MaxClusterSize (25000)
ec.set_SearchMethod (tree)
cluster_indices = ec.Extract()

print('cluster_indices : ' + str(cluster_indices.count) + " count.")
print('cluster_indices ' ,type(cluster_indices))
print('cluster_indices ' ,len(cluster_indices))


# print('cluster_indices : ' + str(cluster_indices.indices.max_size) + " count.")

#   int j = 0;
#   for (std::vector<pcl::PointIndices>::const_iterator it = cluster_indices.begin (); it != cluster_indices.end (); ++it)
#   {
#     pcl::PointCloud<pcl::PointXYZ>::Ptr cloud_cluster (new pcl::PointCloud<pcl::PointXYZ>);
#     for (std::vector<int>::const_iterator pit = it->indices.begin (); pit != it->indices.end (); ++pit)
#       cloud_cluster->points.push_back (cloud_filtered->points[*pit]); //*
#     cloud_cluster->width = cloud_cluster->points.size ();
#     cloud_cluster->height = 1;
#     cloud_cluster->is_dense = true;
# 
#     std::cout << "PointCloud representing the Cluster: " << cloud_cluster->points.size () << " data points." << std::endl;
#     std::stringstream ss;
#     ss << "cloud_cluster_" << j << ".pcd";
#     writer.write<pcl::PointXYZ> (ss.str (), *cloud_cluster, false); //*
#     j++;
#   }
#



cloud_cluster = pcl.PointCloud()

for j, indices in enumerate(cluster_indices):
    # cloudsize = indices
    print('indices = ' + str(len(indices)))
    # cloudsize = len(indices)
    points = np.zeros((len(indices), 3), dtype=np.float32)
    # points = np.zeros((cloudsize, 3), dtype=np.float32)

    print('indices',indices)
    
    # for indice in range(len(indices)):
    for i, indice in enumerate(indices):
        # print('dataNum = ' + str(i) + ', data point[x y z]: ' + str(cloud_filtered[indice][0]) + ' ' + str(cloud_filtered[indice][1]) + ' ' + str(cloud_filtered[indice][2]))
        # print('PointCloud representing the Cluster: ' + str(cloud_cluster.size) + " data points.")


        # print('type(cloud_filtered)',type(cloud_filtered))
        # print('indice',indice)

        indice=(indice-1)/2
        points[i][0] = cloud_filtered[indice][0]
        points[i][1] = cloud_filtered[indice][1]
        points[i][2] = cloud_filtered[indice][2]

    cloud_cluster.from_array(points)
    ss = "cloud_cluster_" + str(j) + ".pcd";
    pcl.save(cloud_cluster, ss)


print('success')
