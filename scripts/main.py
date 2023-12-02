
from functions.helpers import (
    get_command_line_args,
    process_folder,
)

if __name__ == "__main__":

    args = get_command_line_args()

    process_folder(args.path, args.num_images)
