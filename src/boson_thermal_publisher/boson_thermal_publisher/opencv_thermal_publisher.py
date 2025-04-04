import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ThermalViewer(Node):
    def __init__(self):
        super().__init__('thermal_viewer')
        self.subscription = self.create_subscription(Image, 'thermal_image', self.listener_callback, 10)
        self.bridge = CvBridge()

    def listener_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='mono8')  # 또는 'mono16'
        cv2.imshow('Thermal View (from ROS)', frame)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = ThermalViewer()
    rclpy.spin(node)
    cv2.destroyAllWindows()
    node.destroy_node()
    rclpy.shutdown()
