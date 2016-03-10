import pdb
import calcROI
from matplotlib import pyplot
from matplotlib import cm

#Function to detect the heart region in all the given images
def detect_heart_region(images):
    #(num_slices, num_times, width,height) = images.shape
    rois,circles  = calcROI.calc_rois(images)
      

    return rois,circles;
