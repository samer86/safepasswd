import subprocess
import sys


def run(cmd):
    p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
## But do not wait till netstat finish, start displaying Enter PRogram Nameoutput immediately ##
    while True:
        out = p.stderr.read()
        if out == '' and p.poll() != None:
            break
        if out != '' and isinstance(out, str):
            sys.stdout.write(out)
            sys.stdout.flush()
        else:
            sys.stdout.write(out.decode("utf-8"))
            break


def testRun(cmd):
    proc = subprocess.Popen(cmd,
                            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    return [stdout, stderr]


def copy2clip(txt):
    cmd = 'echo '+txt.strip()+'|xclip -selection  clipboard'
    return subprocess.check_call(cmd, shell=True)
