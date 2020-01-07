def main_work_subdirs(gl):
    for root, dirs, files in os.walk('.'):
        dirs.sort()
        if root == gl['pwd']:
            for d2i in dirs:
                print(d2i)