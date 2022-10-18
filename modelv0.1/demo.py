import cv2
import detect

k = cv2.waitKey(1) & 0xFF

while k != ord('q'):

    detect.run(source='0') # rtmp://0.0.0.0:1935/live