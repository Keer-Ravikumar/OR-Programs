# ------------------------------------------------------------- Formatting Tool ----------------------------------------------------------

class color:
    
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#  -------------------------------------------------------- User Input of the Question ---------------------------------------------------

print(color.BOLD+" -------------------------------------------- Hungarian Method --------------------------------------------- "+color.END)

flag = 1
while flag:
    print( "Choose the correct option: \n" )
    print( "1. Minimization \n2. Maximization" )
    choice = int(input( "Enter the option : " ))
    if choice != 1 and choice != 2:
        print( "Wrong Choice \n" )
        print( "Enter again" )

    else:
        print( "\n" )
        flag = 0


order = 0
print(color.UNDERLINE+"Enter the dimension of the input matrix"+color.END+" : \n")
m = int(input("Row Matrix : ")) 
n = int(input("Column Matrix : "))
print("\n")

if m == n:
    print(color.BOLD+"The entered matrix is a balanced assignment problem."+color.END+"\n")
    d = color.UNDERLINE+"The entered matrix"+color.END+" : "
    order = m

else:
    print(color.BOLD+"The entered matrix is a unbalanced assignment problem."+color.END+"\n")
    d = color.UNDERLINE+"The entered matrix after balancing"+color.END+" : "

    if m > n:
        order = m

    else:
        order = n

array = [[0 for i in range(order)] for j in range(order)]
result_array = [[0 for i in range(order)] for j in range(order)]
xyz_array = [[0 for i in range(order)] for j in range(order)]

print(color.UNDERLINE+"Enter the matrix"+color.END+" : \n")
for i in range (m):

    for j in range(n):
        k = int(input())
        array[i][j] = k
        xyz_array[i][j] = k

# array = [[10, 5, 9, 18, 11], [13, 9, 6, 12, 14], [3, 2, 4, 4, 5], [18, 9, 12, 17, 15], [11, 6, 14, 19, 10]]
# xyz_array = [[10, 5, 9, 18, 11], [13, 9, 6, 12, 14], [3, 2, 4, 4, 5], [18, 9, 12, 17, 15], [11, 6, 14, 19, 10]]


#  ----------------------------------------------------------- Display of Matrix ----------------------------------------------------------

print(color.RED+"\n"+d+"\n")
print(color.RED)
for i in range(order):

    for j in range(order):
        print(array[i][j], end = "\t")
    print("\n")
print(color.END)

rowred_array = [[0 for i in range(order)] for j in range(order)]
new_array = [[0 for i in range(order)] for j in range(order)]

# ---------------------------------------------------------- Row & Column Reduction -----------------------------------------------------

def row_col_red(array):

# -------------------------------------------------------------- Row Reduction -----------------------------------------------------------
    
    min_r = []
    min_c = []

    for i in range(order):
        m = array[i][0]

        for j in range(order):
            if array[i][j] <= m:
                m = array[i][j]

        min_r.append(m)

    for i in range(order):

        for j in range(order):
            rowred_array[i][j] = array[i][j] - min_r[i]

# ------------------------------------------------------------- Column Reduction ----------------------------------------------------------

    for i in range(order):
        m = rowred_array[0][i]

        for j in range(order):

            if rowred_array[j][i] <= m:
                m = rowred_array[j][i]

        min_c.append(m)

    for i in range(order):

        for j in range(order):
            new_array[j][i] = rowred_array[j][i] - min_c[i]

    # print(min_r)
    # print(min_c)
    # print(rowred_array)
    # print(new_array)

# ---------------------------------------------------------- Printing reduced Matrix ----------------------------------------------------------

    print(color.UNDERLINE+"\nThe matrix after Row and Column reduction"+color.END+" : \n")
    for i in range (order):

        for j in range (order):
            print(new_array[i][j], end = "\t")
        print("\n")

    for i in range (order):

        for j in range (order):
            result_array[i][j] = array[i][j]
            array[i][j] = new_array[i][j]

    # print(result_array)
    # print(array)

# ---------------------------------------------------------- Row Scan for Zeros ----------------------------------------------------------

def row_zero(new_array):
    
    count_array = []
    i = 0
    while i < order:
        count = 0

        for j in range (order):
            if new_array[i][j] == 0:
                pos1 = i 
                pos2 = j
                count = count + 1

        count_array.append(count)
        i = i + 1 

        if count == 1:
            new_array[pos1][pos2] = 'x'
            for k in range (order):
                
                if new_array[k][pos2] in range(-9999, 9999):
                    new_array[k][pos2] = '|'
            i = 0

        if len(count_array) == order:
            max = 0
            for a in range( len(count_array) ):
                if max >= count_array[a]:
                    max = count_array[a]
                    pos = a
                
# ----------------------------------------------------- Printing altered Matrix ----------------------------------------------------------

    print(color.UNDERLINE+"\nMatrix after row scanning"+color.END+" : \n")
    for i in range (order):

        for j in range (order):
                print(new_array[i][j], end = "\t")
        print("\n")
    # print(count_array)

    flag = 0
    i = 0
    j = 0

    for i in range (order):

        for j in range (order):
            if new_array[i][j] == 0:
                flag = 1
        
    return flag
            
# ------------------------------------------------------- Column Scan for Zeros ----------------------------------------------------------

def col_zero(new_array):

    count_array = []
    i = 0
    while i < order:
        count = 0

        for j in range (order):
            if new_array[j][i] == 0:
                pos1 = i
                pos2 = j
                count = count + 1
        
        count_array.append(count)
        i = i + 1

        if count == 1:
            new_array[pos2][pos1] = 'x'

            for k in range (order):

                if new_array[pos2][k] in range(-9999, 9999):
                    new_array[pos2][k] = '-'

                elif new_array[pos2][k] == '|':
                    new_array[pos2][k] = '+'
            j = 0

# ---------------------------------------------------- Printing altered Matrix ----------------------------------------------------------

    print(color.UNDERLINE+"\nMatrix after column scanning"+color.END+" : \n")
    for i in range (order):

        for j in range (order):
            print(new_array[i][j], end = "\t")
        print("\n")

    # print(count_array)

# ----------------------------------------------- Detection of min un-deleted value ------------------------------------------------------

def min_detect(new_array):

    minimum = 9999

    for i in range (order):

        for j in range (order):
            if new_array[i][j] in range(-9999,9999):
                if new_array[i][j] < minimum:
                    minimum = new_array[i][j]
                
    return minimum

# ---------------------------------------------- Addition and subtraction of minimum element --------------------------------------------

def add_subtract(new_array, m):
    global array
    for i in range (order):
        
        for j in range (order):

            if new_array[i][j] == '+':
                array[i][j] = array[i][j] + m

            elif new_array[i][j] in range(-9999,9999):
                array[i][j] = new_array[i][j] - m
    
    # print(array)

# ------------------------------------------------------- Finding optimal solution -------------------------------------------------------

def optimize(new_array):

    global xyz_array
    cost = 0
    op = []
    co = []

    print(color.GREEN)
    print("\n"+color.UNDERLINE+"The Optimized solution"+color.END+" : \n")
    print(color.GREEN)
    print("JOB\t  |\tOPERATOR\t")
    print(color.END)
    for i in range (order):

        for j in range (order):
            if new_array[i][j] == 'x':
                co.append(xyz_array[i][j])
                op.append(j+1)

    print(color.GREEN)
    for i in range (order):
        print(i+1,"\t  |\t  ",op[i],"\t")
        cost = cost + co[i]
    print("\n")

    print( " The cost is : ", cost )
    print(color.END)

# ------------------------------------------------------ maximization to minimization ---------------------------------------------------------------

def maximum(array):
    maxi = 0

    for i in range (order):

        for j in range (order):
            if array[i][j] >= maxi:
                maxi = array[i][j]
        
    for i in range (order):

        for j in range (order):
            array[i][j] = maxi - array[i][j] 

    # print(array)

# ---------------------------------------------- Checking if it is a maximization problem ---------------------------------------------------------------

if choice == 2:
    maximum(array)

# ---------------------------------------------------------- While loop ---------------------------------------------------------------

flag_check = True
while(flag_check):

# ---------------------------------------------------------- Function Calls ---------------------------------------------------------------

    row_col_red(array)

    flag = row_zero(new_array)
    if flag == 1:
        col_zero(new_array)

# ------------------------------------------------------ Number of cancelled 0 check -------------------------------------------------------
  
    cx = 0
    for i in range (order):

        for j in range (order):
            if new_array[i][j] == 'x':
                cx = cx + 1

# ----------------------------------------------------------- Function Calls ---------------------------------------------------------------

    if cx == order:

        optimize(new_array)
        flag_check = False

    else:

        m = min_detect(new_array)
        add_subtract(new_array, m)
