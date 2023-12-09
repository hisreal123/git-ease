#!/usr/bin/python3
import os
import subprocess

check_untracked_files = __import__('check_untracked_files').check_untracked_files


def fetch_repo():
    repo = input("Enter repository: ")
    return repo


def create_readme():
    readme = os.path.isfile('README.md')

    if not readme:
        with open('README.md', 'w') as read_file:
            read_file.write("My Git Repository\n\nWelcome to my Git repository!")
            print("\nGit repository initialized, and README.md created.")
    else:
        pass


def git_initializer():
    repo = fetch_repo()
    print("\n===============================\n"
          "Let\'s start with a new one !!! \n"
          "===============================")

    # # Set global default branch name to 'main'
    # subprocess.run(['git', 'config', '--global', 'init.defaultBranch', 'main'])

    print('\nInitializing a new Git repository...\n')
    subprocess.run(['git', 'init'])

    create_readme()

    try:
        first_commit_message = input('Enter the initial commit message: ')

        # subprocess.run(['git', 'add', '.'])

        check_untracked_files()

        subprocess.run(['git', 'commit', '-m', 'Initial commit'])

        branch_name = input('Enter the initial branch name (e.g., main, master): ')
        subprocess.run(['git', 'branch', '-M', branch_name])

        subprocess.run(['git', 'remote', 'add', 'origin', repo])

        # Set the upstream and push
        subprocess.run(['git', 'push', '-u', 'origin', branch_name])

        print("===============================\n"
              "You pushed to origin/{} on {}\n"
              "===============================".format(branch_name, repo))

    except EOFError:
        print("\n\n=============================== \n "
              "Exiting"
              "\n ===============================\n")

    except KeyboardInterrupt:
        print("\n\n=============================== \n "
              "Push process canceled \n "
              "===============================\n")
        git_initializer()

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        git_initializer()
