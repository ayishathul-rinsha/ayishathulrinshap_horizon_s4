from setuptools import find_packages, setup

package_name = 'add_two_ints'

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
    maintainer='ayisha',
    maintainer_email='ayisharinshapadickal@gmail.com',
    description='Service tpo add two numbers',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'server = add_two_ints.service_server:main',
		'client = add_two_ints.sevice_client:main',
        ],
    },
)
