#!/usr/bin/python3
import subprocess
import os

push_command = __import__('push_command').push_command
initializer = __import__('initializer').git_initializer
had_commit = __import__('had_commit').had_commit


def get_interest():
    username = ""
    remote_output = subprocess.run(['git', 'remote', '-v', ], capture_output=True, text=True)
    if "origin" in remote_output.stdout:
        repo = remote_output.stdout.split("origin")[1].split()[0]
        repo_url = repo.split(':')[1]
        username = repo_url.split('/')[0]

    # Greeting to user !!
    print("Welcome!!!!, {}".format(username))
    print("\nDo you have a repo already ????")

    # try:
    #     choice = input("Enter 'Y/N': ")
    #
    #     if choice == "yes" or "y":
    #         push_command()
    #     elif choice == "N" or "n":
    #         initializer()
    #         pass
    #     else:
    #         exit()

    # except KeyboardInterrupt: print("\n\n=============================== \nOperation aborted by {}\n
    # ===============================\n". format(username))
    #
    # except Exception as e:
    #     print(f"An error occurred: {e}")


if __name__ == "__main__":
    if os.path.exists('.git'):
        print("This directory is already a Git repository.")
        had_commit()
    else:
        initializer()
