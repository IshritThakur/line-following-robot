from setuptools import setup

package_name = 'line_follower'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ishrit Thakur',
    maintainer_email='ishritthakur@gmail.com',
    description='A ROS2 Python package for a simple line following robot.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'linefollower = line_follower.linefollower:main'
        ],
    },
)