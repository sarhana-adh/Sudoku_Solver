import math
import Tkinter
import time


grid =  [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    
root = Tkinter.Tk()
buttonArr=[]
root.title('Sudoku Solver')



def printOn(a):
    B = Tkinter.Text(root,height = 1, width = 3).grid(row=3,column=0,columnspan=9)
    A = Tkinter.Text(root,height = 1, width = 3).grid(row=7,column=0,columnspan=9)
    colored_btn = Tkinter.Text(root,height = 2, width = 1).grid(row=0,column=3)
    colored_btn = Tkinter.Text(root,height = 2, width = 1).grid(row=0,column=7)

    global buttonArr
    row=[]
    for i in range(9):
        row=[]
        for q in range(9):
            if (a[i][q]==0):
                row.append(Tkinter.Text(root,height = 2, width = 3,highlightbackground='#3E4149'))
                row[q].insert('1.0', " ")
              
            elif (grid[i][q]!=0):
                row.append(Tkinter.Text(root,height = 2, width = 3,highlightbackground='#3E4149'))
                row[q].insert('1.0', a[i][q])
                
        buttonArr.append(row)
    ro=0
    co=0
    for j in range(9):#row 
        for k in range(9):#column
          if k <3: 
            if j<3:     
              buttonArr[j][k].grid(row=j,column=k)
            elif j<6:
              buttonArr[j][k].grid(row=j+1,column=k)
            elif j<9:
              buttonArr[j][k].grid(row=j+2,column=k)
          
          elif k <6: 
            if j<3:     
              buttonArr[j][k].grid(row=j,column=k+1)
            elif j<6:
              buttonArr[j][k].grid(row=j+1,column=k+1)
            elif j<9:
              buttonArr[j][k].grid(row=j+2,column=k+1)
              

          elif k <9: 
            if j<3:     
              buttonArr[j][k].grid(row=j,column=k+2)
            elif j<6:
              buttonArr[j][k].grid(row=j+1,column=k+2)
            elif j<9:
              buttonArr[j][k].grid(row=j+2,column=k+2)
  
#this thing man
Dim=9

#print(buttonArr)

def printPuzzle(a):
  for row in range(Dim):
    for column in range(Dim):
      if((row+1)%3!=0):
        print(a[row][column], end=" ")
      else:
        print("\033[4m" + str(a[row][column]) + "\033[0m", end=" ")
      if((((column+1)%3)==0) ) : 
        print ("|", end="")
    print()



#find possibility of solutions try it.

def possible(a, row, col, n):
# check for the columns
  for i in range(Dim):
    if (a[row][i]==n): 
      return False
#check for the rows 
  for j in range(Dim):
    if (a[j][col]== n):
      return False

# find the start columns and rows of the box x and y belongs to 
  startRow= (int(row/3))*3
  startCol= (int(col/3))*3
#check for the boxes 
  for boxr in range(3):
    for boxc in range(3):
      if ((a[startRow+boxr][startCol+boxc])==n):
        return False

  return True #after testing everything 

def changeGrid(a):
  global buttonArr
  for i in range(9):
    for j in range(9):      
      buttonArr[i][j].delete('1.0', Tkinter.END)
      buttonArr[i][j].insert('1.0', a[i][j])

def ReadInput(grid):
  global  buttonArr
  for i in range(9):
    for q in range(9):
        value=buttonArr[i][q].get('1.0', Tkinter.END)
        if value!=' \n' and value!='\n':
          grid[i][q]=int(value)
        else:
          grid[i][q]=0
              
    


def solve(a,ro,co):
  if ((ro >= 8) & (co >=9)):
    return True  # check for the end of the solved 
  if (co== 9): 
        ro=ro+1
        co = 0

  if (a[ro][co] > 0):
        return solve(a, ro, co + 1)
 
  for i in range(1,10):
    if (possible(a, ro, co, i)):
          a[ro][co] = i;
          if (solve(a, ro, co + 1)):
              return True;    
    a[ro][co] = 0;
  return False 

def both(a):  
  print()
  ReadInput(a)
  printPuzzle(a)
  solve(a,0,0)
  print()
  printPuzzle(a)
  changeGrid(a)

  



printOn(grid)
#printPuzzle(grid)
# print the button for solving onto the 
Tkinter.Button(root, text = "Solve Puzzle",command = lambda:both(grid), highlightbackground='#00FF00',highlightthickness=30).grid(row=13,column=1,columnspan=9)
#printOn(grid)
root.mainloop()
  
        
