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

order = 0
print("Enter the dimension of the input matrix")
m = int(input("Row Matrix : "))
n = int(input("Column Matrix : "))

if m == n:
    print("The entered matrix is a balanced assignment problem\n")
    disp = "The entered matrix is : "
    order = m

else:
    print("The entered matrix is a unbalanced assignment problem\n")
    disp = "The entered matrix after balancing is : "

    if m > n:
        order = m

    else:
        order = n

array = [[0 for i in range(order)] for j in range(order)]
result_array = [[0 for i in range(order)] for j in range(order)]
xyz_array = [[0 for i in range(order)] for j in range(order)]

print("Enter the matrix\n")
for i in range (m):

    for j in range(n):
        k = int(input())
        array[i][j] = k
        xyz_array[i][j] = k

# array = [[10, 5, 9, 18, 11], [13, 9, 6, 12, 14], [3, 2, 4, 4, 5], [18, 9, 12, 17, 15], [11, 6, 14, 19, 10]]
# xyz_array = [[10, 5, 9, 18, 11], [13, 9, 6, 12, 14], [3, 2, 4, 4, 5], [18, 9, 12, 17, 15], [11, 6, 14, 19, 10]]


#  ----------------------------------------------------------- Display of Matrix ----------------------------------------------------------

print("\n"+disp+"\n")
for i in range(order):

    for j in range(order):
        print(array[i][j], end = "\t")
    print("\n")

rowredn_array = [[0 for i in range(order)] for j in range(order)]
new_array = [[0 for i in range(order)] for j in range(order)]

# ---------------------------------------------------------- Row & Column Reduction -----------------------------------------------------

def rowcolredn(array):

# -------------------------------------------------------------- Row Reduction -----------------------------------------------------------
    
    minr = []
    minc = []

    for i in range(order):
        m = array[i][0]

        for j in range(order):
            if array[i][j] <= m:
                m = array[i][j]

        minr.append(m)

    for i in range(order):

        for j in range(order):
            rowredn_array[i][j] = array[i][j] - minr[i]

# ------------------------------------------------------------- Column Reduction ----------------------------------------------------------

    for i in range(order):
        m = rowredn_array[0][i]

        for j in range(order):

            if rowredn_array[j][i] <= m:
                m = rowredn_array[j][i]

        minc.append(m)

    for i in range(order):

        for j in range(order):
            new_array[j][i] = rowredn_array[j][i] - minc[i]

    # print(minr)
    # print(minc)
    # print(rowredn_array)
    # print(new_array)

    print("\nThe matrix after Row and Column reduction : \n")
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
    
    i = 0
    while i < order:
        count = 0

        for j in range (order):
            if new_array[i][j] == 0:
                pos1 = i 
                pos2 = j
                count = count + 1

        i = i + 1            
        if count == 1:
            new_array[pos1][pos2] = 'x'
            for k in range (order):
                
                if new_array[k][pos2] in range(-9999, 9999):
                    new_array[k][pos2] = '|'
            i = 0

                
    print("\nMatrix after row scanning : \n")
    for i in range (order):

        for j in range (order):
            print(new_array[i][j], end = "\t")
        print("\n")

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

    i = 0
    while i < order:
        count = 0

        for j in range (order):
            if new_array[j][i] == 0:
                pos1 = i
                pos2 = j
                count = count + 1
        
        i = i + 1

        if count == 1:
            new_array[pos2][pos1] = 'x'

            for k in range (order):

                if new_array[pos2][k] in range(-9999, 9999):
                    new_array[pos2][k] = '-'

                elif new_array[pos2][k] == '|':
                    new_array[pos2][k] = '+'
            j = 0

    print("\nMatrix after column scanning : \n")
    for i in range (order):

        for j in range (order):
            print(new_array[i][j], end = "\t")
        print("\n")

# ----------------------------------------------- Detection of min undeleted value ------------------------------------------------------

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

    print("\nThe Optimized solution is : \n")
    print("\tJOB\t  |\tOPERATOR\t")
    for i in range (order):

        for j in range (order):
            if new_array[i][j] == 'x':
                co.append(xyz_array[i][j])
                op.append(j+1)
    
    for i in range (order):
        print("\t",i+1,"\t  |\t  ",op[i],"\t")
        cost = cost + co[i]
    print("\n")

    print( " The cost is : ", cost )



flag_check = True
while(flag_check):

# ---------------------------------------------------------- Function Calls ---------------------------------------------------------------
    
    rowcolredn(array)

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
