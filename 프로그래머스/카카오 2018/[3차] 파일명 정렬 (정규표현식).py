import re
def solution(files):
    # [HEAD, NUMBER, TAIL]
    files = [ re.match('(\D+)(\d{1,5})([\d\D]*)', file).groups() for file in files ]
    files.sort( key=lambda x: [x[0].lower(), int(x[1])] )
    return [ ''.join(file) for file in files ]