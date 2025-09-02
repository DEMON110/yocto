# IoT Device Binary Hardening with Yocto and Clang

## Overview
This project demonstrates how to implement binary hardening techniques for IoT devices using the Clang compiler in the Yocto build environment. By utilizing Clang's security flags, we can enhance the security of IoT devices while minimizing the performance trade-offs.

## Contents
- **fortifybuild.py**: A Python script for automating the application of Clang security flags in a Yocto build environment.
- **pins.json**: Configuration file containing Clang security flags and build setup.
- **metrics_collection.py**: A Python script to gather and store performance metrics like boot time, binary size, latency, and throughput.
- **Clangify.py**: Tool to manage Clang security flags for Yocto packages.
- **matplotlib_graphs.py**: Python script to visualize the performance metrics with Matplotlib.
- **metrics.csv**: CSV file containing the performance results of different builds (Stock GCC, Stock Clang, All Clang).
- **performance_metrics.png**: Graph generated from the metrics CSV file, comparing the performance of different builds.

## Installation
1. **Clone this repository**:

2. **Dependencies**:
- Python 3.x
- Matplotlib (for visualizing graphs)
- Yocto build environment

3. **Run the scripts**:
- Initialize Clang and set security flags:
  ```
  python3 fortifybuild.py
  ```
- Collect performance metrics:
  ```
  python3 metrics_collection.py
  ```
- Generate performance graphs:
  ```
  python3 matplotlib_graphs.py
  ```

## Recommendations
- **Security Flags**:
- `-D_FORTIFY_SOURCE=2`: Buffer overflow protection.
- `-fstack-protector-strong`: Stack protection.
- `-fPIE`: Position-independent executable for ASLR.
- `-Wl,-z,relro,-z,now`: Relocation and immediate binding for secure function calls.

## References
- [Clang Compiler User’s Manual](https://clang.llvm.org/docs/UsersManual.html)
- [LLVM Project](https://llvm.org)
