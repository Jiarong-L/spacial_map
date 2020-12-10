# spatial_map
Playing around with novosparc(0.4.1)   

### pre-precessing.ipynb  --- prepare target_shape and marker_info
1. Extract FISH images and reshape them to disired shape.  
2. Select the coordinates of disired shape and save them in .npy (e.g. (y,x) according to novosparc's loading method)  
3. For those selected points in step 2, mark 1 if FISH image is in this region, otherwise mark 0. Save the results in atlas.txt, while each column repersents one gene. 

### mynovosparc.ipynb
Run novosparc with dge_matrix.txt and atlas.txt  
In our case, each row represents a cell, and each column represents a gene.  



