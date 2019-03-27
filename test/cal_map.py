with open('coco_results_test.txt', 'r') as test_file:
    lines = test_file.readlines()
    sum_ap = 0.
    for line in lines[1:]:
        line = line.strip().split()
        print(line[-1])
        sum_ap += float(line[-1])
    assert len(lines)== 81, "classes number is 80"
    print(sum_ap/(len(lines)-1))
