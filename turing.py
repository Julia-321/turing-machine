NMAX = 1000050
rules = {}


def input_rules(filename = None):
    if filename:
       import sys
       real_stdin = sys.stdin
       sys.stdin = open(filename, 'r')
    print("""Input rules (one in a row):
state symbol write new_state move(L/R/N)
Input 'done' when finished""")
    while True:
        s = input()
        if s.strip(" '") == 'done':
            break
        state, val, write, new_state, move = s.split(' ')
        if (state, val) in rules:
            ans = input("You already have rule {} {}: {} {} {}. Do you want to replace it? (y/n)".format(state, val, *rules[(state, val)]))
            if ans == 'n':
                continue
        rules[(state, val)] = (write, new_state, move)
    global start_state
    global term_state
    global blank
    blank = input("Blank symbol: ")
    start_state = input("Start state: ")
    term_state = input("Terminate state: ")
    if filename:
        sys.stdin = real_stdin
    
    


def input_combination():
    global tape
    global position
    tape = input("Input space separated combination ({} for blank):\n".format(blank)).split(' ')
    position = int(input("Start position: "))
    tape = NMAX*[blank]+tape+NMAX*[blank]
    position += NMAX

    

def execute(do_log = False):
    state = start_state
    global position
    while state != term_state:
        if do_log:
            print((5*"{:^5}|")[:-1].format(*tape[position-2:position+3]))
            print("{:^30}".format('^'*5))
            print("{:^30}".format(state))
        if (state, tape[position]) not in rules:
            print("Error! No rule for state {} symbol {}".format(state, tape[position]))
            exit()
        else:
            write, new_state, move = rules[(state, tape[position])]

        tape[position] = write
        state = new_state
        position += 1 if move == 'R' else -1 if move == 'L' else 0

    if do_log:
        print((5*"{:^5}|")[:-1].format(*tape[position-2:position+3]))
        print("{:^30}".format('^'*5))
        print("{:^30}".format(state))

def input_unary():
    a, b  = map(int, input("Input 2 numbers (1..1000): ").split(' '))
    global tape
    global position
    tape = list('1'*a+'0'+'1'*b)
    position = 0
    tape = NMAX*[blank]+tape+NMAX*[blank]
    position += NMAX

def count():
    cnt = 0
    global position
    position -= 1
    while tape[position] == '1':
        cnt += 1
        position -= 1
    return cnt

                  
input_rules('mult_test.txt')
input_combination()
#input_unary()
execute()
#print(count())
if (NMAX < 100):
    print(tape)
else:
    f = open('result.txt', 'w');
    f.write(str(tape))
    print('OK')


