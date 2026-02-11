
from cfg import cfg


def create_label_list(train_list):
    classSet = set()
    with open(train_list) as f:
        next(f)
        for line in f:
            img_name, label = line.strip().split("\t")
            for e in label:
                classSet.add(e)
    # 在类的基础上加一个blank
    cfg["classify_num"] = len(classSet) + 1
    classList = sorted(list(classSet))
    # with open("/home/aistudio/data/label_list.txt", "w") as f:
    with open(cfg['label_list'], "w") as f:
        for idx, c in enumerate(classList):
            f.write("{}\t{}\n".format(c, idx))
            
    return classSet

classSet = create_label_list(cfg["train_list"])
print("classify num: ", len(classSet))

# classify num:  3096



