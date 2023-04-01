from mpi4py import MPI

COLS = 8
ROWS = 8

comm = MPI.COMM_WORLD
p = comm.Get_size()
rank = comm.Get_rank()

a = None

NPROWS = 2
NPCOLS = 2
BLOCKROWS = ROWS // NPROWS
BLOCKCOLS = COLS // NPCOLS

if rank == 0:
    a = bytearray(range(ROWS*COLS))

if p != NPROWS*NPCOLS:
    if rank == 0:
        print(f"Error: number of PEs {p} != {NPROWS} x {NPCOLS}")
    comm.Abort()

b = bytearray(BLOCKROWS * BLOCKCOLS)

blocktype2 = MPI.CHAR.Create_vector(BLOCKROWS, BLOCKCOLS, COLS)
blocktype2.Commit()

blocktype = blocktype2.Create_resized(0, 1)
blocktype.Commit()

disps = [i * COLS * BLOCKROWS + j * BLOCKCOLS for i in range(NPROWS) for j in range(NPCOLS)]
counts = [1] * (NPROWS * NPCOLS)

comm.Scatterv([a, counts, disps, blocktype], b)

for proc in range(p):
    if proc == rank:
        print(f"Rank = {rank}")
        if rank == 0:
            print("Global matrix:")
            for i in range(ROWS):
                for j in range(COLS):
                    print(f"{a[i*COLS+j]:3d}", end=" ")
                print("")
        print("Local Matrix:")
        for i in range(BLOCKROWS):
            for j in range(BLOCKCOLS):
                print(f"{b[i*BLOCKCOLS+j]:3d}", end=" ")
            print("")
        print("")

    comm.Barrier()

blocktype2.Free()
blocktype.Free()

MPI.Finalize()
