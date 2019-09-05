<img src="descarga.png"/>
<h1 align="center" style="color:red;"> Dynamic System Program</h1>

<h5 align="left" Style="color:orange;">DYNAMIC SYSTEM</h5>
            DYNAMIC SYSTEMS.- A dynamic system is a system or process in which motion occurs, or includes active forces, as opposed to static conditions with no motion.
            Dynamic systems by their very nature are constantly moving or must change states to be useful.

<h5 align="left" Style="color:orange;">WHAT TO DO:</h5>

            -to execute the program write in the console- python plot.py 
            
            
            wait for more.....

<h5 align="left" Style="color:orange;">METHODOLOGY</h5>
            "ReadEquation".- it's a function used to read an equation of any number of variables, the equation is of character str and it is iterations are int,list and dictionaries. int,if the iterations=int.
            
            def ReadEquation(equation, X0=(0.1, 1.0, 10.0), iterations=7, **valor):
    
    PARAMETERS IN main.py
    ==========
    
    
    
    equation: str
        It is the variable where the equation will be stored.
    
    X0: int,list
        It is or are the values ​​that the equation will take as the starting point
    
    iterations: int,list,dict
        are all the iterations that the equation will take
        
        *int, if iterations=int- the equations will have the same iterations
        *list, if iterations=list then every X0 will take the position of the iteration list.
            EXAMPLE: 
                iterations=(3.0,4.0,5.0)
                X0=(0.1,5.0,6.0)

                          X0 ->  (0.1 5.0 6.0)
                                   |   |   |
                  iterations ->  (3.0 4.0 5.0)
    
    
        *dict, if iterations=dict...then every X0 will take the value of his key , in the case of selecting dict ...
             ... X0 will be discarded and ignored
             
            EXAMPLE:
                iterations={0.1:4,3:7,2.0:10}

                        X0 -> 0.1 3.0 2.0
                               |   |   |
                iterations -> 4.0 7.0 10.0
                
    valor: dict
        it is a dictionary where the variables of the equation will take the values of their keys
    
    Return:
    
    Yx: dictionary, size = len (X0)
         It is where the results of each X0 are saved
         
    equation: str
         It is the name that will have the image
    
    # equations -> str
        #X0 -> int,list
        #int:= just be an equation
        #list:= will make different equations equal to the amount of
    X0 on the list
    # iterations -> int,list,dict. 
        #int:= will take the same value for all the iterations in X0
        #list:=will take the position of the list with the iterations in X0, 
        #dict:=will take the iteration of the key in de X0
    #valor -> dict, will take the values of each variable
        #Note: if the value isn't empty, the parameter won't be taken in X0
    
    ######################
    # Mistake proofing #
    ######################
    
    variables=[] we save the variables in the equation  
    powers=[] we save the powers of the equation
    symbols=["/","^","*","+","-","(",")"] mathematical symbols
    str_vavriables="" - where we'll save the equation
    type_X0 = [type(0),type([])]
    type_iterations = [type(0),type([]),type({})]
    valores = valor
    X0 = list(X0) if isinstance(X0,tuple) else X0
    iterations = list(iterations) if isinstance(iterations,tuple) else iterations
    
    # -------------- TESTING EQUATION ERRORS ------------------------------- -
    if isinstance (equation, str) == False:
        raise ("equation can only be str no" + str (type (equation)))
    for i in equation: #recorremos the whole equation to see its content
        try:
            if int (i)% 1 == 0: # if it is a number it is a power
                powers.append (i)
        except:
            if i not in symbols_math: # we prevent you from saving math symbols
                if i! = "x":
                    variables.append (i) #if it is not a number it is a variable
                    str_variables + = str (i) + ""
               
    for i in variables: #recorremos the variables of the equation
        if i not in valor.keys (): # if they gave us more variables than the equation has or is not, then it has an error
            raise TypeError ("The equation variables do not match") #we return the error
   
    # -------------- TESTING X0 ERRORS ------------------------------- --------
    #if type (X0) not in type_X0:
        #raise TypeError ("X0 can only be 'list' or 'int' no" + str (type (equation)))
       
    #if isinstance (X0, int) == False or isinstance (X0, list) == False: #If X0 is different from int or list then error
        #raise TypeError ("X0 can only be 'list' or 'int' no" + str (type (equation)))
    #if isinstance (X0, dict):
        #raise TypeError ("X0 can only be 'list' or 'int', not 'dict'")
    #else if isinstance (X0, str):
        #raise TypeError ("X0 can only be 'list' or 'int', not 'str'")
       
   
    # -------------- TESTING ITERATIONS ERRORS ------------------------------- ---
    if type (iterations) not in type_iterations:
        raise TypeError ("iterations cannot be" + str (type (iterations)))
       
    #if isinstance (iterations, int) == False or isinstance (iterations, list) == False or isinstance (iterations, dict) == False:
        #raise TypeError ("iterations cannot be" + str (type (iterations)))
   
    if isinstance (iterations, list):
        for i in iterations:
            if isinstance (i, int) == False:
                raise TypeError ("all iterations values ​​must be int")
   
    # ------------- TESTING THE LISTS OF X0 AND ITERATIONS -----------------------
    #if isinstance (iterations, list) and isinstance (X0, int):
    # raise TypeError ("if iteration is 'list' then X0 must also be 'list'")
    #if isinstance (iterations, int) and isinstance (X0, list):
    # raise TypeError ("if X0 is 'list' then iterations must also be 'list'")
   
           
                            ########################
                            # Execution of the code #
                            ########################
   
    #str_variables = str_variables [: - 1] #all the variables we are going to use
    str_variables + = "x" #all the variables we are going to use
   
       
    # =================== FOR X0 = INT ========================== =================================
    if isinstance (X0, int): #If it is int then you will only want a single value for X0
        # ---- What we saw in class ----
        variables_ = symbols (str_variables) # we tell you which variables we will use
        y = sympify (equation) # we tell you the equation
        f = lambdify (variables_, and, "numpy") #save the function
        Yx = {} #dictionary where we will keep the output of the equations
       
        values ​​["x"] = X0 # add the variable x to the dictionary to solve the equation
       
        outputs = [] #list where we will save all the data
        for _ in range (iterations): #iterations must be int
            aux_ = f (** values)
            values ​​["x"] = copy (aux_)
            outputs.append (aux_) #save the result of the equation in the list
            Yx [X0] = outputs #lo add it to the dictionary
       
        return Yx, equation #We return
   
    # ===================== FOR X0 = LIST AND ITERATIONS! = DICT =================== ===============
    elif isinstance (X0, list) and isinstance (iterations, dict) == False:
       
        # ---- What we saw in class ----
        variables_ = symbols (str_variables) # we tell you which variables we will use
        y = sympify (equation) # we tell you the equation
        f = lambdify (variables_, and, "numpy") #save the function
        Yx = {} #dictionary where we will keep the output of the equations
       
        # ----------------- ITERATIONS = INT ------------
        if isinstance (iterations, int): #If it is an integer then the entire list of X0 will have the same iterations
            for i in X0: #As it is a list we have to take each of the values
                values ​​["x"] = i # add the variable x to the dictionary to solve the equation
                outputs = [] #list where we will save all the data
                for j in range (iterations): # being int iterations we must use range
                    aux_ = f (** values)
                    values ​​["x"
    
    


<h5 align="left" style="color:orange;">IMPLEMENTATION</h5>

    in plotter,py to show the graphic we create a function for the plotter(def plotter(Yx, equation):) where it will take the mandatory parameters of Xy which is the dictionary of the values of the Y axis to graph and equation which is the equation entered and which will be added as a title,
    We will assign the variables fig and ax to the subplots to graph the values of the Y, fig is not yet used

    then we implement a cycle that runs through all the keys of the dictionaries and that makes the graphs for all the values that contain the keys, that is the values of Y.
    What is done next is to scale the graphs, make the grids, label the X and Y axes and add the equation in which it will work.
      ending with a plt.show () that will show the graph
      
      
      Console input example:
      
      
      python3 main.py -e x+x^2+a a=1.4 X0=4.2 -i 9

        -e ask for the equation
        a = the values of a in the equation
        X0 = starting point values
        -i = the number of iterations
<h5 align="left" style="color:orange;">REFERENCES</h5>

            - "Corrosionpedia", s.f, Párr.1. Dynamic System. Recovered from  https://www.corrosionpedia.com/definition/424/dynamic-system.




