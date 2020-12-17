x="a2b3"
output=""
for ch in x:
    if ch.isalpha():
        output=output+ch
        preceed=ch
    else:
        output=output+preceed*(int(ch)-1)
print(output)
