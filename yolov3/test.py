#from moviepy.editor import VideoFileClip
#import cv2

#def process_image(image):
#    cv2.rectangle(image, (0,0), (600,600), (0,0,255), thickness=5)
#    return image

#white_output = 'video_out.mp4'
#clip = VideoFileClip('video.mp4').subclip(10,25)
#white_clip  = clip.fl_image(process_image)
#white_clip.write_videofile(white_output, audio=False)

import argparse

argparser = argparse.ArgumentParser(
    description='test yolov3 network with coco weights')

argparser.add_argument(
    '-w',
    '--weights',
    help='path to weights file')

argparser.add_argument(
    '-i',
    '--image',
    help='path to image file')

args = argparser.parse_args()

print(args.weights)