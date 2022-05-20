# Package-Delivery-App

Package-Delivery App

A package delivery application that receives a list of packages from a CSV file, places them in a user-created hashtable, loads those packages on a truck, and then delivers the packages to their destinations in under 140 total miles.

The application is written in the Python language and is run with JetBrains PyCharm.

To run application:
-Clone repository
-Run the program
-After reading the available options, make a selection and press enter.

Challenges:
-Ensuring that the total mileage for all packages stayed under 140 miles.  An inefficient algorithm would have prevented the total mileage from being met.  A nearest-neighbor algorithm and distance matrix had to be implemented.

Future implementations:
-The trucks were manually loaded. A future update would allow for the program to traverse through the packages to determine which packages need to go on which trucks to ensure they are delivered on time.
-Nearest-Neighbor algorithm in O(n^2).  Future update would find a more efficient algorithm to deliver the packages in under 100 total miles.
