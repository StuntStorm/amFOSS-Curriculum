```
1. What is an RGBA value?
```
```
Answer:
> An RGBA value is a group of numbers that specify the amount of red, green, blue, and alpha in a color
```
-----------------------------------------------------
```
2. How can you get the RGBA value of 'CornflowerBlue' from the Pillow module?
```
```
Answer:
> from PIL import ImageColor

> ImageColor.getcolor('CornflowerBlue', 'RGBA')

> Using ImageColor() function
```
-----------------------------------------------------
```
3. What is a box tuple?
```
```
Answer:
> It means pillow is expecting a tuple of four integer coordinates that represent a rectangular region in an image.
```
-----------------------------------------------------
```
4. What function returns an Image object for, say, an image file named zophie.png?
```
```
Answer:
> Image.open('zophie.png')
```
-----------------------------------------------------
```
5. How can you find out the width and height of an Image object’s image?
```
```
Answer:
> Using catIm.size() function
```
-----------------------------------------------------
```
6. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?
```
```
Answer:
> Using resize() function
```
-----------------------------------------------------
```
7. After making changes to an Image object, how could you save it as an image file?
```
```
Answer:
> Using save() function
```
-----------------------------------------------------
```
8. What module contains Pillow’s shape-drawing code?
```
```
Answer:
> ImageDraw object code
```
-----------------------------------------------------
```
9. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?
```
```
Answer:
> Pillow’s module has ImageDraw. Using ImageDraw.Draw object by importing the PIL.
```
-----------------------------------------------------
