# 🔎 Search on Data Scientist path

This note contains the things I've learned from the Dataquest's [Data Scientiest path](https://www.dataquest.io/path/data-scientist/). The codes and takeaways are stored [on Github](https://github.com/dinhanhthi/dataquest-aio). This note is used to show the concepts/methods I've learned from these courses for the purpose of looking up later.

> Please use `Ctrl` + `F` (on Win) or `⌘` + `F` (on Mac) to search on this page.

## 🐍 Step 1: Python Introduction

### 📚 Course 1: Python for Data Science — Fundamentals

- **[Task 1: Programming in Python](https://github.com/dinhanhthi/dataquest-aio/blob/master/step-1-python-introduction/course-1-python-for-ds-fundamentals/task-1-programming-in-python.ipynb)**. Very basic math operators in python. You will also learn to `print` something in one line or multi-lines, change data types from `int` to `float` and vice versa.
- **[Task 2: Variables and Data Types](https://github.com/dinhanhthi/dataquest-aio/blob/master/step-1-python-introduction/course-1-python-for-ds-fundamentals/task-2-variables-and-data-types.ipynb)**. Using operators like `+=` (and others) to add more values to current variables. You also learn about `string` and its operators.
- **[Task 3: Lists and For loops](https://github.com/dinhanhthi/dataquest-aio/blob/master/step-1-python-introduction/course-1-python-for-ds-fundamentals/task-3-lists-and-for-loops.ipynb)**
  - Learn about list in Python: length (size, number of elements) of a list, negative indexes, print a list, first/last element of the list, list of lists, append a new element into list.
  - How to open a `.csv` file using `open()`.
  - How to use `for` loop in Python.
- **[Task 4: Conditional Statements](https://github.com/dinhanhthi/dataquest-aio/blob/master/step-1-python-introduction/course-1-python-for-ds-fundamentals/task-4-conditional-statements.ipynb)**. 
  - Every things about `if` statement (`if..else..elif...`): comparison, operators,... in the if statement.
  - Sum of all elements in a list using `sum`.
- **[Task 5: Dictionaries and Frequency Tables](https://github.com/dinhanhthi/dataquest-aio/blob/master/step-1-python-introduction/course-1-python-for-ds-fundamentals/task-5-dictionaries-and-frequency-tables.ipynb)**
  - How to create a dictionary in python, what it is. Check if a key already exists in dictionary.
  - Understand the `hash` function (the way python use to read a "key" in dictionary).
  - Count the number of each unique values in a column of a dataset and then add them to a dictionary.
  - Find the frequency of a table.
- **[Task 6: Functions](https://github.com/dinhanhthi/dataquest-aio/blob/master/step-1-python-introduction/course-1-python-for-ds-fundamentals/task-6-functions.ipynb)**
  - How to create a function in python.

## 🧹 Step 2: Data Analysis and Visualization

### 📚 Course 4: Data Cleaning and Analysis

- **[Datasets](https://github.com/dinhanhthi/dataquest-aio/tree/master/step-2-data-analysis-and-visualization/course-4-data-cleaning-and-analysis/data)**: World Happiness Report in 2015, 2016, 2017 & Economic data from the World Bank.
- **[Task 1: Data Aggregation](https://github.com/dinhanhthi/dataquest-aio/blob/master/step-2-data-analysis-and-visualization/course-4-data-cleaning-and-analysis/task-1-data-aggregation.ipynb)**
  - Plot directly with dataframe using `df.plot()` with an option `kind='barh'` (horizontal bars).
  - Check unique values in each column (Series) of df by using `s.unique()`.
  - We can create a new dataframe with index is (a) group(s) and values are other groups using `df.pivot_table()` and `df.groupby` methods.
- **[Task 2: Combining Data with Pandas](https://github.com/dinhanhthi/dataquest-aio/blob/master/step-2-data-analysis-and-visualization/course-4-data-cleaning-and-analysis/task-2-combining-data-with-pandas.ipynb)**
  - Combine different dataframes using `pd.concat()` (two directions); joining like in SQL (inner join, outer, left join, right) using `df.merge()` method.
  - Display side by side dataframes.
  - Rename columns using `df.rename()`.
- **[Task 3: Transforming data with pandas](https://github.com/dinhanhthi/dataquest-aio/blob/master/step-2-data-analysis-and-visualization/course-4-data-cleaning-and-analysis/task-3-transforming-data-with-pandas.ipynb)**
  - We wanna apply (or `map`) some functions on (some) columns using `df.map()` or `df.apply()` or `df.applymap()` methods.
  - Count the number of values each in a column using `pd.value_counts`.
  - Reshape current dataframe to a new one by put some columns into one single one whose values are the name of these columns. We can use `pd.melt()` method. We need this task for the vectorized methods (faster).
  - We can split unique values of a columns into new columns using `pdf.pivot()` (inverse of `pd.melt()`).
- **[Task 4: Working with Strings in Pandas](https://github.com/dinhanhthi/dataquest-aio/blob/master/step-2-data-analysis-and-visualization/course-4-data-cleaning-and-analysis/task-4-working-with-strings-in-pandas.ipynb)**
  - How many columns in dataframe?
  - How to turn of `chained_assignment` warning.
  - Check if there are missing values in the column.
  - Using vectorized string methods (`Series.str.split()` for example).
  - Using Regular Expressions (RegEx) and `re` package.
- **[Task 5: Working with missing and duplicate Data](https://github.com/dinhanhthi/dataquest-aio/blob/master/step-2-data-analysis-and-visualization/course-4-data-cleaning-and-analysis/task-5-working-with-missing-and-duplicate-data.ipynb)**



