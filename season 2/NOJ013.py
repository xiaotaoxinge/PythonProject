def convert(list):
    list_conv = []
    for i in range(len(list)):
        try:
            list_conv.append(int(list[i]))
        except ValueError:
            try:
                list_conv.append(float(list[i]))
            except ValueError:
                list_conv.append(list[i])
    return list_conv

def add(list):
    count = 0
    for i in range(len(list)):
        if isinstance(list[i],(int,float)):
            count += list[i]
        else:
            continue
    return count

if __name__ == '__main__':
    list = []
    list.extend(input().split())
    print(convert(list))
    print(add(convert(list)))