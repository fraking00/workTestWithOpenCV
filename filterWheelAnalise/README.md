# Construction of Multiple color mask by a basic frame with OpenCV in Python

### using webcam

This code is based on the base tutorial of OpenCV, but it aims at creating multiple color masks and comparing between them using "and" and "or".

In this code there are the white, yellow and blue filters and they are recognized by the use of the lower and upper limit of the color scale.

The res with a color next to it are the base color filter.

The res_sum is the sum of all with the use of or so it result as the composition of all the filters.

The res_Wcommon_allfilter is what ther is in common using the and between all the filter and normally it results in a black frame.

The last one is res_Wcommon_WhandY that is the comparison between white and yellow filter and normally if you use a light to enlighten the yellow object there is always a common spot between yellow and white filter.










