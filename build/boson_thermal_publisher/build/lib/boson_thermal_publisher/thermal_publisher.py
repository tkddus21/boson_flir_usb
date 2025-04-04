import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class ThermalPublisher(Node):
    def __init__(self):
        super().__init__('thermal_publisher')
        self.publisher_ = self.create_publisher(Image, 'thermal_image', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.cap = cv2.VideoCapture(0)  # /dev/video0 사용
        self.bridge = CvBridge()
        self.get_logger().info("Thermal camera publisher started")

    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            msg = self.bridge.cv2_to_imgmsg(gray, encoding='mono8')
            self.publisher_.publish(msg)
        else:
            self.get_logger().warn('Failed to read frame')


def main(args=None):
    rclpy.init(args=args)
    node = ThermalPublisher()
    rclpy.spin(node)
    node.cap.release()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
