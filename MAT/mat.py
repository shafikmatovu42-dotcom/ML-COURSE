import numpy as np

import matplotlib.pyplot as plt 

import pandas as pd

print("********BASIC PLOTING**********")
def basic_plotting():
    x = [10,20,30,40,50]
    y = [0.1,0.2,0.3,0.4,0.5]

    plt.plot(x,y, marker="o")
    plt.show() 

#basic_plotting()
class plot():
    #using a dict()to create customisation of the plots at once
    """customization = dict(marker="o,.,etc",
                    #markersize(ms)=10, #size of the marker,
                    #markerfacecolor(mfc)="red" #color of the marker
                    #markeredgecolor(mec)="blue" #color of the marker edge
                    #linestyle(ls)="dashed,dotted,solid,dashdot,none" #line style
                    #linewidth(lw)=2, #width of the line
                    #linecolor(lc)="green", #color of the line)
                    # then we can insert this when plotting
                    # but we unpack it using **customization"""

    #editing labels of the graph(words arount it)
    """  plt.title("Title of the graph",
                    fontsize=20, #size of the title
                    color="red", #color of the title
                    fontweight="bold", #font weight of the title
                    fontfamily="serif" #font family of the title
                    )
        plt.xlabel("txt for x-axis",
                     fontsize=15, 
                     color="blue", 
                     fontweight="bold", 
                     fontfamily="serif")
        plt.ylabel("txt for y-axis", 
                     fontsize=15, 
                     color="blue",
                     fontweight="bold", 
                     fontfamily="serif")
        plt.tick_params(axis="x or y or both", 
                        color="red", #color of the ticks
                        labelsize=10, #size of the ticks
                        labelcolor="green", #color of the ticks labels
                        direction="in or out or inout", #direction of the ticks
                        length=5, #length of the ticks
                        width=2, #width of the ticks
                        grid_color="blue", #color of the grid
                        grid_linestyle="dashed", #style of the grid
                        grid_linewidth=1, #width of the grid
                        grid_alpha=0.5, #transparency of the grid
                        grid_axis="x or y or both" #which axis to show the grid
                     **there we are editing the ticks(value and words on the scale)
       
        
        plt.grid(    axis="x or y or both", #which axis to show the grid)
                    color="blue", #color of the grid
                    linestyle="dashed", #style of the grid
                    linewidth=1, #width of the grid
                     
                     """

    def using_array():
        x = np.array([10,20,30,40,50])
        y1 = np.array([0.1,0.2,0.3,0.4,0.5])
        y2 = np.array([0.5,0.4,0.3,0.2,0.1])


        #we can unpack as shown bellow
        #here we have two lines, one for y1 and another for y2
        plt.plot(x,y1, marker="o"
                    # **customization
                    )
        plt.plot(x,y2, marker="s")
        plt.show()

    

    

    
    
    #we then generate values from -10 to 10 with 100 steps btn
    def plot_sin():
        x = np.linspace(-10,10,100)
        # for y axix, we get the sin(x)
        y = np.sin(x)
        #we then use the plot funtion to plot
        plt.plot(x, y, marker="x"
                
                )
        plt.show()


    #plotting a barchart from a list of values
    #we convert the list to an array and then plot it using the bar() function
    def barchart():
        categories = np.array(["boys","girls","men","women","children"])
        values     = np.array([40,20,50,30,10])

        #we then plot using the bar()
        plt.bar(categories, values, color="blue", alpha=0.5)
        #for a horizontal bar chart, we use barh() instead of bar()
        #plt.barh(categories, values, color="blue", alpha=0.5)
        plt.title("OUR ENVIRONMENT",
                  fontsize=20,
                  color = "green"
                  )
        plt.xlabel("members")
        plt.ylabel("present")
        plt.show()

    def pie_chart():
        categories = ["boys","girls","men","women","children"]
        values     = np.array([40,20,50,30,10])
        #we can add colors directly
        #colors = ["red","green",'blue',"white","yellow"]

        #we then plot using the pie()
        #plt.pie(values, labels=categories, #colors = colors)
        #explode param extends a pie way , eg
        plt.pie(values, 
                labels=categories, 
                autopct="%1.1f%%", 
                startangle=90,
                explode=[0,0,0,0,0.1],
                shadow = True)
        
        
        plt.title("OUR ENVIRONMENT",
                  fontsize=20,
                  color = "green"
                  )
        
        
        plt.show()


    def scatter_graph():
        #shows relationship btn 2 variables
        #helps to indentify corelatio
        # e.g sturdy hours vs test scores
        rng = np.random.default_rng(seed=42)
        n = 9

        x1 = rng.integers(0,10,size=n)  #hours studied
        y1= rng.integers(0,100,size=n) #grades

        #lets create our own values
        x2  = np.array([2,3,4,5,6,7,7,8,9]) #hours sturded
        y2 = np.array([55,60,65,62,68,70,78,87,93]) #GRADES

         
        plt.ylabel("GRADES",color = "green")
        plt.xlabel("HOURS STURDIED",color = "green")
        plt.title("TEST SCORES")
        plt.scatter(x1,y1,color= 'red',
                    alpha=0.6,
                    s = 200,
                    label = 'CLASS A'
                      )
        plt.scatter(x2,y2,color= 'green',
                            alpha=0.6,
                            s = 200,
                            label = "CLASS B"
                              )
        #CALL THE LEDGEND FUNC  to make the  lables vissible
        plt.legend()
        plt.show()

    def    histogram():
        #A VISUAL REPRESENTATION OD THE DISTRIBUTION OF QUANTITATIVE DATA

        scores = np.random.normal(loc=80, scale=10, size=100 )
        #we can use the clip() to set boundaries
        #eg
        #scores = np.clip(scores,0,100)

        plt.hist(scores,
                 bins=10,
                 color = "brown",
                 edgecolor = "black") 
        
        plt.title(" EXAM SCORES")
        plt.xlabel("SCORES")
        plt.ylabel("NO OF STUDENTS")
        
        plt.show()



    def sub_plots():
        #this is used to create multiple plots
    
        
        figure , axes = plt.subplots(2,2)
        x = np.array([1,2,3,4,5])

        axes[0,0].plot(x,x*2,color = "green")
        axes[0,0].set_title("x*2")

        axes[1,0].bar(x,x**2, color = "red")
        axes[1,0].set_title("x**2")

        axes[0,1].scatter(x,x**3,color = "yellow")
        axes[0,1].set_title("x**3")

        axes[1,1].plot(x,x**4,color = "brown")
        axes[1,1].set_title("x**4")

        plt.tight_layout()

        plt.show()

    def panda_mat():

        df = pd.read_csv("MAT/pokemon.csv")



        type_count = (df['Type1'].value_counts(ascending=True))

        plt.barh(type_count.index,type_count.values,color = "green",
                 edgecolor = "black")
        plt.xlabel("COUNT")
        plt.title("POKEMEN OF PRIMARY TYPE", color = "red")
        plt.ylabel("TYPE")
        plt.tight_layout()
        plt.show()







    



          





    

#plot.using_array()
#plot_sin()
#plot.barchart()
#plot.pie_chart()
#plot.scatter_graph()
#plot.histogram()
#plot.sub_plots()
plot.panda_mat()