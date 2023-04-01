from mpi4py import MPI
COMM = MPI.COMM_WORLD
nbOfproc = COMM.Get_size()
RANK = COMM.Get_rank()
tag=99
i=0
while i < nbOfproc-1:
   if RANK==i:
       sendb = 1000
       COMM.send ( sendb , dest=i+1, tag=tag )
   if RANK ==i+1:
       recvb = COMM.recv ( source=i , tag=tag )
       print ("Process {RANK} receive {recvb} from {RANKO}".format(RANK=RANK, recvb=recvb, RANKO=RANK-1))
   i=i+1 
