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

# do the actual calculation
mpirun -n "${SLURM_NTASKS}" abinit < "${INFILE}" &> log

exit 0
