# python_timing_experiments
Small code snippets to test the timing of different implementations
<br>
<br>
<br>
** Experiment 1 ** <br>
For the first experiment, I am trying to calculate the sum of the numbers in the range(10)
using different kinds of implementations. So at the end of every method, my goal is to put 
the list inside sum(list/generator) and let the sum handle it.
<br>
('For loop took ', 4.291534423828125e-05) <br>
('List comprehension took ', 2.09808349609375e-05)<br>
('List using generator took ', 2.288818359375e-05)<br>
('Generator directly inside sum took ', 1.3113021850585938e-05)<br>
So Generator directly inside the sum function is the fastest.

<br>
<br>
** Experiment 2 ** <br>
Timing experiment between if conditions in list comprehension vs lambda inside filter function<br>
They gave same results but list comprehension was almost 2x faster than filter function.<br>
Time taken by list comprehension: %s 1.7881393432617188e-05<br>
Time taken by filter: %s 3.3855438232421875e-05<br>




<br>
<br>
** Experiment 3 ** <br>
Timing experiment between list and set using them for looking up a value<br>
Lookup in the set is so much faster than lookup in the list .<br>
('list took: ', 5.0067901611328125e-06) <br>
('set took: ', 2.1457672119140625e-06) <br>

