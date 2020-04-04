from mpi4py import MPI

print('hello world! --- %s' % MPI.COMM_WORLD.Get_rank())
