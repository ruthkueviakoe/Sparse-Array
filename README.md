# Sparse Array

Sparse Array repository allows you to count the number of occurences of the strings in the list "queries" that occurs in the list "strings". The list strings is given in the shell as follow :

**python -m main ab,abc,bc**


## Prerequisites

It is recommended to have the last version of Python : **Python 3.7**

### Running with Docker
Example invocation:

    $ docker build -t testdocker /home/ruth_kueviakoe/testdocker (the path where the files of the repository are)
    $ docker run -it testdocker  aba,er,baba
    
In the dockerfile the environment variable ENV strings has to be defined by you. Only the list queries can be modify by the person who wants to execute directly the dockerfile.

## Examples :

If you run :

**python -m main ab,abc,bc** with the strings list ['ab','er','bc']

The shell command will display : {'ab': 1, 'er': 0, 'bc': 1} 
