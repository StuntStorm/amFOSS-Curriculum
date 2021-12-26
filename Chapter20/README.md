```
1. How can you trigger PyAutoGUI’s fail-safe to stop a program?
```
```
Answer:
> Move the mouse toward a corner to stop a program
```
-----------------------------------------------------
```
2. What function returns the current resolution()?
```
```
Answer:
> Using pyautogui.size() function
```
-----------------------------------------------------
```
3. What function returns the coordinates for the mouse cursor’s current position?
```
```
Answer:
> Using pyautogui.position() function
```
-----------------------------------------------------
```
4. What is the difference between pyautogui.moveTo() and pyautogui.move()?
```
```
> The pyautogui.moveTo() calls, the mouse cursor would have instantly teleported from point to point

> The pyautogui.move() function moves the mouse cursor relative to its current position
```
-----------------------------------------------------
```
5. What functions can be used to drag the mouse?
```
```
Answer:
> Using pyautogui.drag() function
```
-----------------------------------------------------
```
6. What function call will type out the characters of "Hello, world!"?
```
```
Answer:
> pyautogui.write('Hello, world!')
```
-----------------------------------------------------
```
7. How can you do keypresses for special keys such as the keyboard’s left arrow key?
```
```
Answer:
> pyautogui.write(['left'])
```
-----------------------------------------------------
```
8. How can you save the current contents of the screen to an image file named screenshot.png?
```
```
Answer:
> pyautogui.screenshot('screenshot.png')
```
-----------------------------------------------------
```
9. What code would set a two-second pause after every PyAutoGUI function call?
```
```
Answer:
> pyautogui.sleep(2)
```
-----------------------------------------------------
```
10. If you want to automate clicks and keystrokes inside a web browser, should you use PyAutoGUI or Selenium?
```
```
Answer:
> PyAutoGUI - move the mouse cursor around the screen and simulate mouse clicks, keystrokes, and keyboard shortcuts
```
-----------------------------------------------------
```
11. What makes PyAutoGUI error-prone?
```
```
Answer:
> As it stops the entire program if there is any error found and also notifies us with error message.
```
-----------------------------------------------------
```
12. How can you find the size of every window on the screen that includes the text Notepad in its title?
```
```
Answer:
> Specifying title and then using size function
```
-----------------------------------------------------
```
13. How can you make, say, the Firefox browser active and in front of every other window on the screen?
```
```
Answer:
> Using pyautogui.click() function
```
-----------------------------------------------------
