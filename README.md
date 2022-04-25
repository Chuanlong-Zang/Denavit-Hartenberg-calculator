# Denavit–Hartenberg-calculator
 Script for calculating the DH-parameters (transformations) on a 4-link robot arm

## Description

This script is based on [Denavit–Hartenberg parameters](https://en.wikipedia.org/wiki/Denavit%E2%80%93Hartenberg_parameters). And for two adjacent links i and (i-1) on the robot arm, we have the coordinate transformation:

![transform](./img/transform.jpg)

where the individual parameters are defined as

![links](./img/links.PNG)
Note this image (and the image below) are taken from the book: Introduction to Robotics. Mechanics and Control. Third Edition. John J. Craig. PEARSON.

Therefore, if we need to get the transformation between last link (e.g. the gripper) and the first link, we need to concatenate the individual matrices:

![concat](./img/concat.PNG)

However, the product cannot be computed by hand efficiently. With this small script, one is able to quickly get the result.

## Usage

1. Adjust the parameters in the beginning of the script.
2. Adjust what you need as the result.
3. Run and get the result!