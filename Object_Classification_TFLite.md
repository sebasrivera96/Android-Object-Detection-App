# Object Classification App with TFLite

## Description

This repository will detail the main steps to modify, prepare and deploy a **Object classification App with TFLite** on a smartphone.

## Main Steps

Below are described in detail the steps that should be followed to place the Object Classification application on a mobile phone:

1. Download and install Android Studio. Make sure there is a stable Internet connection because the IDE will download some files.

2. Clone the [TensorFlow for poets 2](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0) repository. *(TensorFlow for poets 2 is a step-by-step tutorial to retrain a model in order to identify a group of specific objects. This is beyond our scope.)*

```bash

git clone https://github.com/googlecodelabs/tensorflow-for-poets-2

```

3. Open the **tensorflow-for-poets-2/android/tflite** project, which is located in the repository that was downloaded, on Android Studio and Sync Project with Gradle Files with a button on the right-top corner of the UI.

4. Once the sync finished, the phone needs to have Developer options activated and [USB debugging](https://www.howtogeek.com/129728/how-to-access-the-developer-options-menu-and-enable-usb-debugging-on-android-4.2/) should be turned on.

5. Plug in the smartphone and select it from Devices/USB/ list. Go back to Android Studio and click the green play button in the top-right corner. A screen will pop up where you can select the Android device. Double click on it and the installation will begin.

6. On the Android device, some permissions must be accepted for the App to begin working. The 3 most likely objects with their respective probability will appear at the bottom of the screen.
