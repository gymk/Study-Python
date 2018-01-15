# List of python based utilities coded

## my_grep_v1.py

This performs search and print those matching lines

> file is of size 1.4GiB
> time my_grep_v1.py 'text' 'file' > out.txt
> real	0m2.546s
> user	0m2.185s
> sys	0m0.360s


## my_grep_v2.py

Using generator implementing the same funcitonality.

> file is of size 1.4GiB
> time my_grep_v2.py 'text' 'file' > out.txt
> real	0m3.308s
> user	0m2.851s
> sys	0m0.456s


Linux grep over the same file for the same pattern

> with -n option
> time grep -rn 'text' 'file > out.txt
> real	0m0.680s
> user	0m0.492s
> sys	0m0.188s


> without -n option
> real	0m0.431s
> user	0m0.223s
> sys	0m0.207s

Seems my Python grep utility is very slow when comparing linux grep.
Need to optimize

[Need to use Boyter-Moore fast string searching algorithm (used in linux grep) for improvement](http://www.cs.utexas.edu/users/moore/best-ideas/string-searching/)
