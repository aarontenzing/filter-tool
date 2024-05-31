# Neural Network for Filtering

This documentation provides a overview of the process for using the trained ResNet18 model to classify synthetic images into 'good' or 'bad' categories. 
It explains how to use the model.ipynb notebook to perform inference on a designated folder of images and save the filtered results into another folder.
Overview

The model.ipynb notebook contains a pre-trained ResNet18 neural network model. This model has been specifically trained to classify synthetic images based on their quality into two categories: 'good' and 'bad'. 
The primary application of this model is to filter out undesirable images from a batch of synthetically generated content, thus enhancing the quality of datasets used in further applications.
Requirements

# Step
1. Copy your synthetic images to the sort_images/ directory
2. Run the code blocks in the model.ipynb notebook, except these for Training
3. The good images will be copied to results/good/ directory
4. Done!
 
