import sys

if len(sys.argv) != 2:
    print('Usage: python3 clayman.py <script>')
    print('  runs a batch in jobs/<script>.py')
    exit(0)

exec('from jobs.' + sys.argv[1] + ' import main')
main()