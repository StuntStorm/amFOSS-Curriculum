```
1. Briefly describe the differences between the webbrowser, requests, bs4, and selenium modules.
```
```
Answer:
> webbrowser - Comes with Python and opens a browser to a specific page.

> requests - Downloads files and web pages from the internet.

> bs4 - Parses HTML, the format that web pages are written in.

> selenium - Launches and controls a web browser. The selenium module is able to fill in forms and simulate mouse clicks in this browser.

```
-----------------------------------------------------
```
2. What type of object is returned by requests.get()? How can you access the downloaded content as a string value?
```
```
Answer:
> Response object

> print(res.text)
```
-----------------------------------------------------
```
3. What requests method checks that the download worked?
```
```
Answer:
> raise_for_status()
```
-----------------------------------------------------
```
4. How can you get the HTTP status code of a requests response?
```
```
Answer:
> Using the status_code attribute of the Response object
```
-----------------------------------------------------
```
5. How do you save a requests response to a file?
```
```
Answer:
> Using open() function and write() method
```
-----------------------------------------------------
```
6. What is the keyboard shortcut for opening a browser’s developer tools?
```
```
Answer:
> CTRL-SHIFT-C on Windows and Linux or by pressing Command-OPTION-C on macOS
```
-----------------------------------------------------
```
7. How can you view (in the developer tools) the HTML of a specific element on a web page?
```
```
Answer:
> CTRL-SHIFT-I on Windows and Linux or by pressing Command-Options-I on macOS
```
-----------------------------------------------------
```
8. What is the CSS selector string that would find the element with an id attribute of main?
```
```
Answer:
> Using soup.select('#main')
```
-----------------------------------------------------
```
9. What is the CSS selector string that would find the elements with a CSS class of highlight?
```
```
Answer:
> 	
Using .highlight
```
-----------------------------------------------------
```
10. What is the CSS selector string that would find all the <div> elements inside another <div> element?
```
```
Answer:
> Using div div
```
-----------------------------------------------------
```
11. What is the CSS selector string that would find the <button> element with a value attribute set to favorite?
```
```
Answer:
> button[value="favorite"]
```
-----------------------------------------------------
```
12. Say you have a Beautiful Soup Tag object stored in the variable spam for the element <div>Hello, world!</div>. How could you get a string 'Hello, world!' from the Tag object?
```
```
Answer:
> str.getText()
```
-----------------------------------------------------
```
13. How would you store all the attributes of a Beautiful Soup Tag object in a variable named linkElem?
```
```
Answer:
> linkElem.attrs
```
-----------------------------------------------------
```
14. Running import selenium doesn’t work. How do you properly import the selenium module?
```
```
Answer:
> Run from selenium import webdriver
```
-----------------------------------------------------
```
15. What’s the difference between the find_element_* and find_elements_* methods?
```
```
Answer:
> The find_element_* methods return a single WebElement object, representing the first element on the page that matches your query

> The find_elements_* methods return a list of WebElement_* objects for every matching element on the page
```
-----------------------------------------------------
```
16. What methods do Selenium’s WebElement objects have for simulating mouse clicks and keyboard keys?
```
```
Answer:
> Using click() method and send_keys() calls
```
-----------------------------------------------------
```
17. You could call send_keys(Keys.ENTER) on the Submit button’s WebElement object, but what is an easier way to submit a form with selenium?
```
```
Answer:
> Using emailElem.submit() function
```
-----------------------------------------------------
```
18. How can you simulate clicking a browser’s Forward, Back, and Refresh buttons with selenium?
```
```
Answer:
> browser.forward() - Forward button

> browser.back() - Back button

> browser.refresh() - Refresh button
```
-----------------------------------------------------
