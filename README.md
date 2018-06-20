# Android-Object-Detection-App

 
## Description

This repository will detail the main steps to modify, prepare and deploy two Android apps regarding object detection and classification on a smartphone:
1. Object classification App with TFLite
2. Object Detection with Tensorflow Object Detection API 

## Requirements

1. Ubuntu 16.04 (Oracle VM VirtualBox)
2. Android Studio 3.1.2
3. Samsung Galaxy S7 (Android 7.0)

## Object Classification App with TFLite

Below are described in detail the steps that should be followed to place the

Object Classification application in a mobile phone:

1. Download and install Android Studio. Make sure there is a stable Internet connection because the IDE will download some files.

2. Clone the [TensorFlow for poets 2](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0) repository. *(TensorFlow for poets 2 is a step-by-step tutorial to retrain a model in order to identify a group of specific objects. This is beyond our scope.)*

```bash

git clone https://github.com/googlecodelabs/tensorflow-for-poets-2

```

3. Open the **tensorflow-for-poets-2/android/tflite** project, which is located in the repository that was downloaded, on Android Studio and Sync Project with Gradle Files with a button on the right-top corner of the UI.

4. Once the sync finished, the phone needs to have Developer options activated and [USB debugging](https://www.howtogeek.com/129728/how-to-access-the-developer-options-menu-and-enable-usb-debugging-on-android-4.2/) should be turned on.

5. Plug in the smartphone and select it from Devices/USB/ list. Go back to Android Studio and click the green play button in the top-right corner. A screen will pop up where you can select the Android device. Double click on it and the installation will begin.

6. On the Android device, some permissions must be accepted for the App to begin working. The 3 most likely objects with their respective probability will appear at the bottom of the screen.

  

## Object Detection API on Android

### Step-by-step explanation for training a custom object

The steps for the tutorial were retrieved from here: https://pythonprogramming.net/custom-objects-tracking-tensorflow-object-detection-api-tutorial/
#### 1) Data collection
Collect at least 100 images of the object you want to detect. Although the training could be done with 100 images, it is recommended to have 500< images.
#### 2) Data preparation
a. Label the images using [LabelImg](https://github.com/tzutalin/labelImg). This process was carried out on Ubuntu 16.04 using Python 3 + Qt5. The label program automatically will create an XML file that describes the pictures. The installation steps are described on the repository. 
b. Split data (picture + corresponding XML file) into train and test samples.
c. Use the xml_to_csv.py script to convert the files created on step 2.
#### 3) Install Object Detection API & Create TF Records
5. Generate TF Records from the datasets.
#### 4) Prepare configuration file and and model
6. Setup a configuration file from the model, e.g. SSD-Mobilenet.
#### 5) Train
7. Train (CPU or GPU)
The difference between training on a CPU or GPU is huge. For the version 1 of the App both options where used. 
*Is it necessary to specify where it was trained?*
#### 6) Export inference graph into Android Studio
8. Export graph generated on previous step to use it on the Android App while performing inference.
https://towardsdatascience.com/detecting-pikachu-on-android-using-tensorflow-object-detection-15464c7a60cd

```bash

protoc object_detection/protos/*.proto --python_out=.

```

```bash

export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

```

### Internal structure of the directory

* Object-Detection
	* data/
		* test_labels.csv
		* train_labels.csv
	* images/
	* test/
		* test_img1.jpg
		* ...
		* test_imgN.jpg
	* train/
		* train_img1.jpg
		* ...
		* train_imgN.jpg
	* training/
	* xml_to_csv.py
	* renameFiles.py

### TODO List

- [ ] Add link to the generatetfRecords.py script
- [ ] Add a Credits section with the two projects followed 
- [ ] Train on other objects different to the Continental Logo
- [ ] Train on other Neural Network architectures

### Other NN Architectures
* SqueezeDet is developed on TF and seems to ve optimized for Object Detection.
* [This](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/defining_your_own_model.md) link contains useful information for configuring a new model on the Object Detection API.

```bash

python3 train.py --logtostderr \

--train_dir=training/ \

--pipeline_config_path=training/ssd_mobilenet_v1_pets.config

```

```bash

python3 export_inference_graph.py \

--input_type image_tensor \

--pipeline_config_path training/ssd_mobilenet_v1_pets.config \

--trained_checkpoint_prefix training/model.ckpt-52001 \

--output_directory Continental_logo_inference_graph

``` 