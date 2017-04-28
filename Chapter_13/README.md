# Weekly Graded Assignment Instructions

The starter code in this chapter's ``solution.py`` contains a ``Point`` class with a method ``slope_from_origin``, which should return the slope of the line joining the origin to the point. For example,

````nohighlight
>>> Point(4, 10).slope_from_origin()
2.5
>>> Point(12, -3).slope_from_origin()
-0.25
>>> Point(-6, 0).slope_from_origin()
0
````

The equation for calculating the slope between any two points is **slope = (Y2 - Y1) / (X2 - X1)**. Remember that dividing by 0 is not allowed, so there are some inputs that will cause your method to fail. Return ``None`` when that happens.