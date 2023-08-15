# Extract images from a ROS2 rosbag

1. Clone the package from the repository:

   ```bash
   git clone https://github.com/khaledgabr77/bag_to_images.git
   ```

2. Build and source the package:

   ```bash
   colcon build 
   source install/setup.bash
   ```

3. Run the script inside the package:

   ```bash
   ros2 run bag_to_images bag_to_image 
   ```

4. Run the rosbag file you want to convert to images:

   ```bash
   ros2 bag play /path/to/your/bagfile.db3
   ```

Replace `/path/to/your/bagfile.db3` with the actual path to your bag file.

These steps will guide you through the process of extracting images from a ROS2 bag file using the `bag_to_images` package.