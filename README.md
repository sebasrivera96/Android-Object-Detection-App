# Android-Object-Detection-App

 
## Description

This repository will detail the main steps to modify, prepare and deploy two Android apps regarding object detection and classification on a smartphone:
1. Object classification App with TFLite
2. Object Detection with Tensorflow Object Detection API 

## Requirements

1. Ubuntu 16.04 (Oracle VM VirtualBox)
2. Android Studio 3.1.2
3. Samsung Galaxy S7 (Android 7.0)
  

## Object Detection API on Android

### Step-by-step explanation for training a custom object
#### 1) Data collection
Collect at least 100 images of the object you want to detect. Although the training could be done with 100 images, it is recommended to have 500< images.
#### 2) Data preparation
* Label the images using [LabelImg](https://github.com/tzutalin/labelImg). This process was carried out on Ubuntu 16.04 using Python 3 + Qt5. The label program automatically will create an XML file that describes the pictures. The installation steps are described on the repository. 
* Split data (picture + corresponding XML file) into train and test samples.
* Use the xml_to_csv.py script to convert the files created on step 2.
#### 3) Install Object Detection API & Create TF Records
* Generate TF Records from the CSV files created on the previous step. The script for this step is called **generate_tfrecord.py**. The *class_text_to_int* function should be modified to specify the class or classes for which you are going to train.
```python
def class_text_to_int(row_label):
	if row_label == 'class_1':
		return 1
	elif row_label == 'class_2':
		return 2
	elif row_label == 'class_3':
		return 3
	# Use as many elifs as you need
	else
		None
```
* To run successfully this script there are two options:
	* Run it from the [models](https://github.com/tensorflow/models) repo directory.
	* Install the Object Detection API as explained on [this](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md) page.
#### 4) Prepare configuration file and model checkpoint 
Prepare a [configuration file](https://github.com/tensorflow/models/tree/master/research/object_detection/samples/configs) and a [checkpoint](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) from a pre-trained model. In my case I used the following files: 
* ssd_mobilenet_v1_pets.config
* ssd_mobilenet_v1_coco_11_06_2017.tar.gz

These files should be saved on the `Object-Detection-Preparation` folder. The configuration file that you will found on this repository is modified to train the model on just one object. If you want to train on more than one object, you can see how to properly modify the configuration file [here](https://pythonprogramming.net/training-custom-objects-tensorflow-object-detection-api-tutorial/?completed=/creating-tfrecord-files-tensorflow-object-detection-api-tutorial/).
#### Internal structure of the directory
The folders (of course also the subfolders) and files maked in **bold font** within this directory will be merged on the **step 5** with the `models/research/object_detection` folder, so be aware of the structure and the files that should be copied, otherwise the training will fail.
* Object-Detection-Preparation
	* **data/**
		* test_labels.csv
		* train_labels.csv
	* **images/**
		* test/
			* test_img1.jpg
			* ...
			* test_imgN.jpg
		* train/
			* train_img1.jpg
			* ...
			* train_imgN.jpg
	* **training/**
	* **ssd_mobilenet_v1_coco_11_06_2017**
	* **ssd_mobilenet_v1_pets.config**
	* renameFiles.py
	* ssd_mobilenet_v1_coco_11_06_2017.tar.gz
	* xml_to_csv.py
	
#### 5) Train 
There are two options to train the model. One is to use transfer learning, which is the method that will be used in this tutorial. The other one is learning from scratch. The difficulties of the latter is that you need much more data and time to obtain good results. It is possible to train with either a CPU or a GPU, but the difference is huge. For the first version of the App both options where used. To have a **TotalLoss** below 1.5  it took for the former around 8 hours, whereas for the latter it took less than two hours. 

For the training to run successfully, the following folders from the `Object-Detection`
```bash

python3 train.py --logtostderr \

--train_dir=training/ \

--pipeline_config_path=training/ssd_mobilenet_v1_pets.config

```
For more details on this step, checkout [this](https://youtu.be/JR8CmWyh2E8) video.
#### 6) Export inference graph into Android Studio TODO
To test the trained model, we need to export the graph generated on previous step to use it on the Android App. You should identify the latest checkpoint which has 3 files with the same step number. Also, in the `models/research/object_detection` directory you will find a script called `export_inference_graph.py` which is used to exported the new trained model. 
```bash
python3 export_inference_graph.py \

--input_type image_tensor \

--pipeline_config_path training/ssd_mobilenet_v1_pets.config \

--trained_checkpoint_prefix training/model.ckpt-52001 \

--output_directory Continental_logo_inference_graph

```
In [this](https://youtu.be/srPndLNMMpk) video you can have a more detailed explanation. The output file is called `frozen_inference_graph.pb`.

At this moment you need to have installed Android Studio. If you don't have it yet, download and install it [here](https://developer.android.com/studio/). Besides Android Studio, the official [tensorflow](https://github.com/tensorflow/tensorflow.git) repository should be cloned. Once cloned, select *File/Open...* on Android Studio to open and **build** the demo App that will be find under `tensorflow/tensorflow/examples/android/`. I recommend reading the README file to get familiarized with the main characteristics.

After the project was build successfully, finally is time to modify the App. The `frozen_inference_graph.pb` should be added to the `android/assets/` directory. Also a file called *labels.txt* should be created on the same directory. In the first line simple write **???** and in the following lines the label of the object or objects for which you trained your model. In my case the I wrote **Continental_logo** on the second line. 

The last step before clicking the **run** button and playing around with the App, the `java/DetectionActivity.java` file must be modified. Search for the variable `TF_OD_API_MODEL_FILE` and change its value to the name of the new frozen model (the one located in the assets folder). Also change the value of the `TF_OD_API_LABELS_FILE` variable to the name of the labels file. At this moment you are ready to deploy the App on your smartphone and play around with it.
### Every time usage commands 
Every time Object Detection API will be used, it doesn't matter if it is the 1st or the 10th time, these commands need to be executed from the `models/research/` directory. Before using any other script. Otherwise it will fail.
```bash

protoc object_detection/protos/*.proto --python_out=.

```
```bash

export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

```

### Credits 
To achieve this goal, two projects were followed along the developing process. For more details on each of the steps, checkout these out:
1. [Tensorflow Object Detection API Tutorial](https://pythonprogramming.net/introduction-use-tensorflow-object-detection-api-tutorial/) from **Stendex**
2. [Detecting Pikachu on Android using Tensorflow Object Detection](https://towardsdatascience.com/detecting-pikachu-on-android-using-tensorflow-object-detection-15464c7a60cd) from **Juan De Dios Santos**

### Other NN Architectures TODO
* SqueezeDet is developed on TF and seems to ve optimized for Object Detection.
* [This](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/defining_your_own_model.md) link contains useful information for configuring a new model on the Object Detection API.


