import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64

class ListenerNode(Node):
    def __init__(self):
        super().__init__("listener_node")
        # Create a subscription to 'sensor_x_readings' topic
        self.subscription_ = self.create_subscription(
            Float64, 
            'sensor_x_readings', 
            self.listener_callback, 
            10
        )

    def listener_callback(self, msg):
        # Log the received message data
        self.get_logger().info(f"Received data: {msg.data}")
        
        # Check if the received value is greater than 0.5
        if msg.data > 0.5:
            self.get_logger().warn('Value is greater than 0.5')

def main(args=None):
    # Initialize the rclpy library
    rclpy.init(args=args)
    
    # Create the listener node
    listener_node = ListenerNode()

    try:
        # Spin the node to keep it running and processing callbacks
        rclpy.spin(listener_node)
    except KeyboardInterrupt:
        # Gracefully handle shutdown
        listener_node.get_logger().info("Node stopped by user")
    finally:
        # Destroy the node and shutdown rclpy
        listener_node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
