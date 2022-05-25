
```
usc_cam@awesomeone:~/Documents/Yufei_workspace/depthai_blazepose$ python3 demo.py -xyz -c
Pose detection blob file : /home/usc_cam/Documents/Yufei_workspace/depthai_blazepose/models/pose_detection_sh4.blob
Landmarks using blob file : /home/usc_cam/Documents/Yufei_workspace/depthai_blazepose/models/pose_landmark_full_sh4.blob
Internal camera FPS set to: 13
Sensor resolution: (1920, 1080)
Internal camera image size: 640 x 640 - crop_w:249 pad_h: 0
2254 anchors have been created
Creating pipeline...
Creating Color Camera...
Creating Pose Detection pre processing image manip...
RGB calibration lens position: 135
Creating Pose Detection Neural Network...
Creating Landmark Neural Network...
Pipeline created.
[14442C10B19060D700] [49.877] [NeuralNetwork(10)] [warning] Network compiled for 4 shaves, maximum available 12, compiling for 6 shaves likely will yield in better performance
[14442C10B19060D700] [49.878] [NeuralNetwork(12)] [warning] Number of inference threads assigned for network is 1, assigning 2 will likely yield in better performance
[14442C10B19060D700] [49.878] [NeuralNetwork(12)] [warning] Network compiled for 4 shaves, maximum available 12, compiling for 6 shaves likely will yield in better performance
Pipeline started - USB speed: HIGH
[14442C10B19060D700] [49.894] [NeuralNetwork(10)] [warning] The issued warnings are orientative, based on optimal settings for a single network, if multiple networks are running in parallel the optimal settings may vary
[14442C10B19060D700] [49.894] [NeuralNetwork(12)] [warning] The issued warnings are orientative, based on optimal settings for a single network, if multiple networks are running in parallel the optimal settings may vary
[14442C10B19060D700] [50.121] [system] [critical] Fatal error. Please report to developers. Log: 'PlgWarpHW' '411'
Traceback (most recent call last):
  File "demo.py", line 65, in <module>
    frame, body = tracker.next_frame()
  File "/home/usc_cam/Documents/Yufei_workspace/depthai_blazepose/BlazeposeDepthai.py", line 636, in next_frame
    self.query_body_xyz(body)
  File "/home/usc_cam/Documents/Yufei_workspace/depthai_blazepose/BlazeposeDepthai.py", line 436, in query_body_xyz
    spatial_data = self.q_spatial_data.get().getSpatialLocations()
AttributeError: 'depthai.ADatatype' object has no attribute 'getSpatialLocations'
Stack trace (most recent call last):
#18   Object "[0xffffffffffffffff]", at 0xffffffffffffffff, in 
#17   Object "python3", at 0x5fa5cd, in _start
#16   Object "/lib/x86_64-linux-gnu/libc.so.6", at 0x7fdbffa870b2, in __libc_start_main
#15   Object "python3", at 0x6b736c, in Py_BytesMain
#14   Object "python3", at 0x6b70fc, in Py_RunMain
#13   Object "python3", at 0x67f8ae, in Py_FinalizeEx
#12   Object "python3", at 0x684732, in PyImport_Cleanup
#11   Object "python3", at 0x5d2256, in 
#10   Object "python3", at 0x6a631b, in 
#9    Object "python3", at 0x5d270b, in 
#8    Object "python3", at 0x5ccad2, in 
#7    Object "python3", at 0x5a729c, in 
#6    Object "python3", at 0x5d28a7, in 
#5    Object "python3", at 0x5a729c, in 
#4    Object "python3", at 0x5d28f3, in 
#3    Object "/home/usc_cam/.local/lib/python3.8/site-packages/depthai.cpython-38-x86_64-linux-gnu.so", at 0x7fdbe91e5d9b, in 
#2    Object "/home/usc_cam/.local/lib/python3.8/site-packages/depthai.cpython-38-x86_64-linux-gnu.so", at 0x7fdbe928b759, in 
#1    Object "/home/usc_cam/.local/lib/python3.8/site-packages/depthai.cpython-38-x86_64-linux-gnu.so", at 0x7fdbe93ea71e, in dai::DataOutputQueue::~DataOutputQueue()
#0    Object "/home/usc_cam/.local/lib/python3.8/site-packages/depthai.cpython-38-x86_64-linux-gnu.so", at 0x7fdbe93e7ff6, in 
Segmentation fault (Address not mapped to object [0x120000000098])
Segmentation fault (core dumped)
```