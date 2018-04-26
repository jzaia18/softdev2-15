def meets_threshold(passwd):
    print "Testing if \"" + passwd + "\" meets the theshold..."
    l = [i for i in passwd if i.isalpha() and i==i.lower()]
    u = [i for i in passwd if i.isalpha() and i==i.upper()]
    n = [i for i in passwd if i.isdigit()]
    print bool(l and u and n) #for formatting
    return bool(l and u and n)

def get_strength(passwd):
    print "Getting strength of \"" + passwd + "\"..."
    a = min(sum([10 if not l.isalnum() else (7 if l.isdigit() else (3 if l==l.upper() else 1)) for l in passwd ]) / (len(passwd)/2), 10)
    print a
    return a

meets_threshold("password")
meets_threshold("PaSsWoRd")
meets_threshold("P@ssword")
meets_threshold("P4ssw0rd")

get_strength("hello")
get_strength("Hello")
get_strength("hello_world")
get_strength("Hello_World")
get_strength("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
get_strength("}{!@&Y*(*IO#@KJLQWHEU(@OQI#LK))}")
