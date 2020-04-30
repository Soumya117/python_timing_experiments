# python_timing_experiments
Small code snippets to test the timing of different implementations

Results for the sum experiment are as follows: 
('For loop took %s', 4.291534423828125e-05)
('List comprehension took %s', 2.09808349609375e-05)
('List using generator took %s', 2.288818359375e-05)
('Generator directly inside sum took %s', 1.3113021850585938e-05)

So Generator directly inside the sum function is the fastest.
