def solution(id):
    import re
    res = re.sub('[^a-z\d_.\-]', '', id.lower())
    
    res = re.sub('\.+', '.', res)
    
    res = res.strip('.')
    
    if (res == ''): res = 'a'
    
    if (15 < len(res)): res = res[:15].rstrip('.')
    
    while (len(res) < 3): res += res[-1]
    
    return res
