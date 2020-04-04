from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    print('process %s--data sending !' % comm.Get_rank(), flush=True)
    req = comm.isend(data, dest=1, tag=11)
elif rank == 1:
    req = comm.irecv(source=0, tag=11)
    data = req.wait()
    print('process %s--data received !' % comm.Get_rank(), flush=True)

else:
    pass

print('process %s--finished !' % comm.Get_rank(), flush=True)
