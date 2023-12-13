for repeat in range(10):

    alt = set()

    n = int(input())
    spinner = list(set(input().split()))
    for i in range(len(spinner)):
        spinner[i] = int(spinner[i])

    for i in range(len(spinner)):
        for j in range(i, len(spinner)):
            alt.add(spinner[i]*spinner[j])
            alt.add(spinner[i]+spinner[j])

    result = ''
    test = input().split()
    for i in range(5):
        test[i] = int(test[i])
        
        for j in range(len(spinner)):
            if (((test[i]-spinner[j]) in alt) or ((test[i]/spinner[j]) == (test[i]//spinner[j]) and ((test[i]//spinner[j]) in alt))):
                result += 'T'
                break
            
            if (j == len(spinner)-1):
                result += 'F'

    print(result)