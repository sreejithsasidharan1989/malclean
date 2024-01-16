#!/usr/bin/python3

import tempfile, shutil, argparse, sys, os

parser = argparse.ArgumentParser(prog=__file__, description='Pattern Saver', usage='%(prog)s -f Filename -b "BEGIN_PATTERN" -e "END_PATTERN"')
parser.add_argument('-b', action="store", dest='begin_pattern', required=True, help='Beginning pattern of the malware')
parser.add_argument('-e', action="store", dest='end_pattern', required=True, help='Ending pattern of the malware')
parser.add_argument('-f', action="store", required=True, dest='files')
parser.add_argument('--dry-run', action='store_true', required=False)
pattern = parser.parse_args()
files = pattern.files
modified_lines = []

def __dry_run(files, begin_pattern, end_pattern):
    temp = tempfile.NamedTemporaryFile(delete=True)
    shutil.copy2(files, temp.name)
    val1 = None
    val2 = None

    with open(temp.name, mode='r') as T:
        T.seek(0)
        lines = T.read().splitlines()
    for i, line in enumerate(lines):
        if not line.startswith(begin_pattern) and not lines[-1].strip().endswith(end_pattern):
            continue
        else:
            if begin_pattern in line:
                val1 = i
            elif end_pattern in line:
                val2 = i
            if val1 is not None and val2 is not None:
                del lines[val1:val2 + 1]
            with open(temp.name, 'w') as T:
                T.seek(0)
                T.writelines(lines)

    with open(temp.name, mode='r') as T:
        T.seek(0)
        lines = T.read().splitlines()
    for line in lines:
        if begin_pattern in line and end_pattern in line:
            val1 = line.index(begin_pattern)
            val2 = line.index(end_pattern)
            modified_line = line[:val1] + line[val2 + len(end_pattern):]
            modified_lines.append(modified_line.strip())
            i=i+1
        else:
            modified_lines.append(line.strip())
            i=i+1

        with open(temp.name, 'w') as T:
            T.writelines(modified_lines)
        
    with open(temp.name) as T:
        T.seek(0)
        print(T.read())
        
def __live_run(files, begin_pattern, end_pattern):
    
    with open(files, 'r') as f:
        lines = f.readlines()
    val1 = None
    val2 = None

    for i, line in enumerate(lines):
        if not line.startswith(begin_pattern) and not lines[-1].strip().endswith(end_pattern):
            continue
        else:
            if pattern.begin_pattern in line:
                val1 = i
            elif pattern.end_pattern in line:
                val2 = i
            if val1 is not None and val2 is not None:
                del lines[val1:val2 + 1]
            with open(files, 'w') as f:
                f.writelines(lines)
                f.close()

    with open(files, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if pattern.begin_pattern in line and pattern.end_pattern in line:
            val1 = line.index(begin_pattern)
            val2 = line.index(end_pattern)
            modified_line = line[:val1] + line[val2 + len(end_pattern):]
            modified_lines.append(modified_line.strip())
        else:
            modified_lines.append(line)
        with open(files, 'w') as f:
            f.writelines(modified_lines)
            f.close()

if pattern.dry_run:
    __dry_run(pattern.files, pattern.begin_pattern, pattern.end_pattern)
else:
    __live_run(pattern.files, pattern.begin_pattern, pattern.end_pattern)

modified_lines = None
