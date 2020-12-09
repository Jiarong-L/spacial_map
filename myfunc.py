import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import morphology



def clip_background(arr,subarr,denoise1 = 5,denoise2 = 3):  
    '''
    Input: 2D binary arrays, subarr can be void 
    Output: 2D binary arrays -clipped version
    
    clip line&rows all is 1 (background) in arr,
    apply the same clipping pattern to subarr
    '''
    row_drop = []
    for i in range(arr.shape[0]):
        if arr[i].sum()>=arr.shape[1]-denoise1:
            row_drop.append(i)
    arr = np.delete(arr, row_drop, 0)  
    if len(subarr)!=0:
        subarr = np.delete(subarr, row_drop, 0)

    line_drop = []
    for i in range(arr.shape[1]):
        if arr[:,i].sum()>=arr.shape[0]-denoise2:
            line_drop.append(i)
    arr = np.delete(arr, line_drop, 1) 
    if len(subarr)!=0:
        subarr = np.delete(subarr, line_drop, 1)
        
    return arr,subarr



def cv2plot(arr,font = 'myplot'):
    cv2.imshow(font, arr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass


def set_borders_zero(arr,border_width = 3):
    i = border_width
    arr[:i,:] = np.zeros(arr[:i,:].shape)
    arr[-i:,:] = np.zeros(arr[-i:,:].shape)
    arr[:,:i] = np.zeros(arr[:,:i].shape)
    arr[:,-i:] = np.zeros(arr[:,-i:].shape)    
    return arr


# 0,1等比收放
def resize_by_ratio(arr,target_arr):
    a = arr
    t = target_arr
    ratio = t.shape[0]/a.shape[0]
    his = -999
    index_list = []
    check_list = []
    for i in range(len(a)):
        if a[i]!=his:
            index_list.append(i)
            check_list.append(a[i])
            his = a[i]

    new_index_list = [int(round(ratio * i,0)) for i in index_list]
    new_index_list.append(len(t))

    res = np.array([-999 for i in range(len(t))])
    for i in range(len(new_index_list)-1):
        res[new_index_list[i]:new_index_list[i+1]] = check_list[i]
    
    if len(res)!=len(target_arr):
        print('unequal!!!')
    
    return res

# a = np.array([1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1])
# t = np.array([0,0,0,0,0,0,0,0,0,0,0,0])
# r = resize_by_ratio(a,t)
# print(t)
# print(r)




# np.where(arr == 0)[0].shape[0] 求每行的图像大小，resize相关区域后定位，两边加1。。

def morph_line(d,s,t): # input are lines
    
    source = d
    subsource = s
    target = t
    
    # index list of pos eqal zero
    s_ind = np.where(source == 0)[0]
    t_ind = np.where(target == 0)[0]
    # process it in case it is not continious Todo: dilate the image to see if there are contamination??
    s_ind = [i for i in range(s_ind[0],s_ind[-1]+1)]
    t_ind = [i for i in range(t_ind[0],t_ind[-1]+1)]
    
    # lists to be resizes
    slist = source[s_ind]
    sublist = subsource[s_ind] # the same pos/len as in source
    tlist = target[t_ind]

    # lists after resize
    new_slist = resize_by_ratio(slist,tlist)
    new_sublist = resize_by_ratio(sublist,tlist)
    
    # pos of resized region
    pos_s = t_ind[0]
    pos_end = t_ind[-1]+1
    len_target = target.shape[0]
    
    # place things back
    new_source = [1 for i in range(len_target)]
    new_subsource = [0 for i in range(len_target)]
    
    new_source[pos_s:pos_end] = new_slist
    new_subsource[pos_s:pos_end] = new_sublist
    
    return new_source,new_subsource

# source =    np.array([1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1])
# subsource = np.array([1,1,1,1,1,0,0,1,0,0,1,1,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1])
# target=     np.array([1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1])

# morph_line(source,subsource,target)



