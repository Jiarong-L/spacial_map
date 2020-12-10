import novosparc
import time
import numpy as np
from scipy.spatial.distance import cdist
from scipy.stats import pearsonr

if __name__ == '__main__':

dataset_path = '/sibcb1/zenganlab1/shenrong/output/project_regeneration_20201020/table/expr_matrix_10day_log_normalized.txt' # this could be the dge file, or also can be a 10x mtx folder
output_folder = '~' # folder to save the results, plots etc.
tissue_path = '/sibcb1/zenganlab1/shenrong/output/project_regeneration_20201020/public_data/day10_画板 1.png'
hvg_path = '/sibcb1/zenganlab1/shenrong/output/project_regeneration_20201020/public_data/high_variable_genes_10day.txt'
location_marker = '/sibcb1/zenganlab1/shenrong/output/project_regeneration_20201020/public_data/dge_full.txt'
dataset = novosparc.io.load_data(dataset_path)
# Optional: downsample number of cells to speed up
cells_selected, dataset = novosparc.pp.subsample_dataset(dataset, min_num_cells=5, max_num_cells=1000)
dataset.raw = dataset # this stores the current dataset with all the genes for future use
dataset, hvg = novosparc.pp.subset_to_hvg(dataset, hvg_file = hvg_path) 

# plot some genes and save them
gene_list_to_plot = ['SMED30011970', #eye and head, dd_4427
'SMED30030642', #pharynx
'SMED30001882',#brain and phx
'SMED30005457', #super strong; big cells around the gut
'SMED30000013', #gut
'SMED30010123', #protonephridia
'SMED30016244', #secretory cells?
'SMED30011490' #epithelium
]

#########################################
# 1. use top 2000 DEG in scRNAseq && location figure ###
#########################################
# Optional: Subset to the highly variable genes
#Load location from png file
locations = novosparc.geometry.create_target_space_from_image(tissue_path)
#setup and spatial reconstruction
tissue = novosparc.cm.Tissue(dataset=dataset, locations=locations, output_folder=output_folder) #create a tissue object
tissue.setup_reconstruction(num_neighbors_s = 5, num_neighbors_t = 5) #这两个参数调大一点可以结果更准确
tissue.reconstruct(alpha_linear=0)
tissue.calculate_spatially_informative_genes()


path = output_folder + '/top2000DEG_with_location_fig1'
isExists=os.path.exists(path)
if not isExists:
	os.makedirs(path)
# save the sdge to file
novosparc.io.write_sdge_to_disk(tissue, path)
novosparc.io.save_gene_pattern_plots(tissue=tissue, gene_list_to_plot=gene_list_to_plot, folder=path)
novosparc.io.save_spatially_informative_gene_pattern_plots(tissue=tissue, gene_count_to_plot=10, folder=path)
