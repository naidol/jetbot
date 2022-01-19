import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # rviz_config_path = PathJoinSubstitution(
    #     [FindPackageShare('linorobot2_viz'), 'rviz', 'linorobot2_slam.rviz']
    # )
    rviz_config_path = os.path.join(get_package_share_directory('nav2_bringup'),'rviz','nav2_default_view.rviz')

    return LaunchDescription([
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path],
        )
    ])