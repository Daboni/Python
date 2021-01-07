# 하위 디렉터리 검색하기

import os

def search(dirname):
    try:
        filenames = os.listdir(name)
        for filename in filenames:
            full_name = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_name)
    except PermissionError:
        pass

