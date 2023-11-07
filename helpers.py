from datetime import datetime
import subprocess

def mcswitch():
    result = subprocess.run(["sh", "./mc.sh"], shell=True, capture_output=True, text=True)
    print(result.stdout)

def getVer():
    with open('CHANGELOG.md', 'r') as f:
        changes = f.readlines()
        vLine = changes[6]
        version = vLine[4:9]
        return version
    
def getLog():
    with open('CHANGELOG.md', 'r') as f:
        changelog = f.readlines()
        return changelog
    
def timestamp():
    cTime = datetime.now()
    print(f'{cTime}')
    print(f'----------')