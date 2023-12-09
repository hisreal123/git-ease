#!/usr/bin/python3
import subprocess


def push_command():
    repo = ''
    remote_output = subprocess.run(['git', 'remote', '-v', ], capture_output=True, text=True)
    if "origin" in remote_output.stdout:
        repo = remote_output.stdout.split("origin")[1].split()[0]
    print(repo)

    subprocess.run(['git', 'add', '.'])
    print("All new files successfully added")

    # git commit
    try:
        commit_message = input('Enter commit message: ')

        if not commit_message:
            print('You have not entered a commit message!')
        else:
            subprocess.run(['git', 'commit', '-m', commit_message])
            print("Successfully committed: '{}'".format(commit_message))

            # git push with the personal access token
            subprocess.run(['git', 'push', 'origin', 'main'])
            print('Git push successful! to {} '.format(repo))

    except EOFError:
        print("\n\n=============================== \n Exiting \n ===============================\n")

    except KeyboardInterrupt:
        print("\n\n=============================== \n push process canceled \n ===============================\n")
        push_command()

    except Exception as e:
        print(f"An error occurred: {e}")
        push_command()
