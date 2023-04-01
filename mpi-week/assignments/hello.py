from mpi4py import MPI
COMM = MPI.COMM_WORLD
SIZE = COMM.Get_size()
RANK = COMM.Get_rank()

if RANK == 0:
   
   print("Hello from the rank {} process on {} total process".format(RANK,SIZE))
