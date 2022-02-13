# Scanbage
## What it does
- A Web App to sort your waste via scanning the uploaded images
- Classifies the waste material in the image into 6 categories :
  1. Cardboard
  2. Glass
  3. Metal
  4. Paper
  5. Plastic
  6. Trash
- The results of tells if the item should be recycled, composted, put into the general trash or needs special treatment (hazardous materials)
- Tells the information on how much CO2 emission they avoided

## How to use
* Click **Login** to start with a free account

[]

* Click **Explore** to start

[]

* **Choose** an image to be uploaded

[]

* **Upload** the file

[]

* Get the result within seconds with atmost accuracy

[]

## How was it built
- Pre-Trained image detection model **DenseNet-121**
- DenseNet-121 is pre-trained on **ImageNet** to distinguish 1000 classes of objects
- Dataset is trained using **VGG16 Transfer Learning Technique** of CNN for the classification
