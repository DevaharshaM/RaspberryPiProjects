This Python script demonstrates the basics of capturing and displaying RealSense camera streams on a Raspberry Pi using OpenCV.

## Hardware Requirements

- **Raspberry Pi 4 Model B**
- **Intel RealSense D435**

## Installation

### Prerequisites

   Follow the installation instructions provided in the [Intel RealSense SDK](https://github.com/DevaharshaM/RaspberryPiProjects/wiki/Interfacing-Intel-RealSense-D435-with-Raspberry-Pi-4) to set up the SDK on your Raspberry Pi.

### Required Packages

1. **Set Up Python Virtual Environment**

   It is recommended to use a Python virtual environment to avoid package conflicts and ensure isolation.

   ```sh
   python3 -m venv ~/myenv
  
   # Activate the virtual environment
   source ~/myenv/bin/activate
   ```

2. **Install Required Packages**

   Once the virtual environment is activated, install the necessary Python packages:

   ```sh
   pip install numpy
   pip install opencv-python
   ```

## Debugging

1. **No Module named 'pyrealsense2'**

   Deactivate the virtual environment, if activated.

    ```sh
    deactivate
    ```
   
   Locate '.so' file:

     ```sh
     find ~/librealsense/build -name "pyrealsense2*.so"
     ```

   Copy the file to the 'pyrealsense2' directory within the Python wrapper:

    ```sh
    cp ~/librealsense/build/wrappers/python/pyrealsense2*.so ~/librealsense/wrappers/python/pyrealsense2/
    ```

   Ensure that the 'pyrealsense2' directory and the '.so' file have the correct permissions:

    ```sh
    chmod +r /home/dissertation/librealsense/wrappers/python/pyrealsense2/pyrealsense2.cpython-311-aarch64-linux-gnu.so
    ```

   Open '.bashrc' file and add the path at bottom.

   ```sh
    echo 'export PYTHONPATH=/home/dissertation/librealsense/wrappers/python/pyrealsense2' >> ~/.bashrc
    source ~/.bashrc
   ```

   Activate and try importing 'pyrealsense2' in python.

2. **OpenCV conflict with Numpy version**

   Delete the Numpy and OpenCV modules:

    ```sh
    pip uninstall numpy
    pip uninstall opencv-python
    ```

   Ensure that the versions are compatibile:

   ```sh
    pip install numpy==1.24.1
    pip install opencv-python==4.10.0.82
   ```
