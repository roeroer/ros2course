import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/paulwetzel/repo/rise-repos/exo2-new/course/ros2course/ch2-3-make-the-nodes-talk/install/listener_node'
