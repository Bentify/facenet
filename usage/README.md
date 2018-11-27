# FaceNet Usage

This folder demonstrates how to use the FaceNet framework.

Pre-requisites:
	1. Install PIP packages
	   Go to facenet directory and run "pip install -r requirements.txt"
	2. Download the models, unzip and put inside facenet\usage\models
	   https://drive.google.com/open?id=1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-
	   https://drive.google.com/open?id=1R77HmFADxe87GmoLwzfgMu_HY0IhcyBz

Training:
	1. Add photos in facenet\usage\datasets\train
	2. Execute train.bat
	   ::python ../src/classifier.py TRAIN datasets\train models\20180408-102900\20180408-102900.pb models\datasets_classifier.pkl --batch_size 1000
	   python ../src/classifier.py TRAIN datasets\train models\20180402-114759\20180402-114759.pb models\datasets_classifier.pkl --batch_size 1000

Testing:
	1. Add photos in facenet\usage\datasets\test
	2. Execute test.bat
	   ::python ../src/classifier.py CLASSIFY datasets\test models\20180408-102900\20180408-102900.pb models\datasets_classifier.pkl
	   python ../src/classifier.py CLASSIFY datasets\test models\20180402-114759\20180402-114759.pb models\datasets_classifier.pkl

Testing w/a webcam:
	1. Connect a webcam
	2. Execute test_webcam.bat
	   ::python real_time_face_recognition.py --model models/20180408-102900 --classifier models/datasets_classifier.pkl
	   python real_time_face_recognition.py --model models/20180402-114759 --classifier models/datasets_classifier.pkl