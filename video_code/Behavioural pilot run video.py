# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 12:06:17 2023

@author: g71044mh
"""
#%%
'''provides list of videos and instructions for cameras'''
import cv2
import numpy as np
import time
import serial

def play_video(video_path,ser):
    
    # quit
    quit_playing = False
    
    # Create a VideoCapture object and read from input file
    cap = cv2.VideoCapture(video_path)

    # Check if camera opened successfully
    if not cap.isOpened():
        print("Error opening video file")
        return

    # Create window named 'Frame'
    cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)

    # Move the window to the second monitor (you'll need to adjust these)
    x, y = 0, 0  # These values depend on your screen's resolution
    cv2.moveWindow('Frame', x, y)

    # Set the window to full screen
    cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Read until video is completed
    while(cap.isOpened()):

        # Capture frame-by-frame
        ret, frame = cap.read()

        if ret:
            # trigger cameras
            if ser != 0:
                ser.write(b'4')
            
            # Display the resulting frame
            cv2.imshow('Frame', frame)
            
            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                quit_playing = True
                break
        else:
            break

    # When everything is done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()
    
    # return the quit value
    return quit_playing

#copy the list of videos here
list_of_videos = [
    r'\\nask.man.ac.uk\home$\Desktop\Behavioural Pilot Stimuli Videos\looming_disc.mp4',
    r'\\nask.man.ac.uk\home$\Desktop\Behavioural Pilot Stimuli Videos\looming_ellipse.mp4',
    r'\\nask.man.ac.uk\home$\Desktop\Behavioural Pilot Stimuli Videos\sweeping_disc_LR.mp4',
    r'\\nask.man.ac.uk\home$\Desktop\Behavioural Pilot Stimuli Videos\sweeping_disc_RL.mp4',
    r'\\nask.man.ac.uk\home$\Desktop\Behavioural Pilot Stimuli Videos\sweeping_ellipse_LR.mp4',
    r'\\nask.man.ac.uk\home$\Desktop\Behavioural Pilot Stimuli Videos\sweeping_ellipse_RL.mp4',
    r'\\nask.man.ac.uk\home$\Desktop\Behavioural Pilot Stimuli Videos\background_only.mp4',
]

def play_all_videos(video_list, wait_time, ser): 
    quit_playing = False
    for i, video_path in enumerate(video_list):
        print(f"Playing video {i+1}: {video_path}")
        quit_playing = play_video(video_path, ser)
        if i != len(video_list) - 1:
            print(f"Waiting for {wait_time} seconds before the next video...")
        if quit_playing == True:
            break
        time.sleep(wait_time)
    return quit_playing
    


#%%
'''runs stimulus set 1 or 2'''
import cv2
import numpy as np
import time
import serial

# init seed & wait time, define all experiment parameters
np.random.seed(1)
wait_time = 60  #set pause time between videos (set to 60)
which_stimuli = 1 # select stimulus set, 1 or 2
use_serial = True

# init serial
if use_serial:
    ser = serial.Serial('COM3',9600,timeout=1)
else: 
    ser = 0

# generates stimulus sets
if which_stimuli == 1:
    ind1 = [0, 4, 6]
    ind2 = [0, 5, 6]
elif which_stimuli == 2:
    ind1 = [1, 2, 6]
    ind2 = [1, 3, 6]
else:
    print("ERROR: Select which_stimuli set to use (1/2)") 
    ser.close()


# first block
ind_list = np.random.permutation(ind1)
ind_list = np.append(ind_list, np.random.permutation(ind2))

# give the number of blocks (- 1)
for n in range(4):
    ind_list = np.append(ind_list, np.random.permutation(ind1))
    ind_list = np.append(ind_list, np.random.permutation(ind2))

# print list of videos
print(ind_list)


# to play the videos
Nlist = len(ind_list)
for n in range(Nlist):
    quit_playing = play_all_videos([list_of_videos[ind_list[n]]], wait_time, ser)
    if quit_playing == True:
        break

ser.close()