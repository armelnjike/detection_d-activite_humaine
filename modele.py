import os
import cv2
import pafy
import math
import random
import numpy as np
import datetime as dt
import tensorflow as tf
from collections import deque
import matplotlib.pyplot as plt

from moviepy.editor import *

from sklearn.model_selection import train_test_split

from tensorflow import keras
from keras.layers import *
from keras.models import Sequential
#from keras.utils import to_categorical
from keras.callbacks import EarlyStopping
from keras.models import load_model


# Specify the height and width to which each video frame will be resized in our dataset.
IMAGE_HEIGHT , IMAGE_WIDTH = 64, 64

# Specify the directory containing the UCF50 dataset.
DATASET_DIR = "UCF50"

# Specify the list containing the names of the classes used for training. Feel free to choose any set of classes.
CLASSES_LIST = ["WalkingWithDog", "TaiChi", "Swing", "HorseRace"]

SEQUENCE_LENGTH = 20

convlstm_model = load_model('convlstm_model___Date_Time_2022_05_03__12_19_16___Loss_0.4881160855293274___Accuracy_0.7950819730758667.h5')


def predict_on_video(video_file_path, output_file_path, SEQUENCE_LENGTH):
    video_reader = cv2.VideoCapture(video_file_path)

    original_video_width = int(video_reader.get(cv2.CAP_PROP_FRAME_WIDTH))
    original_video_height = int(video_reader.get(cv2.CAP_PROP_FRAME_HEIGHT))

    video_writer = cv2.VideoWriter(output_file_path, cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), video_reader.get(cv2.CAP_PROP_FPS), (original_video_width, original_video_height))

    frames_queue = deque(maxlen=SEQUENCE_LENGTH)

    predicted_class_name = ''

    while video_reader.isOpened():

        # Read the frame.
        ok, frame = video_reader.read()

        # Check if frame is not read properly then break the loop.
        if not ok:
            break

        resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))

        normalized_frame = resized_frame / 255

        frames_queue.append(normalized_frame)

        if len(frames_queue) == SEQUENCE_LENGTH:
            predicted_labels_probabilities = convlstm_model.predict(np.expand_dims(frames_queue, axis=0))[0]

            predicted_label = np.argmax(predicted_labels_probabilities)

            predicted_class_name = CLASSES_LIST[predicted_label]

        if predicted_class_name == "TaiChi":
            cv2.putText(frame, predicted_class_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            video_writer.write(frame)
        else:
            #cv2.putText(frame, predicted_class_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            video_writer.write(frame)

    video_reader.release()
    video_writer.release()


def download_youtube_videos(youtube_video_url, output_directory):
    video = pafy.new(youtube_video_url)

    title = video.title

    video_best = video.getbest()

    output_file_path = f'{output_directory}/{title}.mp4'

    video_best.download(filepath=output_file_path, quiet=True)

    return title


#test_videos_directory = 'test_videos'
#os.makedirs(test_videos_directory, exist_ok=True)

#video_title = download_youtube_videos('https://www.youtube.com/watch?v=8u0qjmHIOcE', test_videos_directory)
#print(f'Video title = {video_title}\n')

#input_video_file_path = "./test_videos/Test Video.mp4"

#output_video_file_path = "./THL 0.mp4"

#predict_on_video(input_video_file_path, output_video_file_path, SEQUENCE_LENGTH)

#VideoFileClip(output_video_file_path, audio=False, target_resolution=(300,None))