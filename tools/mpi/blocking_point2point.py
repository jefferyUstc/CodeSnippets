from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()


if rank == 0:
    data = {'a': 7, 'b': 3.14}
    print('process %s--data sending !' % comm.Get_rank(), flush=True)
    comm.send(data, dest=1, tag=11)
elif rank == 1:
    data = comm.recv(source=0, tag=11)
    print('process %s--data received !' % comm.Get_rank(), flush=True)
else:
    pass

print('finished process %s' % comm.Get_rank(), flush=True)
