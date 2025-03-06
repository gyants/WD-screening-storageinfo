# Storage Info Application

## Overview

This command-line application retrieves and displays detailed information about every storage device on the system. For each device, it prints:
- The device path (e.g., `/dev/sda1`)
- The total capacity (in bytes)
- The unused (available) capacity (in bytes)

I developed this project using Python 3 which is already available on Ubuntu 24.02. The script relies on basic modules like `subprocess` and `os` to retrieve data from the system. I use `lsblk` to list out the available storage devices with only the necessary options like Name, Size, and Mountpoints.

My initial approach was to try out what the output looks like in WSL, and then what it would look like in `stdout` via `subprocess`. I then carefully extract the data and format it in an easy-to-understand way for the users. 

## Dependencies

- Ubuntu 24.04 
- Python 3.x

## Build and Run Instructions

1. **Ensure Python 3 is installed:**  
   If not already installed, you can install it using:
   ```
   sudo apt update
   sudo apt install python3
   ```

2. **Clone the repository and navigate into it:** 
   ```
   git clone https://github.com/gyants/WD-screening-storageinfo (Skip this line if you install this via a zip file) 
   cd WD-screening-storageinfo
   ```

3. **Run the application:**
   ```
   python3 src/storage_info.py
   ```

## Testing

The application was manually tested on Ubuntu 24.04 to verify that it correctly identifies storage devices and prints their capacity information. It uses the `lsblk` command, which is typically available on Ubuntu, to list storage devices. For devices that are mounted, it calculates available capacity using filesystem statistics.