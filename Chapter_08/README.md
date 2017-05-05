# Weekly Graded Assignment Instructions

Write a function ``analyze_text`` that receives a string as input. Your function should count the number of alphabetic characters (a through z, or A through Z) in the text and also keep track of how many are the letter ``'e'`` (upper or lowercase).

Your function should return an analysis of the text in exactly the same format as below:

```nohighlight
The text contains 240 alphabetic characters, of which 105 (43.75%) are 'e'.
```

You will need to make use of the ``isalpha`` function, which can be used like this

```nohighlight
"a".isalpha() # => evaluates to True
"3".isalpha() # => evaluates to False
"&".isalpha() # => False
" ".isalpha() # => False

mystr = "Q"
mystr.isalpha() # => True
```