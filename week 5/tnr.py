from mpi4py import MPI
comm=MPI.COMM_WORLD
rank=comm.rank
if rank ==0:
	a=[]
	a.append(comm.recv(source=1))
	a.append(comm.recv(source=2))
if rank ==1:
	comm.send([1,2,3,4,5],dest=0)
if rank ==2:
	comm.send([6,7,8,9],dest=0)
