from jetson.inference import detectNet
from jetson.utils import videoSource,videoOutput
# import jetson.inference
# import jetson.utils

net = detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = videoSource("/dev/video0") # '/dev/video0' for V4L2
display = videoOutput("display://0") # 'my_video.mp4' for file
while display.IsStreaming():
  img=camera.Capture()
  
  if img is None:
    continue
  detections=net.Detect(img)
  print(detections[0])
  display.Render(img)
  display.SetStatus("Object Detection|Network{:.0}FPS".format(net.GetNetworkFPS()))



