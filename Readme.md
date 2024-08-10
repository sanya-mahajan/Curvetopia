# **Polygon Simplification and Regularization**

This project focuses on the simplification and regularization of hand-drawn shapes, particularly polygons, by processing the input paths and reducing complex paths into simpler geometric forms. The goal is to retain the original shape's orientation and approximate vertex positions while transforming it into a more regular form.

## **Features**

- **Path Extraction**: Extracts paths from CSV files where each path is represented as a series of (x, y) coordinates.
- **Line Simplification**: Simplifies hand-drawn lines into straight segments while preserving the original form when the total deviation is minimal.
- **Polygon Regularization**: Converts hand-drawn polygons into regular polygons by adjusting vertex positions while retaining the overall orientation and relative placement of vertices.
- **Visualization**: Compares original and processed paths using Matplotlib, providing clear before-and-after views of the shape transformations.

## **Usage**

### **1. Path Extraction**
Paths are extracted from a CSV file containing x and y coordinates:


### **2. Line Simplification**
The `isLine` function reduces a series of points to a straight line if the deviation from linearity is below a threshold.

### **3. Circle Detection and Contour Approximation Using OpenCV**

This project leverages OpenCV's powerful image processing capabilities to detect and approximate shapes within an image. The focus is on identifying contours and fitting geometric primitives, particularly circles, to these contours.

#### **Concepts:**

- **Contour Detection:** Contours are curves joining all continuous points along a boundary with the same color or intensity. This is a fundamental concept in image analysis, used for shape detection, object recognition, and more.

- **Gaussian Blur:** Applied to smooth the image and reduce noise, Gaussian blur is crucial for improving the accuracy of edge detection algorithms.

- **Canny Edge Detection:** A multi-stage algorithm used to detect a wide range of edges in images. It is based on finding the intensity gradients of the image, leading to more defined and detectable edges.

- **Min Enclosing Circle:** This is a mathematical approach to find the smallest circle that can completely enclose a given set of points. In the context of contours, it helps approximate the contour with the most suitable circle.

#### **Code Overview:**

- **Grayscale Conversion & Blurring:** The image is converted to grayscale and smoothed using Gaussian blur to enhance edge detection.

- **Edge Detection:** Canny edge detection is used to find the contours of the shapes within the image.

- **Contour Approximation:** Among the detected contours, the largest one is selected, and the minimal enclosing circle is calculated to fit around it.

- **Visualization:** The original image is then annotated with the detected contour and the best-fit circle, illustrating the approximation.
  <img width="262" alt="image" src="https://github.com/user-attachments/assets/5b4464e9-f080-4cb7-bf11-4c7ecc11d533">


#### **Mathematical Foundation:**
- **Contours**: Defined by level sets of the image intensity function, contours are critical in understanding the shape and geometry of objects within an image.
- **Circle Fitting**: Using principles from computational geometry, the minimal enclosing circle is a fundamental geometric primitive, providing the best-fit approximation for closed contours.

### **4. Polygon Regularlization**
This Python script utilizes OpenCV to identify and adjust the vertices of a polygonal shape in an image, making it a regular polygon while retaining the original vertex positions as close as possible. The process involves calculating the centroid, determining the radius, and adjusting vertex positions to form a regular polygon.

<img width="350" alt="image" src="https://github.com/user-attachments/assets/88f5a667-fce6-4e88-a2d9-2fa14cc4758f">


