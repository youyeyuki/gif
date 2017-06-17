import os

EV_ABS             = 0x0003
EV_SYN             = 0x0000
ABS_MT_POSITION_X  = 0x0035
ABS_MT_POSITION_Y  = 0x0036
ABS_MT_PRESSURE    = 0x003a
ABS_MT_TOUCH_MAJOR = 0x0030
SYN_REPORT         = 0x0000
ABS_MT_TRACKING_ID = 0x0039

touch_event_id = 1

def touch(x, y):

    global touch_event_id

    event_string =  "sendevent /dev/input/event1 %d %d %d\n" % (EV_ABS, ABS_MT_TRACKING_ID, touch_event_id)
    event_string += "sendevent /dev/input/event1 %d %d %d\n" % (EV_ABS, ABS_MT_POSITION_X,  x)
    event_string += "sendevent /dev/input/event1 %d %d %d\n" % (EV_ABS, ABS_MT_POSITION_Y,  y)
    event_string += "sendevent /dev/input/event1 %d %d %d\n" % (EV_ABS, ABS_MT_PRESSURE,    5)
    event_string += "sendevent /dev/input/event1 %d %d %d\n" % (EV_ABS, ABS_MT_TOUCH_MAJOR, 5)
    event_string += "sendevent /dev/input/event1 %d %d %d\n" % (EV_SYN, SYN_REPORT,         0)

    event_string += "sendevent /dev/input/event1 %d %d %d\n" % (EV_ABS, ABS_MT_TRACKING_ID, -1)
    event_string += "sendevent /dev/input/event1 %d %d %d\n" % (EV_SYN, SYN_REPORT,         0)

    touch_event_id+=1
    print('adb shell "%s" &' % event_string)
    os.system('adb shell "%s" &' % event_string)
touch(60,90)