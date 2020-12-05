
# 0 Abstract
In this paper we describe a semantic mapping system for autonomous offroad driving with an All-Terrain Vehicle (ATVs). The system’s goal is to provide a richer representation of the environment than a purely geometric map, allowing it to distinguish, e.g. tall grass from obstacles. The system builds a 2.5D grid map encoding both geometric (terrain height) and semantic information (navigation-relevant classes such as trail, grass, etc.). The geometric and semantic information are estimated online and in real-time from LiDAR and image sensor data, respectively. Using this semantic map, motion planners can create semantically aware trajectories. To achieve robust and efficient semantic segmentation, we design a custom Convolutional Neural Network (CNN) and train it with a novel dataset of labelled off-road imagery built for this purpose. We evaluate our semantic segmentation offline, showing comparable performance to the state of the art with slighly lower latency. We also show closed-loop field results with an autonomous ATV driving over challenging off-road terrain by using the semantic map in conjunction with a simple path planner. Our models and labelled dataset will be publicly available.



# 1 Introduction
The last few years have seen enormous progress in the 3D sensing capabilities of   autonomous vehicles. Mature and robust LiDAR and INS technologies give selfdriving vehicles an accurate and real-time sense of the geometric structure around   them, immensely simplifying navigation-related tasks.  

However, we have observed that relying primarily on geometric information   leads to disappointing results for autonomous navigation in off-road environments.    The main reason is that geometric structure, by itself, fails to provide many important distinctions for wheeled All-Terrain Vehicles (ATVs) such as ours, shown in 1.   For example, tall grass may be perceived as an obstacle, but our ATV may traverse   it if desired. Similarly, leaf litter may appear as rocky terrain, or puddles may appear as either holes or smooth surfaces. All of these may lead to suboptimal, even   dangerous, decisions in path planning. Similar observations have been made many   times before in the context of off-road robotics, e.g., [11, 15, 22, 10].   

In this paper, we describe a system to counter this problem by building a semantic map, a representation of the vehicle’s surroundings encoding both geometric   (e.g. height, roughness) and semantic information (navigation-relevant classes such   as trail, grass, obstacle, etc.). The map is stored as a 2.5D grid centered on the vehicle frame, and is continuously updated as new sensor data is acquired. Using this   representation, a motion planner can create semantically-aware trajectories.   

Our key contribution is a simple yet effective system coupling a custom Convolutional Neural Network architecture, based on Fully Convolutional Networks [14],   and a 2.5D vehicle-centered semantic grid map that fuses the geometric and semantic measurements as the vehicle moves and acquires more data. We show the   effectiveness of the semantic segmentation CNN in offline benchmarks. By using a   simple planner with the semantic map, we show qualitative examples of our system   being successfully used to navigate challenging off-road terrain.   

As an additional contribution, the labelled dataset of off-road imagery used to   train our network will be made publicly available.


# 2 Related Work

Our system is heavily inspired by the rich literature on semantic approaches to offroad navigation tasks, going as far back as 1990 [7].

A decade later, various practical systems showed impressive results with this paradigm, usually with a combination of LiDAR and images [11, 15, 22, 25, 26].

The LAGR program [10] featured various highly relevant systems such as [18,   12, 24, 2], which performed semantic classification with hand-engineered vision   pipelines. An exception is [9], featuring an early deep neural network system for   semantic segmentation.

In more recent work, [21] demonstrate autonomous navigation featuring a lightweight   semantic segmentation system. Unlike our system, they use traditional visual feature   engineering, leading to noisy pixelwise predictions that they smooth with a novel   regularization method. In contrast, our architecture, based on Fully Convolutional   Networks (FCNs) [14], incorporates spatial context that naturally smoothes the output. Another relevant work is [23], which uses an encoder-decoder network architecture that is similar to FCNs. They explore modalities beyond RGB and achieve   impressive segmentation results. However, they do not build a metric map or demonstrate closed-loop navigation.

# 3 Approach

Overview. This system architecture is outlined in Fig. 2. There are two primary sensor streams, RGB imagery and LiDAR point cloud data. The RGB images are fed into the semantic segmentation module, which uses a CNN to generate a pixelwise labelling. Concurrently, the LiDAR point clouds are used to update a 2.5D grid map in the semantic mapping module. The semantic mapping module also receives the pixelwise prediction images from the semantic segmentation module and projects them onto the 2.5D grid map, which fuses the semantic predictions over time. The result is a vehicle-centered 2.5D grid map encoding continuously updated estimates of relevant geometric and semantic information for off-road navigation. Finally, the map is used for semantically-aware path planning. For our initial testing we used a simple receding horizon path planner that assigns a traversal cost to each semantic class and continuously chooses a path to minimize the cost. The whole system runs at 10Hz, a rate dictated by the speed at which the semantic mapping module processes images. 

Hardware Platform. Our vehicle is shown in Fig. 1. It is a commercial All-Terrain Vehicle modified and instrumented for experiments in autonomous off-road driving. The sensor suite includes an INS/GPS system, a 64-line Velodyne LiDAR and an RGB stereo camera with a 21 cm baseline manufactured by Carnegie Robotics. Note that the system in this paper does not currently use the stereo depth information. All computation is performed onboard with two COTS laptops, connected through highspeed ethernet. The laptop for semantic mapping includes an NVIDIA GT980M GPU, used to achieve real-time execution of the CNN classifier. 

Software Platform. All computers run Ubuntu Linux. The different system modules run concurrently as ROS nodes and communicate through ROS messages. The nodes are implemented in C++ and Python, using CUDA (generated via the Theano library [3]) to make effective use of the GPU.

## 3.1 Semantic Segmentation
The goal of 2D semantic segmentation is to assign one of K predefined classes to each pixel in an image. Like many tasks in computer vision, the state of the art for this task has been recently revolutionized by Deep Learning, and in particular Convolutional Neural Networks. 

For this task, the most successful neural networks architectures are Fully Convolutional Network (FCNs) [14]. The key idea in these networks is to take advantage of convolutional structure to label all the pixels simultaneously with a very similar network to more traditional CNNs. Due to pooling, this results in low-resolution outputs; to reverse this, so-called “deconvolution” layers are added to upsample the output. In order to preserve high-frequency detail, skip layers connecting early layers to upsampled feature maps are added. Encoder-Decoder architectures [17, 1], of which UpNet [23] is an example, are similar, but omit skip layers. 

At the start of the project, we found state of the art architectures to be relatively slow, as they were optimized for accuracy over speed. Thus we implemented and trained our own architectures, using the Theano [3] and Lasagne [6] libraries. Currently, we have found various possible architectures to show very similar accuracy for our off-road semantic segmentations tasks, differing mostly in time cost, which in turn is largely driven by details of the architecture and input/output resolution.We believe this is due to the relatively small datasets used, but merits further investigation. 

To date we have used mostly two architectures. The first, cnns-fcn, is based on our “convolutionalization” of VGG-CNNs from [4], and has 227×227 input size with 109×109 output size. The second, dark-fcn, is based on our own convolutionalization of the Darknet architecture [19], which in turn is similar but more effi- cient than VGG16 [20]. For dark-fcn both the input and output are 300×300, in order to facilitate comparison with UpNet. Despite the higher resolution dark-fcn is faster than cnns-fcn: 21 ms on a GT980M, compared to 37 ms. The authors of UpNet [23] describe a 50 ms with Caffe on a GTX Titan X, which in our experience has similar speeds to the GT980M. This leads us to believe our model should be faster or at least comparable. Fig. 3 shows both of our architectures. Code and trained models will also be made available.




## 3.2 Semantic Mapping
The output of the semantic mapping step is in 2D image space, but it is far more natural for vehicles to plan in a 3D, metric space. In our case, as adopt a 2.5D grid, or heightmap representation for simplicity. This suffices for most environments, but would potentially have issues with overhanging trees or tunnels.


To keep an up-to-date heightmap of the vehicle’s surroundings, we use a scrolling grid data structure, which has been reinvented multiple times in the literature. This structure is a generalization of ring-buffers to two dimensions, and its main feature is that it can be shifted (translated) without copying its data, and instead updating the variables indicating its limits. This is a speed optimization; logically, the grid behaves like a finite 2D array centered around the vehicle, with each grid cell containing various properties about the terrain. In our paper the grid cells are 0.25m×0.25m each, and the map has 400×400 cells. Each grid cell maintains a running estimate of the minimum and maximum height in that grid cell, computed by using occupancy and free-space constraints derived from LiDAR rays, similar to [8, 28]. For each point in the point cloud, we raytrace on our grid using Bresenham’s algorithm in 3D; cells that are passed through, and above, are considered empty, and cells where the beam stops, and below, are considered occupied.


The semantic map also integrates semantic measurements, as its name indicates. To project the output of the 2D semantic segmentation into a heightmap representation, we follow a straightforward process depicted in Fig. 4.





Given that we know the relative position of the camera and the LiDAR, and the camera intrinsics, we can project the 2D semantic predictions onto the 2.5D grid cells using simple geometry. However, for added robustness, we fuse measurements over time. To this end we adopt a scheme inspired by the sequential filtering process of occupancy maps [16], but generalized to K classes. 

For this we use the probabilistic (softmax) pixelwise output of the classifier. We maintain a running sum of the log odds of the K classes projected to each grid cell. While this soft multiclass representation could be used directly, for simplicity when interfacing with other systems we use the argmax of the K classes as our current best estimate of the semantic class for each grid cell. Note that this representation assumes a single class per cell, which may be a limitation in certain environments. 

An example cumulative output of the semantic map in a live field run is shown in Fig. 5.


## 3.3 Path Planing
Path Planning. a) Library of candidate paths, overlaid on top of the semantic map. Red indicates feasible paths. b) Illustration of how we account for vehicle width. For each trajectory, we compute the cost (or reward) over seven shifted versions of the trajectory, covering the vehicle footprint. c) An example chosen trajectory, chosen according to the traversability score of the semantic classes it covers.

In order to demonstrate autonomous operation we implement an extremely simple receding horizon path planner. The planner has a library of 30 trajectories corresponding to yaw rates of 15◦/s to 15◦/s, discretized at 1◦/s, and at constant velocity of 9 km h 1 ; see Fig. 6a). 

Each time the map is updated, which happens at 10 Hz, a trajectory is chosen from the library. The choice of trajectory maximizes a reward function derived from the semantic map as follows. Cells labelled as “smooth” or “rough” trail have a reward of 1, and cells labelled as “grass” have a reward of 0.1. All other classes have zero reward. The total reward of a trajectory is the sum of rewards over a 20 m trajectory length, originating from the vehicle. To account for vehicle width, we slightly modify this calculation, as shown in Figure 6b).

The advantage of this planner is that in its extreme simplicity, its performance depends largely on the output of our semantic mapping, with no interference from other factors that will be a present in a more complex, multi-layered system. However, our system was also used as an additional input to a more deliberative planner, for which the main representation was a geometric map built with LiDAR. In this planner, our semantic predictions were used primarily to avoid treating grass as an obstacle.


# 4 Experiments
Overview. We evaluate our system in two ways. First, we run offline benchmarks of the semantic segmenation module in two datasets. Second, we demonstrate the whole system operating autonomously in live field experiment.

## 4.1 Offline Benchmarks
In order to evaluate our semantic segmentation module we use two datasets, the DeepScene dataset from Valada et al. [23] and our own dataset, the Yamaha-CMU Off-Road Dataset. 

DeepScene Dataset. 
This dataset consists of 233 training images and 139 validation images of off-road imagery densely labelled with six semantic categories: void, road, grass, vegetation, tree, sky, and obstacle. While this dataset shows some interesting variety in appearance due to time of day, it is fairly small and seems to lack diversity in terms of weather and location. A key feature of this dataset is various modalities (depth, NIR), but we do not currently make use of them. 

Yamaha-CMU Off-Road Dataset. 
In order to train and evaluate our method we have collected our own dataset, which we call Yamaha-CMU-Off-Road, or YCOR. It consists of 1076 images collected in four different locations in Western Pennsylvania and Ohio (8), spanning three different seasons (Fig. 7). The dataset was labelled using a polygon-based interface with eight classes: sky, rough trail, smooth trail, traversable grass, high vegetation, non-traversable low vegetation, obstacle. The polygon labels were post-processed using a Dense CRF [13] to densify the labels; the output of the CRF was manually inspected, and in some cases corrected, to ensure no wrong labels were created. 

We believe our dataset is more diverse and challenging than DeepScene. In Fig. 8, we show the mean RGB image and pixelwise labelmode of each dataset. The DeepScene dataset shows a left-right bias and more predictable structure than ours; if we used the pixelwise mode as a baseline classifier, we would obtain 0.30 pixelwise error-rate in DeepScene, but 0.51 in ours. However, we acknowledge that compared to recent efforts, both datasets are relatively small; cf. CityScapes [5], with 25000 labelled images.


Fig. 7 Montage of frames from the YCOR dataset.

Our current split has 931 training images, and 145 validation images. This split  was generated randomly, ensuring there was no overlap in data collection session  between images in the training and validation split. However, there is overlap in  locations used. We will provide location and time of acquisition metadata to enable  further evaluation in terms of generalization across these factors.  

Quantitative Results. We evaluated our models on the two datasets. In each case  we train our models from scratch on the predefined training set until convergence  with SGD, dividing by the initial learning rate (0.0001) by a factor of 10 three times.  We use a standard pixelwise cross-entropy loss with a small L2 regularization factor  (0.0005). Training takes around two days on a GT980Ti GPU. We use crop, rotation  and color augmentations at training time, and none at test time. We use per-class  intersection over union (IoU) as the evaluation metric, the most common metric for  semantic segmentation.


Table 1 shows results for DeepScene and Table 2 shows results for YCOR. In  both, we include a variant of the dark-fcn model with 448 × 448 resolution, in  addition to the standard 300 × 300. We report the numbers from their paper [23],  where we denote by frequency-weighted IoU (fw-IoU) what they denote as IoU,  and add mean IoU (mIoU), calculated by ourselves. As we can see, both our models  perform comparably, with dark-fcn having a slight advantage. In the DeepScene  dataset we can also compare the two models with the RGB UpNet. We see that  our models have a slight edge in fw-IoU, though they display dramatically worse  performance for obstacles, which severely skews the mIoU metric. We note that the  number of obstacle pixels in the dataset is three orders of magnitude less than for  the other classes, so the network tends to ignore it. Nonetheless, it is an important  class, and we are investigating how to detect it more accurately. Finally, we see that  increasing the input resolution gives a slight boost in performance.  





Qualitative Results. We show some qualitative labellings of the cnns-fcn architecture for each dataset in Fig. 9. As can be seen, the results are generally quite  accurate. For the YCOR, most of the confusions come from smooth vs. rough trail,  a distinction that is hard for humans to make consistently.


## 4.2 Field Experiments
We performed various self-driving experiments in March and July 2017, in various locations around our testing site near Pittsburgh, PA. Despite the simplicity of   our planner, the vehicle managed to successfully traverse various trails that were  too challenging for a previous LiDAR-only system. These include locations with  puddles, grass in the middle of the trail, and narrow trails. We will upload video  to the project website at http://dimatura.net/offroad. Fig. 10 shows the vehicle in  autonomous operation.  

On the other hand, we observed some limitations of our current system. Many  of the limitations were due to the simplicity of the receding horizon planner, which  often swerved from side-to-side in wider trails.  

Some of the failures were also due to our semantic classification system. For  example, it sometimes failed to detect sparse grass alongside the trail, resulting in      the vehicle veering off-trail. In one occasion, it also confused a large non-traversable  bush with traversable grass, forcing us to manually intervene.  


To address these issues we will use a more deliberative and safe planner, more  training data, and better network architectures.  

Timing. We run all computation onboard the vehicle using a i7 laptop with a 6GB  GT980M GPU. The bottleneck of the system is in the semantic mapping, with semantic segmentation taking approximately 35 ms per image and the label projection taking around 60 ms per image. These steps occur sequentially, leading to the  roughly 10Hz rate operation of the system. This is sufficient for medium-speed operation, and we expect that even without changes to our architecture, GPU advances  will lead to at least 2× faster operation in the near future.  


# 5 Conclusions
We have introduced an efficient and robust semantic mapping system for off-road  navigation featuring a state-of-the-art CNN classifier. To train the CNN, we have  collected and labelled a new dataset of off-road imagery. We have evaluated it in offline benchmarks with results comparable to the state of the art with lower latencies.  We have also demonstrated closed-loop operation in challenging off-road terrain.  

In future work, we are interested in incorporating recent advances from the state  of the art in semantic segmentation, such such as Dilation layers [27] and multiple  input modalities, like [23].  

Having verified firsthand the difficulty of accurately labelling large amounts of  data, in future work we are interested in alternatives to manual labelling, such as  self-supervision and inverse reinforcement learning.


