# Weekly Graded Assignment Instructions

Read the instructions in the Think Python book for Chapter 14's Weekly Graded Assignment. Practice running the ``Chatbot`` code in the book, because we'll utilize that code in this assignment. Then follow these instructions:

Your job is to make a subclass called ``BoredChatbot`` that inherits from ``Chatbot``, but acts a little differently, in the following way:

* A bored chatbot has a short attention span. When the human says something that is longer than 20 characters, it should respond by saying:

  > “zzz... Oh excuse me, I dozed off reading your essay.”

* If, on the other hand, the human says something with a length of 20 characters or less, then the bored chatbot should respond just like a normal chatbot would.

Note that we are requiring you to use **inheritance**. Your new ``BoredChatbot`` class must be a **subclass** of the ``Chatbot`` class, and your subclass should only implement the things that make it distinct. (See the *Inheritance* chapter for a review of how this works.)

