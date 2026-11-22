# HDD Synth sample packs
Hard disk drive recordings for use with the [HDD Synth](https://www.strifestreams.com/projects/hddsynth/).

These work with both the [hardware](https://github.com/MaverickUK/HDDSynth) and [software](https://github.com/MaverickUK/HDDSynth_Win32) versions of the device

## Contents
- [What is the HDD Synth?](#what-is-the-hdd-synth)
- [How to use](#how-to-use)
- [Previewing samples](#previewing-samples)
- [Creating new HDD Sample Packs](#creating-new-hdd-sample-packs)
- [CD-ROM drive packs](#cd-rom-drive-packs)
- [Sample packs](#sample-packs)

## What is the HDD Synth?
Primarily it's hardware based device that can be put into computers to simulate the sound of a mechanical hard drive.

More details about on the [project website](https://www.strifestreams.com/projects/hddsynth/)

## How to use
Simply copy the directory containing the samples you wish to use into the `samples` folders on the SD card used in the hardware based HDD Synth.

For example, to use the Western Digital Raptor pack, copy this directory from the repo:

```
samples/PB_WD_Raptor/
```

So it ends up on the SD card as:

```
SD card
└── samples/
    └── PB_WD_Raptor/
        ├── spinup.wav
        ├── idle.wav
        ├── access.wav
        └── spindown.wav
```

For the software based version, it's a case of copying the directory into the `samples` folder where ever you've installed the software

## Previewing samples
The sample packs live in the [`samples`](samples) directory. `preview.py` plays a sample pack as the HDD Synth would: spin up, idle looping three times then spin down. You just need Python3 installed to run the command.

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
- `access.wav`
- `spindown.wav`

Each WAV file must be:
- Mono
- 16bit
- Sample rate of 16, 22.05, 32, 44.1 or 48 kHz

> [!WARNING]
> All samples within a pack must use the same sample rate

You may call the HDD sample pack directory by any name of your choice, however it must not exceed 64 characters in length or contain any spaces (i.e.`IBM_type_2` is OK, `IBM type 2` is not)


## CD-ROM drive packs

With an [IDE Synth Bay](https://github.com/MaverickUK/HDDSynthPro) emulating a CD-ROM drive beside the hard disk, the HDD Synth can play the CD-ROM too (experimental: HDDSynth_Native's `cdrom-sounds` branch). A CD-ROM pack has a hard disk pack's files plus the tray:

- `spinup.wav`, `idle.wav`, `access.wav`, `spindown.wav`, and `sequential.wav`
- `tray_open.wav` and `tray_close.wav`
- `pack.json` (optional: `NAME`, `AUTHOR`, `GAIN`)

They live in [`cdrom`](cdrom), and go in a `cdrom` folder on the SD card, beside `samples` (not in it, or the pack button would play them as a hard disk):

```
SD card
├── samples/
│   └── PB_WD_Raptor/ ...
└── cdrom/
    └── CD_LG_GCC4320B/
        ├── spinup.wav
        ├── idle.wav
        ├── access.wav
        ├── sequential.wav
        ├── spindown.wav
        ├── tray_open.wav
        ├── tray_close.wav
        └── pack.json
```

A CD-ROM pack must have the same sample rate as the hard disk pack it plays beside (every pack here is 16 kHz). The IDE Synth Bay's `tools/cd_sounds` records them from a real drive.

### [LG GCC-4320B](cdrom/CD_LG_GCC4320B)
- A DVD-ROM/CD-RW combo drive (HL-DT-ST), recorded 21-22 Nov 2026 on a Samson Meteor microphone, the drive on a sponge.
- Access and sequential are the head alone, recorded with the disc stopped (at full speed the disc's rush hides it).
- Size: 1.4 MB, 16 kHz

## Sample packs

### [Mark (Original)](samples/Mark_Original)
- Created by: [Mark Angus](https://www.gladestock.co.uk/)
- Size: 434 KB

### [Mark (IBM)](samples/Mark_IBM)
- Created by: [Mark Angus](https://www.gladestock.co.uk/)
- Size: 573 KB

### [Mark (Toaster)](samples/Mark_Toaster)
- Created by: [Mark Angus](https://www.gladestock.co.uk/)
- Size: 568 KB

### [IBM Ultrastar IC35L018UWD210-0](samples/PB_IBM_Ultrastar)
- Created by: Peter Bridger, using recording by [MBC Computers](https://www.youtube.com/watch?v=2Q4jKxAKpmI)
- Size: 1,076 KB

### [MicroScience HH 612](samples/PB_MicroScience612)
- Created by: Peter Bridger, using recording by [MBC Computers](https://www.youtube.com/watch?v=YUmg1hMx5fM)
- Size: 1,555 KB

### [Quantum Fireball EX 3.2AT](samples/PB_QuantumFireballEX)
- Created by: Peter Bridger, using recording by [MBC Computers](https://www.youtube.com/watch?v=rnQ536oCb8w)
- Size: 788 KB

### [Quantum Fireball TM 1.2S SCSI](samples/PB_QuantumFireballTM)
- Created by: Peter Bridger, using recording by [MBC Computers](https://www.youtube.com/watch?v=otw775WdaP8)
- Size: 1,089 KB

### [Western Digital Caviar 2850](samples/PB_WD_Caviar2850)
- Created by: Peter Bridger, using recording by [MBC Computers](https://www.youtube.com/channel/UCPKbhl3GPYnZ2dQ9gn_NLCQ)
- Size: 818 KB

### [Western Digital WD Raptor WD360ADFD](samples/PB_WD_Raptor)
- Created by: Peter Bridger, using recording by [MBC Computers](https://www.youtube.com/watch?v=rGmpMltEUgQ)
- Size: 752 KB