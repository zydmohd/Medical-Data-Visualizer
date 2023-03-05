import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
# Import data
df = pd.read_csv("/home/zyd/Projects_for_Backup/coding_project/python_freecodecamp/Medical Data Visualizer/medical_examination.csv")

# Add 'overweight' column
df['overweight'] = (df['weight']/((df['height']/100)**2)).apply(lambda x: 1 if x>25 else 0 )

    # Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol']=df['cholesterol'].apply(lambda x : 0 if x==1 else (1 if x>1 else df['cholesterol']))
df['gluc']=df['gluc'].apply(lambda x : 0 if x==1 else (1 if x>0 else df['gluc']))


# Draw Categorical Plot
def draw_cat_plot():
    
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,id_vars='cardio',value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #df_cat = None
    

    # Draw the catplot with 'sns.catplot()'
    fig=sns.catplot(df_cat,x='variable',kind='count',hue='value',col="cardio")
    


    # Get the figure for the output
    
    fig.set(ylabel="total")


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat=df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
           & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = corr.where(np.tril(np.ones(corr.shape)).astype(bool))



    # Set up the matplotlib figure
    fig=sns.heatmap(mask, annot=True, linewidth=.5,fmt=".1f")

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
