import random

def main():
    goodware = open("goodware_hashes.txt", "r")
    malware = open("malware_hashes.txt", "r")

    goodware_data = goodware.read()
    malware_data = malware.read()

    goodware_list = goodware_data.split("\n")
    goodware_list.pop(-1)
    goodware_list = [("goodware/" + u + ".png") for u in goodware_list]
    malware_list = malware_data.split("\n")
    malware_list.pop(-1)
    malware_list = [("malware/" + u + ".png") for u in malware_list]
    
    #malware_list = malware_list[:34]

    mega_list = goodware_list.copy()
    mega_list += malware_list

    for i in range(1, 11):
        random.shuffle(mega_list)
        train_index = int(len(mega_list) * 0.8)
        test_index = train_index + int(len(mega_list) * 0.1)
        valid_index = test_index

        train = open("data_splits/train" + str(i) + ".txt", 'w')
        for app in mega_list[:train_index]:
            train.writelines(app + "\n")
        train.close()

        test = open("data_splits/test" + str(i) + ".txt", 'w')
        for app in mega_list[train_index:test_index]:
            test.writelines(app + "\n")
        test.close()

        valid = open("data_splits/valid" + str(i) + ".txt", 'w')
        for app in mega_list[valid_index:]:
            valid.writelines(app + "\n")

        valid.close()

    print(int(len(goodware_list) * 0.8))
    print("malware: ")
    print(int(len(malware_list) * 0.8))

    goodware.close()
    malware.close()
    


if __name__ == "__main__":
    main()
