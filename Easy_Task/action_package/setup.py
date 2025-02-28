from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'action_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	(os.path.join('share', package_name, 'action'), glob('action/*.action')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ayisha',
    maintainer_email='ayisharinshapadickal@gmail.com',
    description='To display the Fibonacci Series',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'action_server = action_package.action_server:main',
		'action_client = action_package.action_client:main',
        ],
    },
)
