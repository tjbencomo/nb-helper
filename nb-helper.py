import datetime as dt
import os

SETTING_KEYS = ['save_dir', 'name']

def read_config(fp):
    settings = {}
    if not os.path.exists(fp):
        raise ValueError("config.txt does not exist! Create config.txt in the same directory as this script")
    with open(fp, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('#'):
                continue
            s = line.rstrip().split('=')
            settings[s[0]] = s[1]
    for key in SETTING_KEYS:
        if key not in settings:
            raise ValueError(f"Missing setting {key}")
    return settings

def new_entry(settings, date=None):
    if date is None:
        date = dt.datetime.now()
    fulldate = date.strftime('%A %B %d, %Y')
    fn = str(date).split(' ')[0] + '.md'
    fp = os.path.join(settings['save_dir'], fn)
    if os.path.exists(fp):
        raise ValueError(f"Notebook entry for {fulldate} already exists in your specified save directory!")
    with open(os.path.join(settings['save_dir'], fn), 'w') as f:
        f.write("# Lab Journal\n")
        f.write(f"**Author:** {settings['name']}\n\n")
        f.write(f"**Date:** {fulldate}\n\n")
        f.write("## Summary\n")
    return fn

def main():
    program_dir = os.path.dirname(os.path.realpath(__file__))
    fp = os.path.join(program_dir, 'config.txt')
    d = read_config(fp)
    entry_fn = new_entry(d)
    print(f"New notebook entry created as {entry_fn}!")

if __name__ == '__main__':
    main()
