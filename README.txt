Name: Lucia Jeon
Net ID: sj2798
Professor: Jeff Epstein
Lecture Session: C

1. The state of the work
I successfully completed the assignment. I chose iris classification. My project meets all the requirements specified in the demos including analyzing two csv files, finding different mathematical values, predicting the types of iris, and plotting the data using turtle module. Regarding artistic liberty, I was able to set my own color preferences for each types of iris when plotting on the canvas.
I made my own function called 'square' that takes two parameters (size, color) and draws a square on to the canvas. Additionally, I created inner functions that is inside the functions given, for example, 'min' and 'max' in order to minimize repetitive codes. I am satisfied with the final result and want to try applying this prediction method into other fields.

2. Retrospective on the development process
Writing functions that create table from a file and calculate each numeric values according to mathematical formula was easier than I expected. However, normalizing the values in the list was a bit challenging since I had to clarify the normalized value from the original value. At first, I made a function inside the function that returns a list of normalized values, so that I can easily calculate the mean and the standard deviation using the another functions. However, I realized 'normalize_data' function should be mutating, not pure. Therefore, I changed the code so that it can change the items in the list in the given parameter. I had to store the means and standard deviations of the features before normalization in order to print it out as well as with normalized means and standard deviations.


3. Additional thoughts or questions
Instructions were clear enough to follow and I had given enough support both from my lab TAs and professor. I was especially impressed when I got instant reply from the professor at 2am when I sent my code to the professor because my error percentage was not right. I was told that my 'normalize_data' function is not actually normalizing the data and it really helped me fix my code. This project taught me that there can be things I did wrong but I don't realize. Even if I try different methods to check which part is wrong, there exists problems that requires new eyes. Therefore, this project was important to me because I came to admit that I'm not the best coder here, or even in our class, and I do need help.