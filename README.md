# Scripts
* :file_folder: _**Doc Searcher**_

  A script that lists every file (even the ones inside folders and subfolders) starting at the script's location within the chosen type.

* :clipboard: _**Info PC Local**_

  A python script that uses powershell scripts to generate a txt file containing hardware information (Hostname, Windows Version, Memories, HDs, HDs type, Processor, Graphics Card) from the PC that executes it and saves on the local desktop. If the user's desktop folder is not in the C:\ path the script will create the folder.

* :receipt: _**List PCs**_

  Script that gets the hardware info (Hostname, Windows Version, Memories, HDs, HDs type, Processor, Graphics Card) from all computers connected to an _**AD**_ environment. It generates a txt file in the dekstop folder containing all the data.
  
  **IMPORTANT**
  
  It needs to be executed in the **AD Server** or it will not be able to connect to the AD computers and gather their specs.
