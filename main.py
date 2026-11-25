import os
import shutil


# This runner keeps it simple on purpose: the farewell line is already
# written in entry.txt, so all this script does is carry that finished
# line, unchanged, into the folder the grader looks at. Nothing is
# rewritten or reformatted along the way — the AI's last words arrive
# exactly as they were written.
def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile("entry.txt", os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
