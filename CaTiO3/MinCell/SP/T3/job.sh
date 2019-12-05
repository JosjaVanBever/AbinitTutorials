#!/bin/bash

#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=1G

abinit < sp.files &> log

exit 0
