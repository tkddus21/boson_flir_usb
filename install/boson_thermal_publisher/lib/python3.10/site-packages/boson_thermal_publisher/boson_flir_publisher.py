import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class ThermalPublisher(Node):
    def __init__(self):
        super().__init__('boson_flir_publisher')
        self.publisher_ = self.create_publisher(Image, 'thermal_image', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
          # /dev/video0 사용
        self.cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L2)
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'Y16 '))
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.bridge = CvBridge()
        self.get_logger().info("Thermal camera publisher started")



    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            # frame: 640x512, 16-bit 데이터
            # normalize -> 8비트로 다운스케일
            normalized = cv2.normalize(frame, None, 0, 255, cv2.NORM_MINMAX)
            gray_8bit = np.uint8(normalized)

            msg = self.bridge.cv2_to_imgmsg(frame, encoding='mono16')
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
