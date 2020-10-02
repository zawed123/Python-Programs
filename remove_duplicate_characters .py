# https://www.facebook.com/zawed.akhtar.7923/posts/965501223932927
# Subscribed by MySirG.com

def fix(string):
    s = set()
    list = []
    for ch in string:
        if ch not in s:
            s.add(ch)
            list.append(ch)

    return ''.join(list)        

string=input("Enter string:")
print(fix(string))
