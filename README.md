# HealthVerity Assessment
This repository contains my submission for the software engineering assessment at HealthVerity.

I completed questions 1 and 2 and the total time spent was about 2 hours.

## Dependencies
Python 3.2 or later recommended

## Question 1
#### Part a
`distinct_integers()` in `question1.py` contains the solution for part a of question 1.

<strong>Assumptions:</strong> Since the input list contains integers between *0* to *N-1* and has a size of *N*, there is not need to check if the user inputs an empty list because, if *list_size=0* then *N-1 = -1* which contradicts the input specifications. However the statement below still accommodates for the possibility of an empty list nonetheless:

`if len(input_ist) <=1`

'distinct_integers()' takes in a list of integers and uses the elements as index values to go through the list. Every element that is visited is stored in a set and once a visited element is re-visited, the program stops going through the list and returns the number of elements in the set as they represent the number of distinct integers that the random generator would have produced.

#### Part b
`distinct_integers_modified()` in `question1.py` contains the solution for part b of question 1.

To improve on the implementation of part a, this function compares elements starting from the front of the list to the other elements in the list. Whenever a duplicate is found in the list, its index is stored in `first_repeated_location`. Any other duplicate values found must have a smaller index value in order for the `first_repeated_location` to be updated since `first_repeated_location` will be storing the location of the first duplicated element in the list. If there are no duplicates, `first_repeated_location` will return the length of the list.

This implementation uses O(1) auxiliary space.

(Note: if you run the tests provided, you will see that `distinct_integers_modified()` fails one of the tests therefore, the implementation would need some improvement)

## Question 2
#### Part a

Write a program that reads in the names of two files from STDIN and outputs the number of
strings they have in common to STDOUT. Each file contains 1 million strings of 32 characters,
1 per line.

`question2.py` contains the solution for part a of question 2.
The program reads in 2 files, compares their contents and returns the number of strings found in both files. The specifications of the contents of the files are provided in the assessment document.

The file names are read in as command line arguments which are then passed to `validate_files()` where we validate that they exist. If they do not exist, we check each of them to find out which one is invalid and print out this information to give the user proper feedback. 

Once the files are validated, `compare_files()` checks their contents. The words in the first file are stored in a dictionary as keys. When reading in the the second file, the words are compared to the dictionary keys and whenever the word is found in the dictionary, we update that key's value to 1. If a word occurs multiple times in the file, the dictionary value for that key will still be 1 since we are not incrementing the value but setting it to 1. After reading in all the contents of the second file, the function returns the sum of the values in the dictionary. For each key, the value is either 0 or 1. Therefore, the sum will represent the number of words in both files.

#### Part b
My implementation in part a breaks the files into chunks while working with the data but if the files being compared were very large, I would use a module, for example, filecmp, that is created to compare files. Since natural language processing also tends to deal with large files, I might look into how they compare their data and maybe get something that can handle large files.

## Testing
`question1_test.py` and `question2_test.py` contain test cases for question 1 and 2 respectively.

As mentioned above, `distinct_integers_modified()` fails one of the tests if given more time, this can be improved on.

## Running from the terminal
#### Setup
To run this project:
-   [clone](https://help.github.com/en/github/using-git/which-remote-url-should-i-use)  the repository or  [download](https://github.com/Mokeira/healthverity/archive/master.zip)  the zipped project.
-   Ensure you have Python installed (Python3 recommended)

Once you are done setting up the files, navigate to the project directory.

#### Running question1.py
To run question1.py use the following command:
	` python -c 'from question1 import func; print(func(args))'`
where `func` is the function name and args represents the arguments where applicable

#### Running question2.py
To run question2.py with the sample text files provided use the following command :`python question2.py f1.txt f3.txt`
You can replace `f1.txt` and `f2.txt` with the input files you want to use.

### Running the test files
To run the test files, use the command `python fileName` where fileName is either `question1_test.py` or `question2_test.py`.
If you choose to suppress the output from the functions, you can use the command `python fileName -b`
