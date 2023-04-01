from mpi4py import MPI
COMM = MPI.COMM_WORLD
nbOfproc = COMM.Get_size()
RANK = COMM.Get_rank()

if RANK==0:
    sendb=int(input("Entrez un nombre: "))
else:
    sendb = None
        
recvb= COMM.bcast(sendb , root=0)
print("Process {RANK} got {data}".format(RANK=RANK, data=recvb))
