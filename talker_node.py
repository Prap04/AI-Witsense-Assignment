import rclpy
from rclpy.node import Node
import random
from std_msgs.msg import Float64

class TalkerNode(Node):
    def __init__(self):
        super().__init__("talker_node")
        self.publisher_ = self.create_publisher(Float64, 'sensor_x_readings', 10)
        timer_period = 0.5  # Timer period in seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        random_number = random.random()  # Generate a random number between 0 and 1
        msg = Float64()  # Create a Float64 message
        msg.data = random_number  # Assign the random number to the data field
        self.publisher_.publish(msg)  # Publish the random number
        self.get_logger().info(f"Publishing random number: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    talker_node = TalkerNode()

    try:
        rclpy.spin(talker_node)
    except KeyboardInterrupt:
        talker_node.get_logger().info("Node stopped by user")
    finally:
        talker_node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
