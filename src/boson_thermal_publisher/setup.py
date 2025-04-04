from setuptools import find_packages, setup

package_name = 'boson_thermal_publisher'

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
    maintainer='krristudent',
    maintainer_email='krristudent@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
             'thermal_publisher = boson_thermal_publisher.thermal_publisher:main',
             'boson_flir_publisher = boson_thermal_publisher.boson_flir_publisher:main',
             'opencv_thermal_publisher_publisher = boson_thermal_publisher.opencv_thermal_publisher_publisher:main'
        ],
    },
)
