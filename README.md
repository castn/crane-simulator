# Crane Simulator 2024

![img.png](resources/images/cover.png)

This program was developed through a project course at the Technical University of Darmstadt.

The task was to develop a tower crane using FEM simulation and to further customize it using parameters.
Our simulation is limited to a highly abstracted version of a tower crane, which is only assembled by simple rods.
Except for the forces weights on the booms, gravity and a horizontal force, which can be considered as a strong
simplification of the wind. No other influences from reality are considered.

## Goals

According to our own requirements, the software should meet the following points

* Create fast and easy new construction cranes
* Simulate your design in different scenarios
* Optimize newly created designs
* Share your design with others

## Quick start

Download the current release for your platform if available. Otherwise, build it your self, follow the instruction
below.

To get started, run your executable. Once done click on **File > Open** and select the file ``exampleCrane.xml``. This
contains an example configuration of the options, which can be set under **Options** can be set.

## Building

Install all requirements for this project listed in the ``requirements.txt`` file. To get a single executable file
[pyinstaller](https://pyinstaller.org/en/stable/) can be used. Otherwise, the program can also be called as usual via a
console or an IDE.

## Licence

This source code is under the [GNU GPLv3](LICENCE.md) license, a free and open-source license.


