###begin
s=input()
s=s.strip()
if s[-1] in ['!','.','?']:
    p=s[-1]
    s=s.replace(p,'')
else:
    p=''
lst=s.split()
lst.reverse()
r=' '.join(lst)
print(r+p)



###end