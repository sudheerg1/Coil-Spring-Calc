# Spring Calculator Application

This is a specialized engineering tool designed to help users find optimal spring configurations based on their specific requirements. The application is built with Python using the Tkinter library for its graphical interface.

## Purpose and Functionality

The Spring Calculator helps engineers and designers find viable spring configurations by calculating multiple possible designs that meet their specified criteria. Rather than manually calculating each possible configuration (which would be time-consuming and error-prone), this tool automates the process by:

1. Taking your basic requirements as input
2. Applying engineering formulas for spring calculations
3. Testing numerous parameter combinations
4. Filtering results to show only designs that meet all your constraints

## Main Components

The interface is organized into four main sections:

### 1. Inputs (Mandatory)
- **Material selection**: Choose between Spring Steel or Stainless Steel 304 (which affects material properties)
- **Initial Length (Li)**: The spring's starting length in millimeters
- **Final Length (Lf)**: The spring's extended length in millimeters

### 2. Constraints
Set minimum and maximum values for:
- **Factor of Safety (FOS)**: The ratio between the material's allowable stress and actual stress
- **Initial Force (Fi)**: The force exerted by the spring at initial length (in kgf)
- **Final Force (Ff)**: The force exerted by the spring at final length (in kgf)

### 3. Filters (Optional)
Further refine results by specifying ranges for:
- **Wire Diameter (d)**: The thickness of the wire used to make the spring
- **Coil Outer Diameter (OD)**: The external diameter of the spring coils

### 4. Results
After clicking "Calculate," the app runs through thousands of possible combinations of:
- Wire diameters
- Coil diameters
- Pitch values (distance between coils)
- Initial extensions

For each combination, it applies mechanical engineering formulas to calculate forces, stresses, and safety factors. It then displays up to 50 valid spring designs that meet all your specified criteria, showing details like:
- Dimensions (wire diameter, outer diameter, pitch)
- Forces (initial and final)
- Factor of safety
- Various length measurements

## Practical Use

This calculator would be valuable for mechanical engineers, product designers, or manufacturing professionals who need to design or select springs for specific applications where the spring needs to provide particular forces when compressed or extended to certain lengths.

This is an MVP (Minimum Viable Product), and it may be expanded with more features in future iterations.
