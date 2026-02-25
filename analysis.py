import pandas as pd
def analyze_data(df):
    subject_avg= df[['Math', 'Science', 'English']].mean()
    
    df['Total']= df[['Math', 'Science', 'English']].sum(axis=1)
    topper= df.loc[df['Total'].idxmax()]['Name']
    weakest_subject= subject_avg.idxmin()
    return subject_avg, topper, weakest_subject, df