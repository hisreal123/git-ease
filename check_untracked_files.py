import os
import subprocess


def check_untracked_files():
    try:
        status_output = subprocess.run(['git', 'status'], capture_output=True, text=True)

        if "Untracked files:" in status_output.stdout:
            print("Untracked files found. Please add and commit them.")
            print(status_output.stdout)

            # Add all untracked files
            # subprocess.run(['git', 'add', '--', ':/', '*.py', '__pycache__/'])
            subprocess.run(['git', 'add', '.'])
        else:
            subprocess.run(['git', 'add', '.'])
    except subprocess.CalledProcessError as e:
        print("An error occurred: {}".format(e))


if __name__ == "__main__":
    check_untracked_files()
