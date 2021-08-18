import pandas as pd
import numpy as np
import operator


def prob( data, attribute):

    prob = {}
    df_split = data.groupby(attribute)

    for i,j in df_split:
        prob[i] = len(j) / len(data)

    #print(prob)

    return prob

if __name__ == '__main__':


    a = []

    a.append(['low', 'low', 'yes'])
    a.append(['low', 'high', 'no'])
    a.append(['high', 'low', 'no'])
    a.append(['high', 'high', 'no'])

    a = pd.DataFrame( a , columns= ['X', 'Y', 'Decision'])



    attributes = a.columns
    attributes = list(attributes)
    target_attribute = 'Decision'
    attributes.remove(target_attribute)

    """
      **********************   training ****************
    """

    p = prob(a, target_attribute)

    q = []

    attribute_value = []

    for i in range(0, len(attributes)):
        r = a[attributes[i]]
        r = list(r)
        r = np.array(r)
        attribute_value.append(list(np.unique(r) ) )

    #print(attribute_value)
    target_attribute_value = []

    target_attribute_value = a[target_attribute]

    target_attribute_value = list(target_attribute_value)
    target_attribute_value = np.array(target_attribute_value)
    target_attribute_value = np.unique(target_attribute_value)
    target_attribute_value = list(target_attribute_value)

    #print("Target attribute value ",target_attribute_value)

    df_split = a.groupby(target_attribute)

    arr1 = [] # target_value, [ prob_of_x_dic], [pro_of_y_dic ]
    arr1_subarray = []

    k = 0.5

    for i,j in df_split:
        #print(i)
        s = []
        dic = {}
        arr1_subarray = []
        for l in range(0, len(attributes)):
            s = list(j[attributes[l]])
            dic = {}
            for m in range(0, len(attribute_value[l])):
                dic[attribute_value[l][m]] = ( s.count(attribute_value[l][m])  + k ) / ( len(j) + k * 2  )

            arr1_subarray.append(dic)
        arr1.append([i , arr1_subarray])


    print("Enter X ")
    x1 = input()

    print("Enter Y ")
    x2 = input()

    X = []
    X.append(x1)
    X.append(x2)
    Y = 'high'
    """
    ************************** prediction ************************
    """
    result  = {}
    m = 1
    for i in range(0, len(target_attribute_value)):
        m = 1
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





