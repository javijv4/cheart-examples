This file runs a simple problem where a cube gets stretched using dirichlet conditions. 

To run, do (remember to change `ncores` for whatever number of cores you want to use)
```
mkdir -p out
mpirun -np ncores cheartsolver.out run.P
```

The python file `visualize_results.py` contains a template script that you can use to read the results in python

### Try 
What happens if you increase the stretching value defined in `line 64`? Or if you make it negative?

### Running in bigblue
In bigblue you won't be able to visualize the results. So you will need to copy the results back to your local computer. You can do that using `rsync` in WSL.
1. Navigate to the folder the example1 folder in your computer (use `cd` to move to the folder)
2. Do (remember to change `username` and don't forget the `.` at the end)
```
rsync -r username@bigblue.engin.umich.edu:/home/username/cheart-examples/example1_simple_stretch/out . 
```
