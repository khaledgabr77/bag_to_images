from setuptools import find_packages, setup

package_name = 'bag_to_images'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='khaled gabr',
    maintainer_email='khaledgabr77@gmail.com',
    description='Extract images from a rosbag ROS2',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['bag_to_image = bag_to_images.extract_images:main',
        ],
    },
)
