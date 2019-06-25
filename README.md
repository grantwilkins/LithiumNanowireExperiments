# LithiumNanowireExperiments
Using the SIESTA coding language, the effects of lithium, beryllium, and sodium electrodes on lithium nanowire were observed via current and voltage graphs generated by TranSIESTA.

## What is this project?
Each file is really an experiment unto itself, where essentially a software called [SIESTA](https://departments.icmab.es/leem/siesta/) is used to compiled different results about atoms. Using the principles of computational quantum chemistry and molecular dynamics, these results are then able to be synthesized. 

In particular this project is looking into how wires the size of 10 atoms conduct electricity. The base wire used is a lithium nanowire two atoms long, and for consistency another wire with an amide group attachment to the lithium nanowire is used as well. The variation in the study are the electrodes, of which lithium, beryllium, and sodium are used. 

## Installation of SIESTA and TranSIESTA
SIESTA 4.0 was used and is compatible with Linux Ubuntu 16.04.
The [download link](https://launchpad.net/siesta/4.0) should allow the user to download the tar.gz file containing the source code.

Once acquired use gunzip to open the tar.gz file.
```bash
cd Downloads
gunzip siesta-4.0.2.tar.gz
```

At this point, the tar file can be moved to the home directory. If a bin folder does not exist, create one.

```bash
cd
mkdir bin
```
Once this is done, using the graphical file manager click on the tar file and extract the SIESTA folder to the home directory. 

Move into the new SIESTA file and create a directory called TObj. Obj and TObj will be where compilation of SIESTA and TranSIESTA will be made.

Copy gfortran.make into Obj and TObj and rename as arch.make for both files.

```bash
cd siesta-4.0.2
cd Obj
cp ../Src/Sys/gfortran.make ./
mv gfortran.make arch.make
```
After doing the same for TObj, using the shell command, inside of Obj you will compile the software.

```bash
sh  ../Src/obj_setup.sh
```
Once complete for Obj:
```bash
make
```
and for TObj:
```bash
make transiesta
```
Once complete, copy the siesta executable from Obj and the transiesta executable from TObj to the bin file.

## Installation of TBTrans
The final piece of software needed to run the source code is TBTrans. To install TBTrans, navigate to Util and into the TBTrans file. Here to compile a comment must be removed from the MakeFile, so using vim on the line TBTRANS_LINALG, remove the comment.
```bash
cd Util
cd TBTrans
make
```
Then move the tbtrans executable to the bin in the home directory.

## How to use Source Code
Each test can be run by using the siesta command on the RUN.fdf file in each folder.
```bash
siesta < RUN.fdf > run.out
transiesta < RUN.fdf > run.out
tbtrans < RUN.fdf > runTB.out
```
The three steps will produce a value for the current in the wire based on the discrete value set in the VOLTAGE.fdf file.
