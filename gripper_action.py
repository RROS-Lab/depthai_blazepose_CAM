import gripper_fcn as gf

if True:
    grip=gf.RobotiqGripper("/dev/ttyUSB1")

    #grip.resetActivate()
    # grip.reset()
    # grip.printInfo()
    # grip.activate()
    # grip.printInfo()
    
    grip.goTo(200)
    # grip.goTo(0)
    # grip.reset()
    # grip.goTo(20)
    
    # grip.calibrate(0,40)
    # grip.goTomm(20,255,255)
    # grip.goTomm(40,1,255)