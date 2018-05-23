# ConcScan
Python library with tools for determining concentration of tracers leached from a dye pad

## Included methods
### ConcScan.imageData
calculates and returns light absorbance array for a given image

### ConcScan.conc
calculates and returns concentration array for a given absorbance array

### ConcScan.plotData
given two arrays, plot them against each other and display 

### ConcScan.exportData
given two arrays, export them to a newly created csv file with the headers 1) "Absorbance" and 2) "Concentration"


## Dependencies
PIL

numpy

matplotlib

os
