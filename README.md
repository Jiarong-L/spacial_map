# spatial_map
Playing around with novosparc(0.4.1)   .... and failed to get valid results.

### pre-precessing.ipynb  --- prepare target_shape and marker_info (in 2D)
1. Extract FISH images and reshape them to target shape.  
2. Select the coordinates of target shape and save them in .npy (e.g. (y,x) according to novosparc's loading method)  
3. For those selected points in step 2, mark 1 if FISH image is in this region, otherwise mark 0. Save the results in atlas.txt, while each column repersents one gene. 

### mynovosparc_2D.ipynb
Run novosparc with dge_matrix.txt and atlas.txt  
In our case, each row represents a cell, and each column represents a gene.  


### generate_3D&fake_marker.ipynb
Generate a fake planarian in 3D space (i.e. an ellipsoid?)    
Generate fake 3D marker of epithelium and another organ (insude body)  


### mynovosparc_3D&fake_epi33119.ipynb
Run novosparc with dge_matrix.txt and the 2 fake 3D markers   






