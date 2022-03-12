def get_cv_list(rep):
    counter = 0
    for vector in product([1, -1], repeat=rep):
        # print(roll)
        cv_list.append(list(vector))
        counter = counter + 1
    print("There are {} number of colour vectors in the cv_list".format(counter))

    return cv_list