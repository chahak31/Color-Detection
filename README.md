**Color Detection using OpenCV and Pandas Libraries**

* **Pandas** Library is used to read the csv file 
* **OpenCV** is used to open and read the image as array of pixels

STEPS Followed:

* Read the csv file with headers color, color_names, R G, B values
* Open the image and resize/ adjust it in the window
* Get the co-ordinates of a particular point clicked by the mouse, and find the b, g, r values (In openCV the pixel values are taken as b, g, r)
* find the name of the color from the csv file with the help of 'abs' (absolute) and the minimum difference

**Functions**
        
        def get_color_name(R,G,B)
        def draw_function(event, x, y, flags, params)
