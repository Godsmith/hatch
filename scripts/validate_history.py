import re
import sys
from pathlib import Path

HEADER_PATTERN = (
    r'^\[([a-z0-9.]+)\]\(https://github\.com/ofek/hatch/releases/tag/({package}-v\1)\)'
    r' - [0-9]{{4}}-[0-9]{{2}}-[0-9]{{2}} ### \{{: #\2 \}}$'
)


def main():
    project_root = Path(__file__).resolve().parent.parent
    history_file = project_root / 'docs' / 'history.md'

    current_pattern = ''
    with history_file.open('r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            elif line.startswith('## '):
                _, _, package = line.partition(' ')
                # Remove any emphasis
                package = package.strip('*_')
                current_pattern = HEADER_PATTERN.format(package=package.lower())
            elif line.startswith('### '):
                _, _, header = line.partition(' ')
                if header.strip('*_') == 'Unreleased':
                    continue
                elif not re.search(current_pattern, header):
                    print('Invalid header:')
                    print(header)
                    sys.exit(1)


if __name__ == '__main__':
    main()
