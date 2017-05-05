# Thinkcspy Assignments

This repository will be used to create and submit your homework solutions. There are a few steps you'll need to take to get this set up on your computer so you can work on it locally. We'll describe those in the next section. Then, we'll describe how to use the repository, i.e., what is in the folder for each chapter, what files you will need to change, and how your homework will be graded. 

## Set Up Instructions

The repository ``thinkcspy_assignments`` should be in your GitHub account at this point, and you should have Python installed locally. The steps you'll take to complete your set up are:  

1. Open git bash or a terminal window. 
2. Clone this repository on your computer by using the command ``git clone`` and then the url for your account's repository. 
3. Install the package ``pytest`` using the command ``conda install pytest``. 
4. Then install the package ``pytest-html`` using the command ``pip install pytest-html``. 

## How to Test and Submit Your Homework

The process for doing your homework for each chapter is:  

1. Look at the "Weekly Graded Assignment Instructions" in the README.md for that chapter. There will occasionally be differences between the book's assignment instructions and the instructions in your repository. When there is a difference, **always** follow the repository instructions over the book's.  

2. Open up the chapter's folder in your text editor and view the ``solution.py`` file. This file contains the code stub that you will start working with. You will put the rest of the code needed to solve the assignment in this file. When you feel ready to test your code, take the next step.  

3. Open git bash or a terminal window and ``cd`` into your repository directory, and then into this chapter's folder.  

4. Run the command ``pytest``. You will see a printout of results from the tests executed for this chapter's assignment. If any of the tests failed, you know that you need to go back and fix or expand your code so that all the tests pass.  

5. It may be helpful to look at the ``test_solution.py`` file to see what kind of tests your code needs to pass.  

6. When your code passes all the tests, then you are ready to "grade" your assignment. Here is the process: 

* ``cd`` into the repository's base directory (where all the chapter folders live)
* run the command ``pytest --html=report.html`` (and be sure NOT to put spaces around the ``=`` sign). Note that the tests from **ALL** chapters will be run, so don't panic if you see that a lot of tests failed. This is because you have not solved them yet! 
* check ``report.html`` and make sure that all the tests for the chapter you are working on, and those of previous chapters, have passed.  

In order to view ``report.html`` online and show it to your T.A., you'll need to do the following steps.  

7. Add and commit your changes, then push your repository to GitHub.  

8. *This step only needs to be done once!* 

* Go to your thinkcspy_assignments repository on GitHub, then click into the ``report.html`` file.  
* Copy the url address for this page.  
* Go to [RawGit](http://rawgit.com/) and paste the url address into the input field in the center.  
* Then copy the address that appears under the heading "Use this URL for development". You will paste that address into the browser bar and go to that address to see your test report. You should bookmark this page to keep it handy. It will automatically update to show the latest ``report.html`` that you push into your GitHub repo. 
* After you've done this once, you can skip this step and go to the next for future assignments. 

9. Show your ``report.html`` to your T.A. by going to the RawGit address for your report page.  

10. Bask in the glow of a job well done!

## Python Style Tips  

There are some important standards for how to write code in Python that are outlined in the official [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/). Not everything in here will make sense at this early stage of your coding journey, so just be aware of this resource, and consult it if you have questions about how your code should look, what kind of naming to use, etc.  

There is one **very important** standard to note. You must be consistent with your choice of using either tabs or spaces to indent your code blocks. The recommended standard, and the one used in all the stub code in your ``solution.py`` files, is to use 4 spaces as your indenting method. If you do not follow this standard and instead mix tabs and spaces, Python will complain and your tests won't run.




