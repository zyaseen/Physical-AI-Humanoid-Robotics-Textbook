---
sidebar_position: 3
title: ROS 2 Fundamentals
---

# ROS 2 Fundamentals

Robot Operating System 2 (ROS 2) is a flexible framework for writing robot software. It is a collection of tools, libraries, and conventions that aim to simplify the task of creating complex and robust robot behavior across a wide variety of robot platforms.

## Architecture

ROS 2 uses a DDS (Data Distribution Service) based architecture that enables:

- **Nodes**: Individual processes that perform computation
- **Topics**: Named buses over which nodes exchange messages
- **Services**: Synchronous request/response communication
- **Actions**: Goal-oriented communication patterns with feedback
- **Packages**: Organized collections of related code

## Key Features

- **Communication**: Reliable message passing between nodes
- **Tools**: Visualization, debugging, and analysis tools
- **Ecosystem**: Rich collection of libraries and software packages
- **Distributed**: Multiple nodes can run on different machines
- **Language Support**: C++, Python, and other languages

## Core Concepts

1. **Publisher/Subscriber**: Asynchronous message passing
2. **Client/Server**: Synchronous request/response patterns
3. **Launch Files**: Configuration for starting multiple nodes
4. **Parameters**: Configuration values that can be changed at runtime
5. **TF (Transforms)**: Managing coordinate frame relationships

ROS 2 is essential for modern robotics development and provides the foundation for many robotic applications.