#!/bin/bash

#SBATCH --ntasks=1           # -n 
#SBATCH --mem-per-cpu=1G
#SBATCH --nodes=1            # -N

#SBATCH --job-name=abinit    # -J
#SBATCH --cpus-per-task=3    # -c

# REMARK: these variables are overwritten when
#         specifying them as flags in input

# load appropriate modules
source abimodule

ml list

# module load openmpi/1.5.3/intel-12.0.0.084

# abinit < "${INFILE}" &> log  # WORKS
# mpirun -n "${SLURM_JOB_CPUS_PER_NODE}" abinit < "${INFILE}" &> log  # FAILS
# mpirun -np "${SLURM_JOB_CPUS_PER_NODE}" abinit -inp "${INFILE}" &> log
mpirun --bind-to none -n "${SLURM_JOB_CPUS_PER_NODE}" abinit < "${INFILE}" &> log

exit 0
