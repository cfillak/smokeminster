# Smokeminster Script

The Smokeminster script is intended as a supplemental utility for use with
SmokeMonster's SMDB project: @SmokeMonsterPacks](https://github.com/SmokeMonsterPacks).
It is intended to reduce storage used by archivists maintaining multiple overlapping
legally dumped ROM sets.

Smokeminster takes an SMDB file, and subtracts the contents of one or more
No-Intro XML .dat files and/or other SMDB files and yields a flattened "Minimum"
SMDB file, with all resulting file references moved into one directory and hash
duplicates discarded.

For example, Smokeminster can be used to create a "minimum update pack" SMDB by
subtracting v6.0 from v7.0 of a particular pack.

Smokeminster does not touch your ROMs at all. It merely creates SMDBs for use
with the utilities included here: @SmokeMonsterPacks](https://github.com/SmokeMonsterPacks).

## Usage

**smokeminster.py** For making SMDBs (example command):
```DOS .bat
"parse_pack.py" -b "Base SMDB" -s "No-Intro .dat or SMDB .txt file(s)" -o "Output folder" -m "Minimum Dat"
```

`-b` (or `--base`) is the base SMDB to be subtracted from

`-s` (or `--sub`) is the No-Intro .dat and/or SMDB .txt file(s) to be subtracted from the base SMDB

`-o` (or `--out`) is the name of the output folder prepended to the files in the new minimized SMDB

`-m` (or `--min`) is the name of the resulting minimized SMDB file i.e. "SNES_MIN.txt"



[wiki](https://github.com/SmokeMonsterPacks/EverDrive-Packs-Lists-Database/wiki).


## Requirements

[python](https://www.python.org) 3.5 or newer

Linux, MacOS, or Windows


## Credits

Written by
[@cfillak](https://github.com/cfillak)

EverDrive Pack SMDB layouts by
[@SmokeMonsterPacks](https://github.com/SmokeMonsterPacks).

Some ideas and code structure borrowed from
[@frederic-mahe](https://github.com/frederic-mahe),
[@eatnumber1](https://github.com/eatnumber1)
[@coughlanio](https://github.com/coughlanio)
