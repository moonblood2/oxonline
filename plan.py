import pickle;

def load(id):
    with open("table_"+str(id)+".pickle", "rb") as f:
        table = pickle.load(f);
    return table;

def save(id, table):
    with open("table_"+str(id)+".pickle", "wb") as f:
        pickle.dump(table, f);

def table(id):
    TABLE = load(id);
    return TABLE;

def set(id, s, x, y):
    TABLE = load(id);
    if (s == "o" or s == "x") and TABLE[x][y] == "":
        TABLE[x][y] = s;
        save(id, TABLE);
        return TABLE;
    else:
        return False;

def reset(id):
    TABLE = [["" for i in range(3)] for j in range(3)];
    save(id, TABLE);

def checkWin(id):
    TABLE = load(id);

    p0 = [
    [1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]];

    p1 = [
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]];

    p2 = [
    [0, 0, 0],
    [0, 0, 0],
    [1, 1, 1]];

    p3 = [
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]];

    p4 = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0]];

    p5 = [
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 1]];

    p6 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]];

    p7 = [
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]];

    pattern = [p0, p1, p2, p3, p4, p5, p6, p7];

    for p in pattern:
        o_t = [[99 for i in range(3)] for j in range(3)];
        x_t = [[99 for i in range(3)] for j in range(3)];
        for i in range(3):
            for j in range(3):
                if TABLE[i][j] == "":
                    o_t[i][j] = 0;
                    x_t[i][j] = 0;
                if TABLE[i][j] == "o":
                    result = TABLE[i][j]*p[i][j];
                    if result == "":
                        o_t[i][j] = 0;
                    if result == "o":
                        o_t[i][j] = 1;
                    x_t[i][j] = 0;
                if TABLE[i][j] == "x":
                    result = TABLE[i][j]*p[i][j];
                    if result == "":
                        x_t[i][j] = 0;
                    if result == "x":
                        x_t[i][j] = 1;
                    o_t[i][j] = 0;
        if o_t in pattern:
            return [True, "o"];
        if x_t in pattern:
            return [True, "x"];
    return [False, ""];

def print_table(id):
    TABLE = load(id);
    for r in TABLE:
        print(r);

if __name__ == "__main__":
    import random;
    id = 0;
    turn_l = ["x","o"];
    turn_num = 0;
    reset(id);
    
    for i in range(9):
        print "turn: ", turn_num+1;

        turn = turn_l[turn_num%2];
        turn_num += 1;

        while(not set(id, turn, random.randint(0,2), random.randint(0,2))):
            pass;

        print_table(id);

        if checkWin(id)[0]:
            break;

        if i==8:
            print("Draw!");

    if turn_num <9:
        print checkWin(id)[1], " WON!";
