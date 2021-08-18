
def Classify(X1, X2):
    import Naive_bayes_AND
    import Naive_bayes_NOR
    import Naive_bayes_NAND
    import operator

    print("Training!!!!!!!!-------------------------------------------------------------------------------------------------------------------------------")

    #q = Naive_bayes_AND.training()
    q = Naive_bayes_NAND.training()
    #q = Naive_bayes_NOR.training()

    p = q[0]
    arr1 = q[1]
    attributes = q[2]
    target_attribute_value = q[3]

    print(p)
    print(arr1)
    print("Training Finished--------------------------------------------------------------------------------------------------------------------------------")

    print(attributes)
    print(target_attribute_value)

    #print("Enter X ")
    #print(X1)
    print("Testing!!!----------------------------------------")
    X1 = str(X1)
    X1 = X1.rstrip("\n")

    x1 = X1

    #x1 = input()

    #print("Enter Y ")
    #print(X2)
    X2 = str(X2)
    X2 = X2.rstrip("\n")

    x2 = X2
    #x2 = input()

    X = []
    X.append(x1)
    X.append(x2)

    result  = {}
    m = 1
    for i in range(0, len(target_attribute_value)):
        m = 1
        i = int(i)
        m = m * p[target_attribute_value[i]]



        for j in range(0, len(arr1)):
            if arr1[j][0] == target_attribute_value[i]:
                temp = arr1[j][1]

                for k in range(0, len(attributes)):
                    m = temp[k][X[k]] * m
                    result[target_attribute_value[i]] = m

    dic2 = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
    print("Input \n", X)
    print("output")
    print(dic2[0][0])

    print(dic2)

    return dic2[0][0]





