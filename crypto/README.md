# Crypto Assignment Instructions

In contrast with the small isolated exercises you have been doing so far, the goal of this assignment is to give you the opportunity to create something a little larger and more complicated.

This assignment consists of 4 parts:

1. **Caesar:** An encryption algorithm.
2. **Vigenere:** An even cooler encryption algorithm.
3. **Refactoring Shared Code:** Make some improvements to the way your code is structured.
4. **Bonus Missions:** Add a couple of additional features to improve user experience and prevent against crashes. (This section is optional).

## Setup

Your folder for this assignment will look a little different from the previous exercises. Inside this directory are five Python files that replace the usual ``solution.py`` file: ``caesar.py``, ``vigenere.py``, ``helpers.py``, ``caesar_final.py``, and ``vigenere_final.py``. They will be used as follows: 
* In Part 1, you'll add code to the ``caesar.py`` file. 
* In Part 2, you'll add code to the ``vigenere.py`` file. 
* In Part 3, you'll add code to the ``helpers.py``, ``caesar_final.py``, and ``vigenere_final.py`` files. 

You can run the unit tests for this assignment with the ``pytest`` command at any time in this process. You should pass all of the tests in the test files listed below at the following stages:
* At the end of Part 1, pass tests in ``test_caesar.py``.
* At the end of Part 2, pass tests in ``test_vigenere.py``. 
* At the end of Part 3, pass tests in ``test_crypto.py``.  

> **Note:** After running ``pytest`` you should look at the terminal message to see which tests in which test files failed, then you can go to the relevant file(s) and see exactly which functions were being tested in each unit test, and therefore determine where your code needs to be corrected.  

> **Note:** You will not pass ALL unit tests for this assignment until you have finished Part 3. That is when you should run ``pytest --html=report.html``. At that point, if you pass all the tests, you can push your repo to GitHub with the new, complete, ``report.html``.

## Part 1: Caesar

Now it’s time for some encryption!

In Chapter 9, you might have worked on an exercise that asked you write a function called ``rot13``, which used the [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher#History_and_usage) to encrypt a message. If you need a refresher, this is what the exercise said:

> Write a function called ``rot13`` that uses the Caesar cipher to encrypt a message. The Caesar cipher works like a substitution cipher but each character is replaced by the character 13 characters to "its right" in the alphabet. So for example the letter a becomes the letter n. If a letter is past the middle of the alphabet then the counting wraps around to the letter a again, so n becomes a, o becomes b and so on.  
> *Hint:* Whenever you talk about things wrapping around its a good idea to think of modulo arithmetic.

The idea is to iterate over the message character by character, rotating each letter 13 places to the right. So for example:

* a becomes n
* b becomes o,
* c becomes p
* ... and so on.

At the end of the alphabet we wrap back around to a, so that:

* m shifts to z
* n shifts to a
* o shifts to b
* ...etc

The end result is a *super secret coded message* that looks like gibberish to any outsiders.

We’re going to build a more general version of the rot13 algorithm that allows a message to be encrypted using *any* rotation amount, not just 13. Ultimately, users will be able to type a message in the terminal, and specify a rotation amount (13, 4, 600, etc), and your program will print the resulting encrypted message.

The final *interactive* program will run like this:

```nohighlight
$ python caesar.py
Type a message:
Hello, World!
Rotate by:
5
Mjqqt, Btwqi!
```

We are going to do this in a few steps, using some helper functions. This will help break the problem down into manageable steps. Furthermore, you will be able to reuse the same helper functions when you move on to Part 2.

### alphabet_position
Open up your ``caesar.py`` file in Visual Studio Code. In that file, write a function ``alphabet_position(letter)``, which receives a letter (that is, a string with only one alphabetic character) and returns the 0-based numerical position of that letter within the alphabet.

Here are some example input parameter values, with the corresponding return values.

| ``letter``  | return value |
|-------------|--------------|
| a | 0 |
| A | 0 |
| b | 1 |
| y | 24 |
| z | 25 |
| Z | 25 |

> **Note:** The function should be case-insensitive.

> **Note:** You can assume that your input will definitely be a letter. Don’t worry about what might happen if somebody tries to use your function with an input parameter that is something other than a single letter, like ``alphabet_position("grandpa22!")``

> **Warning**  
>It is important that you test your function to make sure it works **before moving on**. This practice of testing each little piece of your code in isolation before trying to put all the pieces together will save you a lot of time and headaches. Pay attention to which tests it passes and which it fails when you run ``pytest``. As long as it passes the unit tests for this function in the relevant test file, you're okay to move on!

### rotate_character
Next, write another helper function ``rotate_character(char, rot)`` which receives a character ``char`` (that is, a string of length 1), and an integer ``rot``. Your function should return a new string of length 1, the result of rotating ``char`` by ``rot`` number of places to the right.

Here are some example input values, with the corresponding return values.

| ``char`` | ``rot`` | return value |
|----------|---------|--------------|
| a | 13 | n |
| A | 14 | O |
| a | 0 | a |
| c | 26 | c |
| C | 27 | D |
| z | 1 | a |
| Z | 2 | B |
| z | 37 | k |
| ! | 37 | ! |
| 6 | 13 | 6 |

> **Note:** The upper or lower case of the letter should be preserved. For example, ``rotate_character("A", 13)`` results in "N", rather than "n".

> **Note:** For non-alphabetical characters, you should ignore the ``rot`` argument and simply return ``char`` untouched. For example, see "!" and "6" in the table above.

> **Hint**  
> You should make use of your own alphabet_position function! If feeling confused, you may want to re-read about how [Functions Can Call Other Functions](https://runestone.launchcode.org/runestone/static/thinkcspy/Functions/Functionscancallotherfunctions.html)

> **Warning**  
> Once again, before moving on to the next stage, make sure to run the unit tests and make sure that all tests for this function pass.

### encrypt

Now let’s get to the heart of the matter. Write one more function called ``encrypt(text, rot)``, which receives as input a string and an integer. This is just like the ``rot13`` function, but instead of hardcoding the number 13, your function should receive a second argument, rot which specifies the rotation amount. Your function should return the result of rotating each letter in the ``text`` by ``rot`` places to the right.

Here are some example input values, with the corresponding return values:

| ``text`` | ``rot`` | return value |
|----------|---------|--------------|
| a | 13 | n |
| abcd | 13 | nopq |
| LaunchCode | 13 | YnhapuPbqr |
| LaunchCode | 1 | MbvodiDpef |
| Hello, World! | 5 | Mjqqt, Btwqi! |


> **Note:** The ``text`` argument might contain non-alphabetic characters (spaces, numbers, symbols). You should leave these as they are.

> **Hint**  
> You should make use of your own ``rotate_character`` function (which should make it very easy to satisfy the condition above).

> **Warning**  
> Don’t forget to test! At this point, your code should pass all the tests in ``test_caesar.py``, though it will still fail those in ``test_vigenere.py`` and ``test_crypto.py``; don't worry, that won't be the case for long!

### Make It Interactive

You’re almost done with Caesar! The last step is simply to write some ``print`` and ``input`` statements so the user can run your program from the terminal. Remember, you should ask the user for their message and rotation amount, and then print the encrypted message:

```nohighlight
$ python caesar.py
Type a message:
Hello, World!
Rotate by:
5
Mjqqt, Btwqi!
```

Recall that, as described in the *Initials* assignment, you should place everything “loose” inside a ``main`` function, like this:

```python
# ... the functions you wrote ...


def main():
    # your main code (input and print statements)

if __name__ == "__main__":
    main()
```

## Part 2: Vigenere

If you’re trying to pass notes in the back of class with your best friend Suzie, the Ceasar cipher would be fairly easy for a nosy outsider to decode. Let’s implement a more complicated cipher algorithm.

First, watch [this short video](https://www.youtube.com/watch?v=9zASwVoshiM&feature=youtu.be) on the Vigenere cipher, courtesy of the CS50 folks at Harvard.

As you can see in the video, Vigenere uses a word as the encryption key, rather than an integer. Your finished program will behave like this:

```nohighlight
$ python vigenere.py
Type a message:
The crow flies at midnight!
Encryption key:
boom
Uvs osck rmwse bh auebwsih!
```

Above, the user entered a message of “The crow flies at midnight” and an encryption key of “boom”, and the program printed “Uvs osck rmwse bh auebwsih!”.

How did we arrive at that result? Here is a detailed breakdown:

| char from input string | char from key | rotation amount | result char |
|------------------------|---------------|-----------------|-------------|
| T | b | 1 | U |
| h | o | 14 | v |
| e | o | 14 | s |
| (space) | n/a | n/a | (space) |
| c | m | 12 | o | 
| r | b | 1 | s |
| o | o | 14 | c |
| w | o | 14 | k |
| (and so on...) | | |

> **Note**  
> As with Caesar, the upper or lower case of each character should be preserved, and non-alphabetical characters like ``" "`` and ``"!"`` should not get encrypted.

> **Note**  
> When we encounter a non-alphabetical character in the message, the *encryption key* does not use up another letter. For example, notice how the ``"m"`` in ``"boom"`` does not get "wasted", so to speak, on the space character. Instead, it is "saved" for the next alphabetical character, the ``"c"`` in ``"crow"``.

> **Note**  
> Whenever we reach the end of the encryption key (“boom”) before reaching the end of the message, the encryption key wraps back around to the beginning again (the letter “b”).


> **Note**  
> You may assume that the encryption key (“boom”) will not contain any numbers or special characters. Letters only.

### Reusing your Caesar code

You probably noticed that Vigenere is very similar to Caesar. The only difference is that the rotation amount varies throughout the course of the message.

Whenever you find yourself in a situation like this–faced with a coding task that is very similar to one you did previously–your instinct should be to sniff around for ways to reuse the code you have already written. Ideally, all the work that is required by both tasks should be factored out into reusable components (like functions).

In this case, the majority of the logic that Vigenere has in common with Caesar is encapsulated in those two helper functions you wrote, ``alphabet_position`` and ``rotate_character``. Indeed, that is why we intentionally guided you down the path of writing those functions. You are going to find both of those functions equally helpful for implementing Vigenere.

Go ahead and copy / paste those functions into ``vigenere.py`` so you can use them. (In reality, copy / pasting is not a very smart thing to do here, and there is a better way, which you will see farther down in this assignemnt. But for now, just do it.)

### encrypt

Now that you have your helper functions, go ahead and write a new version of the ``encrypt`` function which uses the Vigenere cipher rather than Caesar.

Your first step is to figure out what the function signature should say. How should it be different from the Caesar version, ``def encrypt(text, rot)``?

As usual, don’t move on until you have run ``pytest`` for this directory. At this point, your code should pass all the tests in both ``test_caesar.py`` and ``test_vigenere.py`` before moving on.

### Make It Interactive

Finally, add the appropriate ``print`` and ``input`` statements inside a ``main`` function so that your program behaves as specified:

```nohighlight
$ python vigenere.py
Type a message:
The crow flies at midnight!
Encryption key:
boom
Uvs osck rmwse bh auebwsih!
```

## Part 3: Refactoring Shared Code

Remember when we said that copy / pasting those helper functions is not a smart thing to do? Now let’s do something better.

The reason that copy / pasting is a bad idea is that now you have two copies of the same exact code lying around. What happens if you realize you need to change the function? You will have to remember to make the same change in both copies. That might not sound so bad, but imagine if you had not two, but three copies, or six, or eleven? Given that you want to use the same function everywhere, that function should only ever be defined once.

### Import to the Rescue

If a function is only defined in one place, a particular file somewhere, then how can some other file use it? It is actually quite easy: the other file simply needs to import the function. You have already used the ``import`` keyword throughout this course, whenever you wanted to access code written by other people, such as the ``math`` and ``random`` modules. It is also possible to create and import your own code. Here’s how:

1. In your editor, open the file called ``helpers.py``. Paste both helper functions, ``alphabet_position`` and ``rotate_character`` into this new file.
2. Next, open up ``caesar_final.py``, and paste **only** your ``encrypt`` method from ``caesar.py``.
3. Finally, add this line to the top of ``caesar_final.py``:

```python
from .helpers import alphabet_position, rotate_character

"""This says that we want to import code from a module named helpers, but that we only want to import 
particular pieces of that module, specificially the functions alphabet_position and rotate_character. 
Note that this works because caesar_final.py is in the same directory as helpers.py"""
```

Now we should be able to use those functions! Try running the unit tests again and you should find that the unit tests in ``test_crypto`` that use ``caesar_final.encrypt()`` pass.

> **Note:** The technique we are using here is a little simpler than the way this is normally done. For larger projects, where the structure is a tree of folders within folders, there is a slightly more involved procedure for reusing code, which does not require both modules to live together in the same folder. If you’re curious, you can read up more about creating modules in Python in the [Python module documentation](https://docs.python.org/3/tutorial/modules.html).

Once you have Caesar working, do the same thing for Vigenere by copying only the ``encrypt`` method from ``vigenere.py`` into ``vigenere_final.py`` and adding the import statement for ``helpers.py``. 

Now your helper functions are defined only once, and your code remains nice and DRY (Don’t Repeat Yourself)!

At this point, go ahead and run ``pytest --html=report.html`` and check that **all** tests are passing. Then add and commit your changes and push to GitHub.

## Part 4: Bonus Missions

Then [go here](https://runestone.launchcode.org/runestone/static/thinkcspy/ProblemSets/Crypto.html) to read about the Bonus Missions toward the bottom of the page.

If you decide to do the Bonus Missions, then make a new directory and copy the files from the ``crypto`` directory into that new directory so that you can play around with them without affecting your graded code. 

