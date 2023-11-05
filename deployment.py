import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('./cars_ins.csv',index_col=False)
st.title('Car Insurance Claim Project')
page = st.sidebar.radio('Select page', ['Uni_variate', 'Bi_variate', 'Multi_variate'])
if page == 'Uni_variate':
    def main():
        tab1, tab2 = st.tabs(['Numerical Features', 'Categorical Features'])
        num_cols = df.select_dtypes(exclude='object').columns
        for col in num_cols:
            tab1.plotly_chart(px.histogram(df, x=col))

        cat_cols = df.select_dtypes(include='object').columns
        for col in cat_cols:
            tab2.plotly_chart(px.histogram(df, x=col))
    if __name__ == '__main__':
        main()
elif page == 'Bi_variate':
    def main():
        st.write('# Numerical vs Target')
        cat_cols = df.select_dtypes(exclude='object').columns.tolist()
        sel_col = st.selectbox('Select Feature', cat_cols)
        select_plot = st.selectbox('Select Plot type', ['Box Plot', 'Violin Plot', 'Strip Plot'])
        if select_plot == 'Box Plot':
            st.plotly_chart(px.box(df, sel_col, 'claim_flag'))
        elif select_plot == 'Violin Plot':
            st.plotly_chart(px.violin(df, sel_col, 'claim_flag'))
        elif select_plot == 'Strip Plot':
            st.plotly_chart(px.strip(df, sel_col, 'claim_flag'))
    if __name__ == '__main__':
        main()
elif page == 'Multi_variate':
    def main():
        col1, col2 = st.columns(2)
        col1.write('## Analysis Questions')
        col2.write('## Plots')
        col1.write('q1')
        col2.plotly_chart(px.box(df,'age','car_type',color='claim_flag'))

    if __name__ == '__main__':
        main()
