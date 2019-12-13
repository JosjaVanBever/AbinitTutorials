#!/bin/bash

#SBATCH --ntasks=3           # -n 
#SBATCH --mem-per-cpu=1G

#SBATCH --job-name=abinit    # -J
#SBATCH --cpus-per-task=1    # -c

# REMARK: these variables are overwritten when
#         specifying them as flags in input
# Other interesting variables:
#     --nodes -N : exclusive mode; use a whole node


# load appropriate modules
source /CECI/home/ucl/naps/jovbever/.bashrc N
source abimodule
# source /CECI/home/ucl/naps/jovbever/.local/bin/abimodule
# export PATH=/CECI/home/ucl/naps/jovbever/localHome/abinit/build/src/98_main/:$PATH
# export PATH=$CECIHOME/localHome/abinit/build/src/98_main/:$PATH

# print modules and environment for debugging
env
ml list

echo $PATH
echo `which abinit`

# abinit < "${INFILE}" &> log  # WORKS
# mpirun -n "${SLURM_JOB_CPUS_PER_NODE}" abinit < "${INFILE}" &> log  # FAILS
# mpirun -np "${SLURM_JOB_CPUS_PER_NODE}" abinit -inp "${INFILE}" &> log

# mpirun --bind-to none -n "${SLURM_JOB_CPUS_PER_NODE}" abinit < "${INFILE}" &> log
# mpirun --bind-to none abinit < "${INFILE}"
mpirun -n "${SLURM_NTASKS}" abinit < "${INFILE}" &> log

exit 0
