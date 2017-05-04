# Initials Assignment Instructions

## Phase One: The Initials Program

In this folder's ``solution.py`` you'll find the function ``get_initials`` stubbed out. Your job is to code this function. Your function will receive one argument – ``fullname``, a string representing someone’s name – and should return a string with that name’s capitalized initials.

Here are some examples of what your function should return for various ``fullname`` arguments:

| ``fullname``  | return value |
|---------------|--------------|
| Ozzie Smith | OS |
| Bonnie blair | BB |
| George | G |
| Daniel Day Lewis | DDL |

> **Note:** Even if the name starts with a lowercase letter, you should always capitalize the initials. For example, notice how even if ``fullname == "Bonnie blair"``, you should still return "BB" rather than "Bb".

> **Note:** You may assume that the name will contain only letters (uppercase and/or lowercase) plus single spaces between words. This means you don’t have to worry about Conan O’Brien, T.S. Eliot, or Cee-Lo Green.

You can test your code as you have for the other assignments, by using ``pytest`` on the command line while in this folder.

## Phase Two: Make It Interactive

Once your code passes the tests in ``test_solution.py``, you can move on to the next phase of the assignment: getting input from a user and printing output. To do this, add an input statement that queries the user for his or her name and a print statement that prints out the user's initials. Once you have added the input and print statements, you can test your code by running the program from the command line by entering ``python solution.py`` while in this directory. Your program should now work like this: 

```nohighlight
$ python solution.py
What is your full name?
Ozzie Smith
OS
```

Just to be clear about the example above:

* The user typed the first line, causing the program to run.
* Then, the program printed the second line asking for their name.
* Then the user typed the third line (“Ozzie Smith”).
* Finally, the program printed the initials (“OS”).

## Phase Three: Make It Importable

Almost done! There is one more thing you must do before pushing your work to GitHub. Presumably, your file now looks like this:

```python
def get_initials(fullname):
    # some code here

# some more code here (input and print statements)
```

As you know, the second block of code contains the lines that actually get executed when the user runs the script. The code *inside* the ``get_initials`` function, by contrast, only executes thanks to the fact that it *gets invoked* by one of the statements from that second block of code that sits all the way on the left, at the global level of scope.

Generally speaking, however, it is actually bad practice to have “loose” statements floating around at that left-most, unindented scope of a script. There are two reasons why:

**Issue 1: Organization.** As your script grows larger, it can become hard to keep track of all those loose statements, especially if you don’t keep them all together in one block. At that point, you will start to loose track of exactly what happens when the script is run.

**Issue 2: Importing.** When some other file tries to ``import`` this file, all the loose statements will be executed, which is probably not what the other file wanted. For example, say you are writing another script, and you once again encounter the need to parse initials from people’s names. Instead of re-writing the ``get_initials`` function, this is a perfect chance to reuse the code you have already written by importing your ``solution.py file``. Sounds great! But unfortunately, the moment you import the file, those ``input`` and ``print`` statements will blurt out and start talking to the user.

The solution to Issue 1 is to move your ``input`` and ``print`` statements into a ``main`` function, like this:

```python
def get_initials(fullname):
    # some code here

def main():
    # some more code here (input and print statements)

main()
```

In the new version, notice that we have placed the second block of code inside a function called ``main``. This is the generally accepted pattern: Move all loose statements into a ``main`` function so that you have them together in one place. Finally, the *only* loose statement left is the invocation of ``main`` at the end.

Issue 2 can be solved by adding one more line of code that places the ``main()`` invocation inside a (strange-looking) ``if`` statement:

```python
def get_initials(fullname):
    # some code here

def main():
    # some more code here (input and print statements)

if __name__ == '__main__':
    main()
```

In effect, that conditional says:

> “If this is actually the main program that is being run, then go ahead and execute the main function. Otherwise, if this file is being imported, or something else is going on, then stay quiet and do nothing.”
> *Note:* If you are curious about the ``if __name__ == '__main__':`` conditional, you can check out [this Stack Overflow post](http://stackoverflow.com/questions/419163/what-does-if-name-main-do#419185).

Now we are good to go! The program works normally when run directly from the command-line, but if some other file imports it, the main function will not execute.

