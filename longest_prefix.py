def prefix(str):
    if not str:
        return ""
    pref_str = ""
    for a, b in zip(str[0],str[-1]):
        if a == b:
            pref_str += a
        else:    
            break
    return pref_str

print(prefix(["flower","float","flight"]))    