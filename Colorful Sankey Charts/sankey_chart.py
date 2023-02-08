import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import itertools
import random

global labels
global df_labels

def generate_color(kind='rgba'):
    if kind=='hex':
        random_number = random.randint(0,16777215)
        hex_number = str(hex(random_number))
        hex_number ='#'+ hex_number[2:]
        yield hex_number
    else:
        levels = range(32,256,32)
        r=[random.choice(levels) for _ in range(3)]
        r.append(0.8)
        r=tuple(r)
        yield 'rgba'+str(r)

def change_opacity(df,opacity):
    df['Color_Link']=df['Color'].apply(lambda x:x.replace('0.8',str(opacity)))
    
def process_data(df1):
    global labels
    global df_labels
    df=df1.copy()
    labels=np.unique(df[["Source", "Target"]], axis=None)
    
    # Replacing Label Names with their indexes
    for i,item in enumerate(labels):
        df.replace(to_replace=item,value=i,inplace=True)
    
    df_labels=pd.DataFrame(labels,columns=['Label Name'])
    df_labels['Color']=''
    df_labels['Color']=df_labels['Color'].apply(lambda x :next(generate_color('rgba')))
    df_labels=df_labels.reset_index()
    df=pd.merge(df,df_labels,left_on='Source',right_on='index')
    change_opacity(df,0.5)
    return df

def plot_sankey(df1,opacity,title,width=1000,height=500,font_size=10,pad=15,thickness=20):
    df=df1.copy()
    global labels
    global df_labels
    change_opacity(df,opacity)
    fig = go.Figure(
        data=[
            go.Sankey(
                node = dict(
                    pad = pad,
                    thickness = thickness,
                    #line = dict(color = "red", width = 0.5),
                    label = labels,
                    color = df_labels['Color'],
                    customdata = df_labels['Label Name'],
                    hovertemplate='%{customdata} has total value %{value}<extra></extra>'
                ),
        link = dict(
          source = df['Source'], 
          target = df['Target'],
          value = df['Value'],
            color=df['Color_Link'],
            hovertemplate='%{target.customdata} has total value %{value}<extra></extra>'
      ))])

    fig.update_layout(title_text=title, font_size=font_size,width=width,height=height)
    fig.show()