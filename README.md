# Overview
A curated list of awesome 3D point cloud denoising (and closely related fields) papers.

You may also find interesting my **survey preprint**: [Unraveling Noise in 3D Point Clouds: A Comprehensive Survey](https://www.techrxiv.org/doi/full/10.36227/techrxiv.177281447.78646347/v1)

> [!NOTE]
> We focus particularly on point clouds as a representation of 3D data and on denoising as a technique, but we also include some works that deal with other representations, such as meshes, voxels... or closely related techniques, such as hole-filling, surface reconstruction... since—like denoising—they aim to recover the underlying surface of the scanned real-world object.

This is a work in _continuous progress_.

For any suggestions, please contact garnungalejandro@gmail.com.

Thank you and enjoy the 3D point cloud denoising world.

**Updated: 02/07/2025**

<h2>Keywords</h2>

`trad.`: traditional filter | `var.`: variational-based | `pde`: PDE-based | `spec.`: spectral-based | `dl.`: deep learning | `un.`: unsupervised | `rec.`: resampling/compression | `sur.`: surface reconstruction  | `ne.`: normal estimation | `inp.`: inpainting | `res.`: super-resolution | `mesh.`: mesh denoising | `surv.`: survey | `oth.`: other 

## Gradations (highly influential citations)
- ◼️ **Less than 5 citations**
- 🔹 **More than 5 citations**
- 🔸 **More than 10 citations**
- 🔥 **More than 25 citations**
- 🌟 **More than 50 citations**

_Star count automated from [Semantic Scholar](https://api.semanticscholar.org/api-docs/#tag/Paper-Data/operation/post_graph_get_papers) with [this script](./update_list.py)._

<h2>Table of Contents</h2>

[2003](#2003), [2004](#2004), [2005](#2005), [2006](#2006), [2007](#2007), [2008](#2008), [2009](#2009), [2010](#2010), [2011](#2011), [2012](#2012), [2013](#2013), [2014](#2014), [2015](#2015), [2016](#2016), [2017](#2017), [2018](#2018), [2019](#2019), [2020](#2020), [2021](#2021), [2022](#2022), [2023](#2023), [2024](#2024), [2025](#2025)

# 2003
- [[Link](https://graphics.stanford.edu/courses/cs468-03-fall/Papers/Levin_MovingLeastSquares.pdf)] Mesh-Independent Surface Interpolation MLS [][`oth.`] 🔥 
- [[Link](https://people.csail.mit.edu/thouis/JDD03.pdf)] Non-Iterative, Feature-Preserving Mesh Smoothing [[code](https://github.com/Oponn-1/3D-Point-Cloud-Denoising/blob/master/smoother.c)] 🔥
- [[Link](https://dev.ipol.im/~morel/Dossier_MVA_2011_Cours_Transparents_Documents/2011_Cours3_Document1_bilateral_mesh_denoising.pdf)] Bilateral mesh denoising [[code](https://github.com/bldeng/GuidedDenoising/tree/master)] 🔸 `trad.`

# 2004
...

# 2005
...

# 2006
- [[Link](https://www.scitepress.org/papers/2006/13589/13589.pdf)] Point cloud denoising using robust principal component analysis ◼️ `trad.`

# 2007
- [[Link](https://langbein.org/wp-content/uploads/2009/06/sun2007.pdf)] Fast and Effective Feature-Preserving Mesh Denoising [[code](https://github.com/bldeng/GuidedDenoising/tree/master)] 🌟
- [[Link](https://hal.science/hal-00333374/file/SSVM-2007.pdf)] Discrete Regularization on Weighted Graphs for Image and Mesh Filtering ◼️ `var.` `pde` `mesh.`
- [[Link](https://dev.ipol.im/~morel/Dossier_MVA_2011_Cours_Transparents_Documents/2011_Cours3_Document2_Locally_Optimal_Projection.pdf)] Parameterization-free Projection for Geometry Reconstruction (LOP) 🔥

# 2008
- [[Link](https://lezoray.users.greyc.fr/Publis/IEEE_IP_2008.pdf)] Nonlocal discrete regularization on weighted graphs: A framework for image and manifold processing 🔥 `var.`

# 2009
- [[Link](https://ieeexplore.ieee.org/document/5137578)] Noise reduction and modeling methods of TLS point cloud based on R-tree ◼️
- [[Link](https://ieeexplore.ieee.org/document/5402768)] Algorithm for 3D Point Cloud Denoising ◼️ `trad.`
- [[Link](https://www.cs.sfu.ca/~haoz/pubs/siga09_consolidater_reduced.pdf)] Consolidation of Unorganized Point Clouds for Surface Reconstruction (WLOP) [[code](https://github.com/jinseokbae/WLOP-based-PointCloudDenoiser)] 🌟
- [[Link](https://ieeexplore.ieee.org/document/5287748)] 3D Body Point Cloud Data Denoising and Registration ◼️

# 2010
- [[Link](https://www.scientific.net/AMR.97-101.3631)] Scatter Point Cloud Denoising Based on Self-Adaptive Optimal Neighborhood ◼️
- [[Link](https://dl.acm.org/doi/10.1145/1857907.1857911)] ℓ1-Sparse reconstruction of sharp point set surfaces 🔹 `var.`

# 2011
- [[Link](https://chpc.greyc.fr/images/Documents/Publications/2011_06_Nonlocal_PDEs-Based_Morphology_on_Weighted_Graphs_for_Image_and_Data_Processing.pdf)] Nonlocal PDEs-Based Morphology on Weighted Graphs for Image and Data Processing ◼️ `pde`
- [[Link](https://hongbofu.people.ust.hk/doc/bilateral_normal_filtering_tvcg11.pdf)] Bilateral Normal Filtering for Mesh Denoising [[code](https://github.com/bldeng/GuidedDenoising/tree/master)] 🌟 `trad.`

# 2012
- [[Link](https://www.tandfonline.com/doi/epdf/10.1080/17415977.2011.603087?needAccess=true)] Denoising point cloud ◼️ `trad.`
- [[Link](https://www.scientific.net/AMR.479-481.2152)] A New near Point Denoising Algorithm for Point Cloud ◼️

# 2013
- [[Link](https://par.nsf.gov/servlets/purl/10443276)] Motion estimation and filtered prediction for dynamic point cloud attribute compression ◼️
- [[Link](https://people.engr.tamu.edu/schaefer/research/L0Smoothing.pdf)] Mesh Denoising via L0 Minimization [[code1](https://github.com/tatsy/L0Denoising)][[code2](https://github.com/AlonzoQuio/MeshDenoisingViaL0Minimization/tree/master)][[code3](https://github.com/bldeng/GuidedDenoising/tree/master)] 🔥 `var.`
- [[Link](https://dl.acm.org/doi/10.1145/2421636.2421645)] Edge-aware point set resampling (AWLOP/EAR) 🔥

# 2014
- [[Link](https://people.csail.mit.edu/jsolomon/assets/MeshBilateral.pdf)] A General Framework for Bilateral and Mean Shift Filtering ◼️ `trad.`
- [[Link](https://ieeexplore.ieee.org/abstract/document/7009913)] Research on 3D scanning point cloud de-nosing ◼️
- [[Link](https://dl.acm.org/doi/10.1145/2601097.2601172)] Continuous projection for fast L1 reconstruction (CLOP) 🔸
- [[Link](https://inria.hal.science/hal-01017700/file/star_author.pdf)] State of the Art in Surface Reconstruction from Point Clouds 🌟

# 2015
- [[Link](https://www.sciencedirect.com/science/article/abs/pii/S0167839615000345)] Denoising Point Sets via L0 Minimization 🔸 `var.`
- [[Link](https://ieeexplore.ieee.org/document/7418871)] 3D point cloud denoising and normal estimation for 3D surface reconstruction ◼️
- [[Link](http://sofienbouaziz.com/pdf/GuidedFilter_PG15.pdf)] Guided Mesh Normal Filtering [[code](https://github.com/bldeng/GuidedDenoising/tree/master)] 🔥
- [[Link](https://www.scientific.net/AMM.741.204)] Adaptive Denoising Algorithm for Scanning Beam Points Based on Angle Thresholds ◼️
- [[Link](https://arxiv.org/pdf/1511.04902)] Graph-based denoising for time varying point clouds ◼️

# 2016
- [[Link](https://arxiv.org/pdf/1602.05312)] Density-based Denoising of Point Cloud ◼️
- [[Link](https://dl.acm.org/doi/10.1145/2980179.2980232)] Mesh Denoising via Cascaded Normal Regression `mesh.` 🔥
- [[Link](https://ieeexplore.ieee.org/document/7785084)] Point Cloud Noise and Outlier Removal for Image-Based 3D Reconstruction ◼️
- [[Link](https://www.sciencedirect.com/science/article/abs/pii/S0924271616300922)] Dynamic occlusion detection and inpainting of in situ captured terrestrial laser scanning point clouds sequence ◼️
- [[Link](https://ee.iisc.ac.in/cvlab/papers/haque2016robden.pdf)] Robust Feature-Preserving Denoising of 3D Point Clouds ◼️

# 2017
- [[Link](https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.13068)] Point Cloud Denoising via Moving RPCA 🔸
- [[Link](https://www.ipol.im/pub/art/2017/179/revisions/2022-01-01/article.pdf)] The bilateral filter for point clouds [[code](https://www.ipol.im/pub/art/2017/179/)] 🔹 `trad.`
- [[Link](https://link.springer.com/article/10.1007/s11042-017-5310-9)] Guided 3D point cloud filtering [[code](https://github.com/aipiano/guided-filter-point-cloud-denoise)] ◼️
- [[Link](https://inria.hal.science/hal-02124225v1/document)] Hierarchical Denoising Method of Crop 3D Point Cloud
Based on Multi-view Image Reconstruction ◼️
- [[Link](https://onlinelibrary.wiley.com/doi/10.1111/cgf.13272)] Data-Driven Sparse Priors of 3D Shapes ◼️
- [[Link](https://link.springer.com/article/10.1007/s00371-017-1391-8)] Guided point cloud denoising via sharp feature skeletons ◼️
  
# 2018
- [[Link](https://arxiv.org/pdf/1804.10831)] Fast 3D Point Cloud Denoising via Bipartite Graph Approximation & Total Variation ◼️ `var.`
- [[Link](https://arxiv.org/pdf/1807.00253)] Weighted Multi-projection: 3D Point Cloud Denoising with Estimated Tangent Planes ◼️
- [[Link](https://yulequan.github.io/ec-net/index.html)] EC-Net: an Edge-aware Point set Consolidation Network [[code](https://github.com/yulequan/EC-Net)] 🔥
- [[Link](https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.13344)] Pointpronets: Consolidation of point clouds with convolutional neural networks 🔹
- [[Link](https://arxiv.org/pdf/1712.03574)] Static/Dynamic Filtering for Mesh Geometry [[code](https://github.com/bldeng/MeshSDFilter)] ◼️
- [[Link](https://www3.cs.stonybrook.edu/~qin/research/2018-cad-mesh-denoising-using-sparse-regularization.pdf)] Robust and effective mesh denoising using L0 sparse regularization ◼️
- [[Link](https://www.sciencedirect.com/science/article/abs/pii/S0097849318300797)] Constraint based point set denoising using normal voting tensor and restricted quadratic error metrics ◼️
- [[Link](https://link.springer.com/article/10.1007/s00366-017-0556-4)] Denoising of point cloud data for computer-aided design, engineering, and manufacturing 🔥
- [[Link](https://arxiv.org/pdf/1812.07711)] 3D Point Cloud Denoising via Bipartite Graph Approximation and Reweighted Graph Laplacian ◼️ `var.`
- [[Link](https://ieeexplore.ieee.org/document/8354317)] 3D Shape Processing by Convolutional Denoising Autoencoders on Local Patches ◼️
- [[Link](http://staff.ustc.edu.cn/~zhangwm/Paper/2019_12.pdf)] DUP-Net: Denoiser and Upsampler Network for 3D Adversarial Point Clouds Defense [[code](https://github.com/RyanHangZhou/tensorflow-DUP-Net)] 🔥
  
# 2019
- [[Link](https://www.mdpi.com/2072-4292/11/2/198)] A 3D point cloud filtering method for leaves based on manifold distance and normal estimation ◼️
- [[Link](https://arxiv.org/pdf/1904.04427)] 3D Point Cloud Denoising via Deep Neural Network based Local Surface Estimation ◼️
- [[Link](https://arxiv.org/pdf/1803.07252)] 3D Point Cloud Denoising using Graph Laplacian Regularization of a Low Dimensional Manifold Model [[code](https://github.com/jzengust/ldmm_graph_laplacian_pointcloud_denoise)] 🔸
- [[Link](https://arxiv.org/pdf/1901.01060)] PointCleanNet: Learning to Denoise and Remove Outliers from Dense Point Clouds [[code](https://github.com/mrakotosaon/pointcleannet)] 🌟
- [[Link](https://isprs-archives.copernicus.org/articles/XLII-2-W13/1021/2019/isprs-archives-XLII-2-W13-1021-2019.pdf)] A Novel Denoising Algorithm for Airborne Lidar Point Cloud Based on Empirical Mode Decomposition ◼️
- [[Link](https://www.sciencedirect.com/science/article/pii/S1877050919307793)] A 3D Point Cloud Filtering Algorithm based on Surface Variation Factor Classification ◼️
- [[Link](https://www.semanticscholar.org/paper/Deep-Unsupervised-Learning-of-3D-Point-Clouds-via-Chen-Duan/4d941083fa57d62fed269ceecbf7d8af66ec6c9c)] Deep Unsupervised Learning of 3D Point Clouds via Graph Topology Inference and Filtering [[code](https://github.com/merlresearch/FoldingNet_Plus)] 🔹 `un.`
- [[Link](https://arxiv.org/pdf/1906.04173)] Differentiable Surface Splatting for Point-based Geometry Processing [[code](https://github.com/yifita/DSS)] 🔸
- [[Link](https://people.engr.tamu.edu/schaefer/research/low_rank.pdf)] Low Rank Matrix Approximation for 3D Geometry Filtering ◼️
- [[Link](https://m.researching.cn/articles/OJe0757400bd253676/referenceandcitations)] Method for Filtering Dense Noise from Laser Scanning Data ◼️
- [[Link](https://ieeexplore.ieee.org/document/8683548)] Denoising of 3D point clouds constructed from light fields ◼️
- [[Link](https://www.sciencedirect.com/science/article/abs/pii/S0167839619300299)] A novel anisotropic second order regularization for mesh denoising ◼️
- [[Link](https://isprs-archives.copernicus.org/articles/XLII-2-W17/217/2019/)] Denoising of 3D Point clouds ◼️
- [[Link](https://arxiv.org/pdf/1904.07615)] Total denoising: Unsupervised learning of 3D point cloud cleaning (TD) [[code](https://github.com/phermosilla/TotalDenoising)] 🔸 `un.`
- [[Link](https://ieeexplore.ieee.org/document/8901695)] 3D Point Cloud Color Denoising Using Convex Graph-Signal Smoothness Priors ◼️ `var.`
  
# 2020
- [[Link](https://ieeexplore.ieee.org/document/9026751)] Feature Graph Learning for 3D Point Cloud Denoising (FGL) ◼️
- [[Link](https://ieeexplore.ieee.org/document/8976421)] Point Cloud Denoising via Feature Graph Laplacian Regularization ◼️ `var.`
- [[Link](https://arxiv.org/pdf/2002.05968)] Pointfilter: Point Cloud Filtering via Encoder Decoder Modeling [[code](https://github.com/dongbo-BUAA-VR/Pointfilter)] 🔹
- [[Link](https://arxiv.org/pdf/2003.06631)] Non-Local Part-Aware Point Cloud Denoising ◼️
- [[Link](https://iopscience.iop.org/article/10.1088/1757-899X/768/7/072041/pdf)] Research on denoising algorithm of 3D point cloud data based on curvature change ◼️
- [[Link](https://www.computer.org/csdl/proceedings-article/iccst/2020/813800a123/1p1gtJQEUPC)] Point Cloud Denoising Algorithm Based on Noise Classification ◼️
- [[Link](https://ieeexplore.ieee.org/document/9309029)] Learning robust graph-convolutional representations for point cloud denoising ◼️
- [[Link](https://www.researchgate.net/publication/334846348_3D_point_cloud_registration_denoising_method_for_human_motion_image_using_deep_learning_algorithm)] 3D point cloud registration denoising method for human motion image using deep learning algorithm ◼️
- [[Link](https://arxiv.org/pdf/1912.03874)] CNN-based Lidar Point Cloud De-Noising in Adverse Weather [[code](https://github.com/rheinzler/PointCloudDeNoising)] 🔸
- [[Link](https://www.sciencedirect.com/science/article/abs/pii/S0010448520300506)] A feature-preserving framework for point cloud denoising ◼️
- [[Link](https://www.mdpi.com/1424-8220/20/11/3206)] Sparse Regularization-Based Approach for Point Cloud Denoising and Sharp Features Enhancement ◼️ `var.`
- [[Link](https://www.sciencedirect.com/science/article/abs/pii/S0010448520300531)] Deep feature-preserving normal estimation for point cloud filtering ◼️
- [[Link](https://arxiv.org/pdf/2004.04242)] Deep Manifold Prior ◼️
- [[Link](https://www.researchgate.net/publication/345665258_Edge-guided_second-order_total_generalized_variation_for_Gaussian_noise_removal_from_depth_map)] Edge-guided second-order total generalized variation for Gaussian noise removal from depth map 🔹 `var.`
- [[Link](https://www.sciencedirect.com/science/article/pii/S0924271620300046)] Noise-robust transparent visualization of large-scale point clouds acquired by laser scanning ◼️
- [[Link](https://ieeexplore.ieee.org/document/9287341)] 3D Point Cloud Denoising Using a Joint Geometry and Color k-NN Graph ◼️
- [[Link](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123650103.pdf)] Learning Graph-Convolutional Representations for Point Cloud Denoising (GPDNet) [[code](https://github.com/diegovalsesia/GPDNet)] 🔹
- [[Link](https://arxiv.org/pdf/2007.13551)] Differentiable Manifold Reconstruction for Point Cloud Denoising [[code](https://github.com/luost26/DMRDenoise)] 🔸 `un.`
- [[Link](https://arxiv.org/pdf/2111.02045)] Deep Point Set Resampling via Gradient Fields [[code](https://github.com/ChenhLiwnl/deep-rs)] 🔹
- [[Link](https://ieeexplore.ieee.org/document/9472930)] Dynamic Point Cloud Denoising via Manifold-to Manifold Distance ◼️
- [[Link](https://ieeexplore.ieee.org/document/9296808)] Mesh Denoising with Facet Graph Convolutions [[code](https://github.com/Elensil/Facet_Graph_Convolution)] 🔹
  
# 2021
- [[Link](https://openaccess.thecvf.com/content/ICCV2021/papers/Luo_Score-Based_Point_Cloud_Denoising_ICCV_2021_paper.pdf)] Score-Based Point Cloud Denoising [[code](https://github.com/luost26/score-denoise)] 🔥 `un.`
- [[Link](https://link.springer.com/article/10.1007/s11263-021-01564-7)] RePCD-Net: Feature-Aware Recurrent Point Cloud Denoising Network [[code](https://github.com/chenhonghua/RePCD-Net)] ◼️
- [[Link](https://www.frontiersin.org/journals/signal-processing/articles/10.3389/frsip.2022.842570/full)] VIPDA: A Visually Driven Point Cloud Denoising Algorithm Based on Anisotropic Point Cloud Filtering ◼️
- [[Link](https://arxiv.org/pdf/2101.02322)] Mesh Total Generalized Variation for Denoising ◼️ `var.`
- [[Link](https://www.sciencedirect.com/science/article/pii/S1047320321000092?dgcid=raven_sd_recommender_email)] Exploiting color for graph-based 3D point cloud denoising ◼️
- [[Link](https://www.mdpi.com/1424-8220/21/11/3703?https://susy.mdpi.com/&gad_source=1&gclid=Cj0KCQiAst67BhCEARIsAKKdWOkK_otZ43ufvO6Hu8fxvQGBWk5pM4ZK54YxdwhDntGlqbAJJBCE-GQaAlkgEALw_wcB)] PCA-Based Denoising Algorithm for Outdoor Lidar Point Cloud Data ◼️
- [[Link](https://webpages.tuni.fi/foi/papers/Anisotropic_Denoising_of_3D_Point_Clouds_by_Aggregation_of_Multiple_Surface_Adaptive_Estimates-prepress.pdf)] Anisotropic Denoising of 3D Point Clouds by Aggregation of Multiple Surface-Adaptive Estimates ◼️
- [[Link](https://ieeexplore.ieee.org/document/9334993)] Joint Geometry and Color Point Cloud Denoising Based on Graph Wavelets ◼️
- [[Link](https://www.sciencedirect.com/science/article/abs/pii/S0031320321003150)] Point cloud denoising using non-local collaborative projections ◼️
  
# 2022
- [[Link](https://www.mdpi.com/2072-4292/14/2/367)] Single-Stage Adaptive Multi-Scale Point Cloud Noise Filtering Algorithm Based on Feature Information ◼️
- [[Link](https://arxiv.org/pdf/2210.15913)] GeoGCN: Geometric Dual-domain Graph Convolution Network for Point Cloud Denoising ◼️
- [[Link](https://caoxin918.github.io/files/%E5%BE%90%E9%9B%AA%E4%B8%BDAO.pdf)] TDNet: transformer-based network for point cloud denoising ◼️
- [[Link](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136630392.pdf)] PD-Flow: A Point Cloud Denoising Framework with Normalizing Flows [[code](https://github.com/unknownue/pdflow)] `dl.` ◼️
- [[Link](https://link.springer.com/article/10.1007/s00530-022-00936-4)] Point cloud denoising algorithm with geometric feature preserving ◼️
- [[Link](https://www.mdpi.com/1999-4893/15/4/124)] Point Cloud Upsampling Algorithm: A Systematic Review ◼️ `surv.`
- [[Link](https://www.semanticscholar.org/reader/524b518d34a672f8f84ba7b139aff00b763464d0)] Dynamic Point Cloud Denoising via Gradient Fields ◼️
- [[Link](https://www.semanticscholar.org/paper/Structure-Aware-Denoising-for-Real-world-Noisy-with-Sun-Chu/5da3a477363e6a3f303b5402dbe62011deb53a4f)] Structure-Aware Denoising for Real-world Noisy Point Clouds with Complex Structures [[code](https://github.com/rg089/SCANING)] ◼️
- [[Link](https://ieeexplore.ieee.org/document/9998112)] From Noise Addition to Denoising: A Self-Variation Capture Network for Point Cloud Optimization ◼️
- [[Link](https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.14661)] MODNet: Multi-offset Point Cloud Denoising Network Customized for Multi-scale Patches [[code](https://github.com/hay-001/MODNet)] ◼️
- [[Link](https://www.sciencedirect.com/science/article/abs/pii/S1524070322000170)] Point cloud denoising review: from classical to deep learning-based approaches 🌟 `surv.`
- [[Link](https://www.mdpi.com/1424-8220/22/7/2666)] Denoising for 3D Point Cloud Based on Regularization of a Statistical Low-Dimensional Manifold ◼️
- [[Link](https://www.mdpi.com/2072-4292/14/3/577)] Reflective Noise Filtering of Large-Scale Point Cloud Using Transformer ◼️
- [[Link](https://iopscience.iop.org/article/10.1088/1742-6596/2383/1/012080/pdf)] Optimization of point cloud preprocessing algorithm for equipped vehicles ◼️
- [[Link](https://par.nsf.gov/servlets/purl/10443276)] Motion estimation and filtered prediction for dynamic point cloud attribute compression ◼️
- [[Link](https://arxiv.org/abs/2211.10023)] LiSnowNet: Real-time Snow Removal for LiDAR Point Cloud ◼️
- [[Link](https://arxiv.org/pdf/2203.03311)] Comprehensive Review of Deep Learning-Based 3D Point Cloud Completion Processing and Analysis 🔹 `surv.`
- [[Link](https://www.mdpi.com/2072-4292/15/1/115)] A Method Based on Improved iForest for Trunk Extraction and Denoising of Individual Street Trees ◼️

# 2023
- [[Link](https://arxiv.org/pdf/2208.06811)] Contrastive Learning for Joint Normal Estimation and Point Cloud Filtering [[code](https://github.com/ddsediri/CLJNEPCF)] ◼️
- [[Link](https://ieeexplore.ieee.org/document/9693131)] Refine-Net: Normal Refinement Neural Network for Noisy Point Clouds [[code](https://github.com/hrzhou2/refinenet)] ◼️
- [[Link](https://www.semanticscholar.org/paper/Point-Cloud-Denoising-Algorithm-via-Geometric-on-Duan-Feng/0deb0dd5f748b350943c538c53cc11fdbc33fe78)] Point Cloud Denoising Algorithm via Geometric Metrics on the Statistical Manifold ◼️
- [[Link](https://iopscience.iop.org/article/10.1088/1742-6596/2383/1/012080/pdf)] Optimization of point cloud preprocessing algorithm for equipped vehicles ◼️
- [[Link](https://arxiv.org/pdf/2209.07121)] 4DenoiseNet: Adverse Weather Denoising From Adjacent Point Clouds [[code](https://github.com/alvariseppanen/4DenoiseNet)] ◼️
- [[Link](https://ieeexplore.ieee.org/document/10226976)] 3D Point Cloud Denoising Algorithm Based on Two-Stage Filtering ◼️
- [[Link](https://www.researchgate.net/publication/377903007_Attention_Mechanism-Based_Deep_Learning_Denoising_of_Scanned_Point_Cloud_for_Rocket_Tank_Panel)] Attention Mechanism-based Deep Learning Denoising of Scanned Point Cloud for Rocket Tank Panel ◼️
- [[Link](https://arxiv.org/pdf/2304.11812)] NoiseTrans: Point Cloud Denoising with Transformers ◼️
- [[Link](https://www.sciencedirect.com/science/article/pii/S0031320323000675?dgcid=raven_sd_recommender_email)] A single-stage point cloud cleaning network for outlier removal and denoising ◼️
- [[Link](https://ieeexplore.ieee.org/document/9543583)] GeoDualCNN: Geometry Supporting Dual Convolutional Neural Network for Noisy Point Clouds ◼️
- [[Link](https://arxiv.org/abs/2305.05991)] DMNR: Unsupervised De-noising of Point Clouds Corrupted by Airborne Particles ◼️
- [[Link](https://ieeexplore.ieee.org/document/10114488)] MSaD-Net: A Mix Self-Attention Networks for 3D Point Cloud Denoising ◼️
- [[Link](https://www.sciencedirect.com/science/article/abs/pii/S0263224123001562)] Parameter optimization for point clouds denoising based on no-reference quality assessment ◼️
- [[Link](https://www.mdpi.com/2072-4292/15/1/269)] Multiscale Feature Fusion for the Multistage Denoising of Airborne Single Photon LiDAR ◼️
- [[Link](https://www.sciencedirect.com/science/article/pii/S1350449523001822)] Bilateral filter denoising of Lidar point cloud data in automatic driving scene ◼️
- [[Link](https://ieeexplore.ieee.org/document/10173632)] PCDNF: Revisiting Learning-based Point Cloud Denoising via Joint Normal Filtering [[code](https://github.com/LabZhengLiu/PCDNF)] ◼️
- [[Link](https://arxiv.org/pdf/2202.10094)] Point Cloud Denoising via Momentum Ascent in Gradient Fields [[code](https://github.com/IndigoPurple/MAG)] ◼️
- [[Link](https://iopscience.iop.org/article/10.1088/1361-6501/ad044d)] 3D point cloud global denoising algorithm based on different noise characteristics ◼️
- [[Link](https://link.springer.com/article/10.1007/s00371-022-02698-6)] 3D point cloud denoising using anisotropic neighborhoods and a novel sharp feature detection algorithm [[code](https://git.tecgraf.puc-rio.br/hurtado/point_cloud_denoising_tvcj)] ◼️
- [[Link](https://openaccess.thecvf.com/content/CVPR2023/papers/de_Silva_Edirimuni_IterativePFN_True_Iterative_Point_Cloud_Filtering_CVPR_2023_paper.pdf)] IterativePFN: True Iterative Point Cloud Filtering [[code](https://github.com/ddsediri/IterativePFN)] ◼️
- [[Link](https://dl.acm.org/doi/abs/10.1016/j.patcog.2023.109569)] A Noising-Denoising Framework for Point Cloud Upsampling via Normalizing Flows ◼️
- [[Link](https://www.researchgate.net/publication/376817692_TP-NoDe_Topology-aware_Progressive_Noising_and_Denoising_of_Point_Clouds_towards_Upsampling)] TP-NoDe: Topology-aware Progressive Noising and Denoising of Point Clouds towards Upsampling ◼️
- [[Link](https://ieeexplore.ieee.org/document/10095488)] Graph-Based Point Cloud Color Denoising with 3-Dimensional Patch-Based Similarity ◼️
- [[Link](https://link.springer.com/article/10.1007/s42791-023-00058-6)] Deep learning-based point cloud upsampling: a review of recent trends ◼️ `surv.` 
- [[Link](https://link.springer.com/article/10.1007/s00371-023-03158-5)] 3D point cloud denoising method based on global feature guidance ◼️

# 2024
- [[Link](https://arxiv.org/pdf/2401.09721)] Fast graph-based denoising point cloud color information ◼️
- [[Link](https://www.mdpi.com/2071-1050/16/5/2077)] Three-Dimensional Point Cloud Denoising for Tunnel Data by Combining Intensity and Geometry Information ◼️
- [[Link](https://arxiv.org/pdf/2307.10875)] PointCVaR: Risk-optimized Outlier Removal for Robust 3D Point Cloud Classification [[code](https://github.com/shinke-li/pointcvar)] ◼️
- [[Link](https://www.mdpi.com/2072-4292/16/13/2347)] Point Cloud Denoising in Outdoor Real-World Scenes Based on Measurable Segmentation ◼️
- [[Link](https://ieeexplore.ieee.org/document/10303185)] Transformer-based Point Cloud Denoising Network ◼️
- [[Link](https://arxiv.org/abs/2404.05522v1)] 3DMambaIPF: A State Space Model for Iterative Point Cloud Filtering via Differentiable Rendering ◼️
- [[Link](https://3d.bk.tudelft.nl/liangliang/publications/2024/pathnet/PathNet.pdf)] PathNet: Path-Selective Point Cloud Denoising [[code](https://github.com/ZeyongWei/PathNet)] ◼️
- [[Link](https://www.researchgate.net/publication/382355164_The_implementation_method_of_point_cloud_denoising_filter_based_on_KinectV2/fulltext/6699306c02e9686cd10d945b/The-implementation-method-of-point-cloud-denoising-filter-based-on-KinectV2.pdf)] The implementation method of point cloud denoising filter based on KinectV2 ◼️
- [[Link](https://openaccess.thecvf.com/content/CVPR2024/html/Mao_Denoising_Point_Clouds_in_Latent_Space_via_Graph_Convolution_and_CVPR_2024_paper.html)] Denoising Point Clouds in Latent Space via Graph Convolution and Invertible Neural Network [[code](https://github.com/yanbiao1/PD-LTS?tab=readme-ov-file)] ◼️
- [[Link](https://www.mdpi.com/2072-4292/16/23/4559)] Hybrid Denoising Algorithm for Architectural Point Clouds Acquired with SLAM Systems ◼️
- [[Link](https://www.sciencedirect.com/science/article/pii/S0167865524002101)] Self-supervised multi-echo point cloud denoising in snowfall [[code](https://github.com/alvariseppanen/SMEDen)] ◼️
- [[Link](https://www.sciencedirect.com/science/article/abs/pii/S0010448524000356)] Denoising point clouds with fewer learnable parameters ◼️
- [[Link](https://www.researching.cn/articles/OJeb4150232c7fa1bc)] Review of 3D Point Cloud Processing Methods Based on Deep Learning ◼️ `surv.` 
- [[Link](https://www.mdpi.com/2072-4292/16/15/2714)] A Novel Point Cloud Adaptive Filtering Algorithm for LiDAR SLAMinForest Environments Based on Guidance Information ◼️
- [[Link](https://arxiv.org/pdf/2405.08322)] StraightPCF: Straight Point Cloud Filtering [[code](https://github.com/ddsediri/StraightPCF)] ◼️
- [[Link](https://arxiv.org/pdf/2411.00857)] Deep Learning for 3D Point Cloud Enhancement: A Survey `surv.` ◼️
- [[Link](https://arxiv.org/pdf/2408.13802)] TripleMixer A 3D Point Cloud Denoising Model or Adverse Weather [[code](https://github.com/Grandzxw/TripleMixer)] ◼️
- [[Link](https://arxiv.org/pdf/2408.16325)] P2P-Bridge Diffusion Bridges for 3D Point Cloud [[code](https://github.com/matvogel/P2P-Bridge)] ◼️
- [[Link](https://www.sciencedirect.com/science/article/abs/pii/S0263224124015562)] TPDNet: A point cloud data denoising method for offshore drilling platforms and its application ◼️
- [[Link](https://arxiv.org/abs/2411.14158)] Point Cloud Denoising With Fine-Granularity Dynamic Graph Convolutional Networks ◼️
- [[Link](https://link.springer.com/article/10.1007/s41095-024-0423-3)] Noise4Denoise: Leveraging Noise for Unsupervised Point Cloud Denoising ◼️ `un.`

# 2025
- [[Link](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2024.1490660/full)] LiDAR point cloud denoising for individual tree extraction based on the Noise4Denoise ◼️ `un.`
- [[Link](https://www.researchgate.net/publication/389316228_Noise2Score3DUnsupervised_Tweedie%27s_Approach_for_Point_Cloud_Denoising)] Noise2Score3D:Unsupervised Tweedie's Approach for Point Cloud Denoising ◼️ `un.`

<a href="https://www.star-history.com/#agarnung/awesome-3d-point-cloud-denoising&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=agarnung/awesome-3d-point-cloud-denoising&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=agarnung/awesome-3d-point-cloud-denoising&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=agarnung/awesome-3d-point-cloud-denoising&type=date&legend=top-left" />
 </picture>
</a>

# TODO

- Link arXiv survey
- Create visuales with [NapkinAI](https://www.napkin.ai/) (for example)
