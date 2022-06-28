def strip_comments(strng, markers):
    qwer = strng.split('\n')
    result = ''
    for i in qwer:
        for k in markers:
            if i.find(k)>=0:
                a=i.find(k)
                i = i[:a].rstrip()
        result +=i+'\n'
    return result[:-1]
