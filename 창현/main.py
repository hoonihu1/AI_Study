step_size = 0.01
w_0, w_1, w_2 = 1, 1, 1
for it in range(100000):
    tmp_0 = w_0 - step_size*(12 * w_2 + 8 * w_1 + 8  * w_0 - 8)
    tmp_1 = w_1 - step_size*(20 * w_2 + 12 * w_1 + 8 * w_0 - 10)
    tmp_2 = w_2 - step_size*(36 * w_2 + 20 * w_1 + 12 * w_0 - 14)
    w_0, w_1, w_2 = tmp_0, tmp_1, tmp_2
    if it == 4999 or it == 9999 or it == 99999 :
        print(it+1,"회")
        print("    w_0= ",w_0)
        print("    w_1= ",w_1)
        print("    w_2= ",w_2)