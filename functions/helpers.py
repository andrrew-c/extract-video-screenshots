import argparse
import os
import re
from math import floor
import subprocess

def get_command_line_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input',
                        required=True,
                        dest = 'path'
                        )

    parser.add_argument('-n', '--num-images',
                        type=int,
                        default = 4
                        )
    args = parser.parse_args()
    return args


    
def get_duration(filename, path) -> float:

    # Run ffprobe to get video duration in seconds
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", os.path.join(path, filename)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    
    return float(result.stdout)
                        

def get_frame_interval(duration, num_images) -> int:

    return floor(duration/num_images)

def get_images_from_video(filename, file_folder, frame_interval):

    # Get tidy output name
    out_file_name = re.sub(r'[\s-]', '_', filename)

    # Full path of file
    file_path = os.path.join(file_folder, filename)

    # Define the command we will run
    command = ["ffmpeg",
            "-i",
                file_path,
                "-vf",
                f"fps=1/{frame_interval}",
                f'{out_file_name}_%04d.png'
                ]
    #print(f"Processing command: '{command}'")
    # Run the command
    subprocess.run(command,
                   stdout=subprocess.PIPE,
                   stderr=subprocess.STDOUT
                   )

def process_single_video(filename, path, num_images):
    
    # Get duration of video
    duration = get_duration(filename, path)

    # Interval for frames for video to process
    frame_interval = get_frame_interval(duration, num_images)

    print(f"Processing video '{filename}' with duration {duration} seconds")
    get_images_from_video(filename, path, frame_interval)

def process_folder(path, num_images):

    all_files = os.listdir(path)

    for file in all_files:
        process_single_video(file, path, num_images)

