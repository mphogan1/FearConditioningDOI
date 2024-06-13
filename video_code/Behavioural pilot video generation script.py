# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:22:48 2023

@author: g71044mh 
"""
#%%
'''Looming disc'''
import cv2
import numpy as np

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
INITIAL_RADIUS = 270  # half size of the height is 270
FRAMES_PER_SECOND = 30
DURATION = 3  # 3 seconds for circle growing
EMPTY_DURATION_BEFORE = 5  # 5 seconds for empty video before
EMPTY_DURATION_AFTER = 5   # 5 seconds for empty video after

# Initialize OpenCV video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(r'\\nask.man.ac.uk\home$\Desktop\Behavioural Pilot Stimuli Videos\looming_disc.mp4', fourcc, FRAMES_PER_SECOND, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Calculate total frames and step size for radius
total_frames = FRAMES_PER_SECOND * (DURATION + EMPTY_DURATION_BEFORE + EMPTY_DURATION_AFTER)
radius_step = 10  # Increase this for faster growth

# Function to generate a white frame
def create_white_frame():
    return np.full((SCREEN_HEIGHT, SCREEN_WIDTH, 3), (255, 255, 255), dtype=np.uint8)

# Add empty video before looming disc
for _ in range(FRAMES_PER_SECOND * EMPTY_DURATION_BEFORE):
    video.write(create_white_frame())

# Initial radius
radius = INITIAL_RADIUS

# Create video for looming disc
for _ in range(FRAMES_PER_SECOND * DURATION):
    frame = create_white_frame()
    x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    cv2.circle(frame, (x, y), radius, (0, 0, 0), -1)  # Black circle
    video.write(frame)
    radius += radius_step

# Add empty video after looming disc
for _ in range(FRAMES_PER_SECOND * EMPTY_DURATION_AFTER):
    video.write(create_white_frame())

# Release video writer
video.release()

# Calculate speed
speed = radius_step * FRAMES_PER_SECOND / SCREEN_WIDTH * 57  # Assuming screen width represents 57 cm

print("Video created successfully!")
print("The speed of the looming disc is:", speed, 'cm/s')
#%%
'''Looming Ellipse'''
import cv2
import numpy as np

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
FRAMES_PER_SECOND = 30
DURATION = 3  # 3 seconds for looming ellipse 
EMPTY_DURATION_BEFORE = 5  # 5 seconds for empty video before
EMPTY_DURATION_AFTER = 5   # 5 seconds for empty video after

# Initial size of the ellipse
initial_width = 72
initial_height = 27

# Initialize OpenCV video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(r'\\nask.man.ac.uk\home$\Desktop\Behavioural Pilot Stimuli Videos\looming_ellipse.mp4', fourcc, FRAMES_PER_SECOND, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Calculate total frames and step size for the ellipse
total_frames = FRAMES_PER_SECOND * (DURATION + EMPTY_DURATION_BEFORE + EMPTY_DURATION_AFTER)
width_step = SCREEN_WIDTH / (FRAMES_PER_SECOND * DURATION)
height_step = SCREEN_WIDTH / (FRAMES_PER_SECOND * DURATION)*3/8

# Function to generate a white frame
def create_white_frame():
    return np.full((SCREEN_HEIGHT, SCREEN_WIDTH, 3), (255, 255, 255), dtype=np.uint8)

# Add empty video before looming ellipse 
for _ in range(FRAMES_PER_SECOND * EMPTY_DURATION_BEFORE):
    video.write(create_white_frame())

# Initial size of the ellipse
width = initial_width
height = initial_height

# Create video for looming ellipse 
for _ in range(FRAMES_PER_SECOND * DURATION):
    frame = create_white_frame()
    center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # Round the axes values to the nearest integer
    axes = (int(width // 2), int(height // 2))

    cv2.ellipse(frame, center, axes, 0, 0, 360, (0, 0, 0), -1)  # Black ellipse
    video.write(frame)
    width += width_step
    height += height_step

# Add empty video after looming ellipse 
for _ in range(FRAMES_PER_SECOND * EMPTY_DURATION_AFTER):
    video.write(create_white_frame())

# Release video writer
video.release()


speed_in_cm=57/DURATION
print("Video created successfully!")
print("The speed of the looming ellipse is:", speed_in_cm, 'cm/s')
#%%
'''Sweeping Disc Left to Right'''
import cv2
import numpy as np

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
CIRCLE_RADIUS = 100 # 6.15deg
FRAMES_PER_SECOND = 30
DURATION = 3  # 5 seconds for circle sweeping
EMPTY_DURATION_BEFORE = 5  # 5 seconds for empty video before
EMPTY_DURATION_AFTER = 5  # 5 seconds for empty video after

# Initialize OpenCV video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(r'\\nask.man.ac.uk\home$\Desktop\Behavioural Pilot Stimuli Videos\sweeping_disc_LR.mp4', fourcc, FRAMES_PER_SECOND, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Calculate total frames and step size
total_frames = FRAMES_PER_SECOND * DURATION
step = (SCREEN_WIDTH + 2 * CIRCLE_RADIUS) / total_frames

# Create a function to generate a background frame
def create_background_frame():
    return np.full((SCREEN_HEIGHT, SCREEN_WIDTH, 3), (255, 255, 255), dtype=np.uint8)

# Add 5 seconds of empty video (background) before sweeping disc
for _ in range(FRAMES_PER_SECOND * EMPTY_DURATION_BEFORE):
    video.write(create_background_frame())

# Initial position
x = 0  # Start from the left
y = SCREEN_HEIGHT // 2  # Center vertically

# Create video for sweeping disc
for _ in range(total_frames):
    # Create a background
    frame = create_background_frame()

    # Update position
    x += step

    # Draw circle
    cv2.circle(frame, (int(x), int(y)), CIRCLE_RADIUS, (0, 0, 0), -1)  # Black circle

    # Write frame to video
    video.write(frame)

# Add 7 seconds of empty video (background) after sweeping disc
for _ in range(FRAMES_PER_SECOND * EMPTY_DURATION_AFTER):
    video.write(create_background_frame())

# Release video writer
video.release()

speed = 57 / DURATION

print("Video created successfully!")
print("The speed of the sweeping circle is:")
print(speed, 'cm/s')
#%%
'''Sweeping Disc Right to Left'''
import cv2
import numpy as np

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
CIRCLE_RADIUS = 100 # 6.15deg
FRAMES_PER_SECOND = 30
DURATION = 3  # 5 seconds for circle sweeping
EMPTY_DURATION_BEFORE = 5  # 5 seconds for empty video before
EMPTY_DURATION_AFTER = 5  # 5 seconds for empty video after

# Initialize OpenCV video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(r'\\nask.man.ac.uk\home$\Desktop\Behavioural Pilot Stimuli Videos\sweeping_disc_RL.mp4', fourcc, FRAMES_PER_SECOND, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Calculate total frames and step size
total_frames = FRAMES_PER_SECOND * DURATION
step = (SCREEN_WIDTH + 2 * CIRCLE_RADIUS) / total_frames

# Create a function to generate a background frame
def create_background_frame():
    return np.full((SCREEN_HEIGHT, SCREEN_WIDTH, 3), (255, 255, 255), dtype=np.uint8)

# Add 5 seconds of empty video (background) before sweeping disc
for _ in range(FRAMES_PER_SECOND * EMPTY_DURATION_BEFORE):
    video.write(create_background_frame())

# Initial position
x = SCREEN_WIDTH+CIRCLE_RADIUS # Start from the right
y = SCREEN_HEIGHT // 2  # Center vertically

# Create video for sweeping disc
for _ in range(total_frames):
    # Create a background
    frame = create_background_frame()

    # Update position
    x -= step

    # Draw disc
    cv2.circle(frame, (int(x), int(y)), CIRCLE_RADIUS, (0, 0, 0), -1)  # Black circle

    # Write frame to video
    video.write(frame)

# Add 5 seconds of empty video (background) after sweeping disc
for _ in range(FRAMES_PER_SECOND * EMPTY_DURATION_AFTER):
    video.write(create_background_frame())

# Release video writer
video.release()

speed = 57 / DURATION

print("Video created successfully!")
print("The speed of the sweeping circle is:")
print(speed, 'cm/s')
#%%
'''Sweeping Ellipse Right to Left'''
import cv2
import numpy as np

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
width = 40  # Width of the ellipse 4.4 deg
height = 111  # Height of the ellipse, 6.6 deg
# Define the angle of rotation (in degrees)
angle = 0  # Rotate the ellipse by 45 degrees (you can change this angle)
FRAMES_PER_SECOND = 30
DURATION = 3  
EMPTY_DURATION_BEFORE = 5  # 5 seconds for empty video before
EMPTY_DURATION_AFTER = 5  # 5 seconds for empty video after

# Initialize OpenCV video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(r'\\nask.man.ac.uk\home$\Desktop\Behavioural Pilot Stimuli Videos\sweeping_ellipse_RL.mp4', fourcc, FRAMES_PER_SECOND, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Function to create a background frame
def create_background_frame():
    return np.full((SCREEN_HEIGHT, SCREEN_WIDTH, 3), (255, 255, 255), dtype=np.uint8)

# Add 5 seconds of empty video (background) before sweeping ellipse
for _ in range(FRAMES_PER_SECOND * EMPTY_DURATION_BEFORE):
    video.write(create_background_frame())

# Calculate total frames and step size
total_frames = FRAMES_PER_SECOND * DURATION
step = (SCREEN_WIDTH + 2 * width) / total_frames

# Initial position
x = SCREEN_WIDTH + width  # Start from the right
y = SCREEN_HEIGHT // 2  # Center vertically

# Create video
for _ in range(total_frames):
    # Create a white background
    frame = np.full((SCREEN_HEIGHT, SCREEN_WIDTH, 3), (255, 255, 255), dtype=np.uint8)

    # Update position
    x -= step

    # Draw ellipse
    cv2.ellipse(frame, (int(x), int(y)), (width, height), angle, 0, 360, (0, 0, 0), -1)  # Red ellipse

    # Write frame to video
    video.write(frame)
    
    
# Add 5 seconds of empty video (background) after sweeping ellipse
for _ in range(FRAMES_PER_SECOND * EMPTY_DURATION_AFTER):
    video.write(create_background_frame())


# Release video writer
video.release()

speed=57/DURATION

print("Video created successfully!")
print("The speed of the sweeping ellipse is:")
print(speed,'cm/s')
#%%
'''Sweeping Ellipse Left to Right'''
import cv2
import numpy as np

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
width = 40  # Width of the ellipse, 2.4 deg
height = 111  # Height of the ellipse, 6.6 deg
# Define the angle of rotation (in degrees)
angle = 0  # Rotate the ellipse by 45 degrees (you can change this angle)
FRAMES_PER_SECOND = 30
DURATION = 3  # 15 seconds
EMPTY_DURATION_BEFORE = 5  # 5 seconds for empty video before
EMPTY_DURATION_AFTER = 5  # 5 seconds for empty video after

# Initialize OpenCV video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(r'\\nask.man.ac.uk\home$\Desktop\Behavioural Pilot Stimuli Videos\sweeping_ellipse_LR.mp4', fourcc, FRAMES_PER_SECOND, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Function to create a background frame
def create_background_frame():
    return np.full((SCREEN_HEIGHT, SCREEN_WIDTH, 3), (255, 255, 255), dtype=np.uint8)

# Add 5 seconds of empty video (background) before sweeping ellipse
for _ in range(FRAMES_PER_SECOND * EMPTY_DURATION_BEFORE):
    video.write(create_background_frame())

# Calculate total frames and step size
total_frames = FRAMES_PER_SECOND * DURATION
step = (SCREEN_WIDTH + 2 * width) / total_frames

# Initial position
x = 0  # Start from the left
y = SCREEN_HEIGHT // 2  # Center vertically

# Create video
for _ in range(total_frames):
    # Create a white background
    frame = np.full((SCREEN_HEIGHT, SCREEN_WIDTH, 3), (255, 255, 255), dtype=np.uint8)

    # Update position
    x += step

    # Draw ellipse
    cv2.ellipse(frame, (int(x), int(y)), (width, height), angle, 0, 360, (0, 0, 0), -1)  # Red ellipse

    # Write frame to video
    video.write(frame)

# Add 5 seconds of empty video (background) after sweeping ellipse
for _ in range(FRAMES_PER_SECOND * EMPTY_DURATION_AFTER):
    video.write(create_background_frame())

# Release video writer
video.release()

speed = 57 / DURATION

print("Video created successfully!")
print("The speed of the sweeping ellipse is:")
print(speed, 'cm/s')
#%%
'''background only'''
import cv2
import numpy as np

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
FRAMES_PER_SECOND = 30
DURATION = 13  # 13 seconds

# Initialize OpenCV video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(r'\\nask.man.ac.uk\home$\Desktop\Behavioural Pilot Stimuli Videos\background_only.mp4', fourcc, FRAMES_PER_SECOND, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Function to create a background frame
def create_background_frame():
    return np.full((SCREEN_HEIGHT, SCREEN_WIDTH, 3), (255, 255, 255), dtype=np.uint8)

# Calculate total frames
total_frames = FRAMES_PER_SECOND * DURATION

# Create video with background only
for _ in range(total_frames):
    # Create a white background frame
    frame = create_background_frame()

    # Write frame to video
    video.write(frame)

# Release video writer
video.release()

print("Background only video created successfully!")

#%%
#Support Code
cv2.circle(frame, (int(x), int(y)), CIRCLE_RADIUS, (0, 0, 0), -1)  # Black circle
cv2.circle(frame, (x, y), radius, (0, 0, 255), -1)  # Red circle
frame = np.full((SCREEN_HEIGHT, SCREEN_WIDTH, 3), (128, 128, 128), dtype=np.uint8)  # Gray background
#%%
'''converts speed in cm/s to subjective angular speed of object for the arena'''
import math

def linear_to_angular_speed(speed, distance_cm):
    # Convert linear speed to angular speed in radians per second
    angular_speed_rad_per_s = speed / distance_cm
    
    # Convert angular speed to degrees per second
    angular_speed_deg_per_s = angular_speed_rad_per_s * (180 / math.pi)
    
    return angular_speed_deg_per_s

distance = 51      # distance from arena floor to screen

angular_speed_deg = linear_to_angular_speed(speed, distance)
print("Angular Speed:", angular_speed_deg, "degrees/s")
#%%
'''converts from diameter in cm to angular diameter'''
import math

def cm_to_angular_diameter(object_diameter_cm, distance_cm):
    # Convert object diameter from centimeters to angular diameter
    angular_diameter_rad = 2 * math.atan(object_diameter_cm / (2 * distance_cm))
    
    # Convert angular diameter from radians to degrees
    angular_diameter_deg = math.degrees(angular_diameter_rad)
    
    return angular_diameter_deg

# Example usage
object_diameter_cm = 2.13  # Replace with the actual object diameter in centimeters
distance_cm = 51  # Replace with the actual distance in centimeters

angular_diameter_deg = cm_to_angular_diameter(object_diameter_cm, distance_cm)

print(f"The angular diameter of the object is {angular_diameter_deg:.2f} degrees.")
#%%
'''converts from angular diameter to diameter in cm'''
import math

def angular_diameter_to_cm(angular_diameter_deg, distance_cm):
    # Convert angular diameter from degrees to radians
    angular_diameter_rad = math.radians(angular_diameter_deg)
    
    # Calculate object diameter in centimeters
    object_diameter_cm = 2 * distance_cm * math.tan(angular_diameter_rad / 2)
    
    return object_diameter_cm

# Example usage
angular_diameter_deg = 6.15  # Replace with the actual angular diameter in degrees
distance_cm = 51  # Replace with the actual distance in centimeters

object_diameter_cm = angular_diameter_to_cm(angular_diameter_deg, distance_cm)

print(f"The diameter of the object is {object_diameter_cm:.2f} centimeters.")

