# Test code for detect heart region
import detectHeartRegion as dhr

from matplotlib import pyplot
from matplotlib import cm
from Dataset import Dataset


d = Dataset("C:\\Kaggle\\train\\27", "27");
d.load();
(num_slices, num_times, width,height) = d.images.shape

rois,circles = dhr.detect_heart_region(d.images);


#plot roi in each slice at time 0
numSlicesToDisplay = 10;
pyplot.figure(1);
pyplot.subplots_adjust(left=0.1,hspace=0.1,wspace=0);

numslicesPerRow = 2;
numRows = numSlicesToDisplay/numslicesPerRow;
index = 1;
for slice in range(numSlicesToDisplay):
    pyplot.subplot(numRows,2 * numslicesPerRow, index );
    pyplot.imshow(d.images[slice][0],cmap=cm.Greys_r);
    index = index + 1;
    
    pyplot.subplot(numRows,2 * numslicesPerRow, index) ;
    pyplot.imshow(rois[slice],cmap=cm.Greys_r);
    index = index + 1;

#todo use subfigure    
pyplot.show();
    

