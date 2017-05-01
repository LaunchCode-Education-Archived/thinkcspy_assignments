# Weekly Graded Assignment Instructions

This is a tricky one!

You have a thermostat that allows you to set the room to any temperature between 40 and 89 degrees.

The thermostat can be adjusted by turning a circular dial. If it is currently at 40 degrees and you turn to the right by one click, you will get 41 degrees. As you continue to turn to the right, the temperature goes up, and the temperature gets closer and closer to 89 degrees. But as soon as you complete one full rotation (50 clicks), the temperature cycles back around to 40 and starts over. By the same token, if it is currently at 40 degrees and you turn it left one click, you will get 89 degrees.

Here is the start of a program that calculates the temperature based on how much the dial has been turned. The user is prompted for a number of clicks (from the starting point of 40 degrees). If the user enters a positive number, then the clicks are to the right; if the user enters a negative number, then the clicks are to the left. Your job is to write code for the function ``calculate_temp`` that figures out the current temp based on how many clicks the user has entered. Your code should go between the commented line and the return statement. 

Here is an example of how your program should behave (When you see >>>, that line represents what the user is typing in):

```nohighlight
By how many clicks has the dial been turned?
>>> 0
The temperature is 40

By how many clicks has the dial been turned?
>>> 24
The temperature is 64

By how many clicks has the dial been turned?
>>> 74
The temperature is 64

By how many clicks has the dial been turned?
>>> 49
The temperature is 89

By how many clicks has the dial been turned?
>>> 51
The temperature is 41

By how many clicks has the dial been turned?
>>> -1
The temperature is 89
```