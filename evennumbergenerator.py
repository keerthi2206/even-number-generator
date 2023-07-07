# printing even number using generator

def evennumber(start,end):
    for i in range(start,end):
        if i % 2 == 0:
            yield i
start = int(input('enter your starting number: '))
end = int(input('enter your ending number: '))
for res in evennumber(start,end):
    print(res)
