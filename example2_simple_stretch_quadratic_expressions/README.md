This example builds from the previous one in two ways
1. There is timesteps  
2. We use quadratic basis for the displacement

To run, do (remember to change `ncores` for whatever number of cores you want to use)
```
mkdir -p out
mpirun -np ncores cheartsolver.out run.P
```

The python file `visualize_results.py` contains a template script that you can use to read the results in python and generating `.vtu` files to visualize it in Paraview.


### Try 
1. What happens if you increase or decrease the number of timesteps? 
2. What happens if you use a linear topology for the displacements instead of a quadratic?
3. Can you try more complicated expresions? 



### Running in bigblue
In bigblue you won't be able to visualize the results. So you will need to copy the results back to your local computer. You can do that using `rsync` in WSL.
1. Navigate to the folder the example1 folder in your computer (use `cd` to move to the folder)
2. Do (remember to change `username` and don't forget the `.` at the end)
```
rsync -r username@bigblue.engin.umich.edu:/home/username/cheart-examples/example1_simple_stretch/out . 
```
