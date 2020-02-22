import os
import subprocess
import glob

col_dir = "/col_dir"
post_dir = "/_posts"

def rm_sub_file(dirname):
    files = glob.glob(dirname + "/*")
    for file in files:
        os.remove(file)

def get_current_path():
    output = subprocess.check_output("pwd", shell=True)
    return output[0:len(output)-1]

def copy_file(target, dst):
    if not subprocess.call(["cp", target, dst]):
        print(target + " finished")

def get_sub_file(dirname, is_dir):
    filenames = os.listdir(dirname)
    sub_file = []
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        if not filename.startswith('.') and os.path.isdir(full_filename) == is_dir:
            sub_file.append(full_filename)
    return sub_file

if __name__ == "__main__":
    cur_path = get_current_path()
    col_path = cur_path + col_dir 
    post_path = col_path + post_dir

    rm_sub_file(post_path)

    col_sub_dirs = get_sub_file(col_path, True)

    for dir in col_sub_dirs:
        if dir == post_path:
            continue
        file_lists = get_sub_file(dir, False)
        for file in file_lists:
            copy_file(file, post_path)


