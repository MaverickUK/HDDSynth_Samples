# HDD Synth samples packs
Hard disk drive recordings for use with the [HDD Synth](https://www.strifestreams.com/projects/hddsynth/).

Both the [hardware](https://github.com/MaverickUK/HDDSynth) and [software](https://github.com/MaverickUK/HDDSynth_Win32) versions of the device

## Contents
- [What is the HDD Synth?](#what-is-the-hdd-synth)
- [How to use](#how-to-use)
- [Previewing samples](#previewing-samples)
- [Creating new HDD Sample Packs](#creating-new-hdd-sample-packs)
- [Sample packs](#sample-packs)

## What is the HDD Synth?
Primarily it's hardware based device that can be put into computers to simulate the sound of a mechanical hard drive.

[More details about on the project website]((https://www.strifestreams.com/projects/hddsynth/))

## How to use
Simply copy the directory containing the samples you wish to use into the `samples` folders on the SD card used in the hardware based HDD Synth.

For the software based version, it's a case of copying the directory into the `samples` folder where ever you've installed the software

## Previewing samples
`preview.py` plays a sample pack as the HDD Synth would: spin up, idle looping three times then spin down. You just need Python3 installed to run the command.

```
# Play single pack
python3 preview.py PB_WD_Raptor

# Play all packs
python3 preview.py 

# Save pack demo to disk
python3 preview.py PB_WD_Raptor --save out.wav
```

## Creating new HDD Sample Packs
The HDD Synth is designed to be easily extendable and allows you to create your own HDD sample packs. Each HDD sample pack is made up a directory on the SD card which then contains the following WAV files:

- `spinup.wav`
- `idle.wav`
- `Access.wav`
- `spinodown.wav`

Each WAV file must be:
- Mono
- 16Khz
- 16bit

The combined size of all the samples must not exceed 2MB (Max 1MB for the HDD Synth v5.3.0 Beta Edition)

You may call the HDD sample pack directory by any name of your choice, however it must not exceed 64 characters in length or contain any spaces (i.e. IBM_type_2.wav is OK, IBM type 2.wav is not)


## Sample packs

### [Mark (Original)](Mark_Original)
- Created by: [Mark Angus](https://www.gladestock.co.uk/)
- Size: 434 KB

### [Mark (IBM)](Mark_IBM)
- Created by: [Mark Angus](https://www.gladestock.co.uk/)
- Size: 573 KB

### [Mark (Toaster)](Mark_Toaster)
- Created by: [Mark Angus](https://www.gladestock.co.uk/)
- Size: 568 KB

### [IBM Ultrastar IC35L018UWD210-0](/PB_IBM_Ultrastar)
- Created by: Peter Bridger, using recording by [MBC Computers](https://www.youtube.com/watch?v=2Q4jKxAKpmI)
- Size: 1,076 KB

### [MicroScience HH 612](/PB_MicroScience612)
- Created by: Peter Bridger, using recording by [MBC Computers](https://www.youtube.com/watch?v=YUmg1hMx5fM)
- Size: 1,555 KB

### [Quantum Fireball EX 3.2AT](/PB_QuantumFireballEX)
- Created by: Peter Bridger, using recording by [MBC Computers](https://www.youtube.com/watch?v=rnQ536oCb8w)
- Size: 788 KB

### [Quantum Fireball TM 1.2S SCSI](/PB_QuantumFireballTM)
- Created by: Peter Bridger, using recording by [MBC Computers](https://www.youtube.com/watch?v=otw775WdaP8)
- Size: 1,090 KB

### [Western Digital Caviar 2850](/PB_WD_Caviar2850)
- Created by: Peter Bridger, using recording by [MBC Computers](https://www.youtube.com/channel/UCPKbhl3GPYnZ2dQ9gn_NLCQ)
- Size: 819 KB

### [Western Digital WD Raptor WD360ADFD](/PB_WD_Raptor)
- Created by: Peter Bridger, using recording by [MBC Computers](https://www.youtube.com/watch?v=rGmpMltEUgQ)
- Size: 753 KB