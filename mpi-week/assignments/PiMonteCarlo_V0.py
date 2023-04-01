
import random 
import timeit
from mpi4py import MPI

COMM = MPI.COMM_WORLD
nbOfproc = COMM.Get_size()
RANK = COMM.Get_rank()



random.seed(42)  

def compute_points(n):
    
    random.seed(42)  
    
    circle_points= 0

    # Total Random numbers generated= possible x 
    # values* possible y values 
    for i in range(n): 
      
        # Randomly generated x and y values from a 
        # uniform distribution 
        # Rannge of x and y values is -1 to 1 
                
        rand_x= random.uniform(-1, 1) 
        rand_y= random.uniform(-1, 1) 
      
        # Distance between (x, y) from the origin 
        origin_dist= rand_x**2 + rand_y**2
      
        # Checking if (x, y) lies inside the circle 
        if origin_dist<= 1: 
            circle_points+= 1
      
        # Estimating value of pi, 
        # pi= 4*(no. of points generated inside the  
        # circle)/ (no. of points generated inside the square) 
    
     
    
    return circle_points

INTERVAL= 1000
a= int((INTERVAL**2)/4)
start = timeit.default_timer()
circle_points = compute_points(a)
end = timeit.default_timer()
pi = 4* circle_points/ INTERVAL**2 
circle_point_reduced = COMM.reduce(circle_points, op=MPI.SUM, root=0)
pi_reduced = COMM.reduce(pi, op=MPI.SUM, root=0)
if RANK==0:
    print("Circle points number :",circle_point_reduced )
    print("Final Estimation of Pi=", pi_reduced, "cpu time :",end-start) 
