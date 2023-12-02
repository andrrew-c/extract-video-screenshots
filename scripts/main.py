import os
import re
import subprocess

# Folder
path = r'.'

# Get files
ofiles = os.listdir(path)
ofiles = os.listdir(path)

# Sort names
files = [re.sub(r'[\s-]', '_', file) for file in ofiles]

# Get durations
duration_command = "ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {file}"

a = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             ofiles[0]],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
                        
                    