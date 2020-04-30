# python_timing_experiments
Small code snippets to test the timing of different implementations
<br>
<br>
<br>
Results for the sum experiment are as follows: 
<br>
('For loop took %s', 4.291534423828125e-05) <br>
('List comprehension took %s', 2.09808349609375e-05)<br>
('List using generator took %s', 2.288818359375e-05)<br>
('Generator directly inside sum took %s', 1.3113021850585938e-05)<br>
<br><br>
So Generator directly inside the sum function is the fastest.
