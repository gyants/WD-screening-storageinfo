#!/usr/bin/env python3
import subprocess
import os

def get_lsblk_data():
    try:
        result = subprocess.run(
            ["lsblk", "-b", "-o", "NAME,TYPE,SIZE,MOUNTPOINT"], # only necessary storage data
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True
        )
    except subprocess.CalledProcessError as e:
        print("Error running lsblk:", e.stderr)
        return []
    
    lines = result.stdout.strip().splitlines()
    data = []
    for line in lines[1:]: # omit columns
        column_data = line.split()
        if len(column_data) >= 3:
            name = column_data[0]
            type_ = column_data[1]
            size = column_data[2]
            mountpoint = column_data[3] if len(column_data) > 3 else ""
            data.append({
                "name": name,
                "type": type_,
                "size": int(size),
                "mountpoint": mountpoint
            })
    return data

def get_unused_capacity(mountpoint):
    """Returns available capacity in bytes for a given mountpoint using os.statvfs"""
    try:
        stat = os.statvfs(mountpoint)
        return stat.f_bavail * stat.f_frsize
    except Exception:
        return None

def main():
    devices = get_lsblk_data()
    
    if not devices:
        print("No devices found or error retrieving device data.")
        return
    
    print("Storage Devices Info:")
    for dev in devices:
        # Form device path: typically /dev/NAME
        dev_path = f"/dev/{dev['name']}"
        total_capacity = dev["size"]
        # Check if device is mounted to get available capacity.
        if dev["mountpoint"]:
            available_capacity = get_unused_capacity(dev["mountpoint"])
            if available_capacity is None:
                available_capacity_str = "Could not determine"
            else:
                available_capacity_str = f"{available_capacity} bytes"
        else:
            available_capacity_str = "N/A (Not mounted)"
        
        print(f"Device: {dev_path}")
        print(f"  Total Capacity: {total_capacity} bytes")
        print(f"  Unused Capacity: {available_capacity_str}")
        print("-" * 40)

if __name__ == "__main__":
    main()
