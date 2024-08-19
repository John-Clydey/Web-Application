import streamlit as st
import matrix_sum as ms
import matrix_product as mp
import matrix_determinant as md
import inverse_matrix as mi
import matrix_transpose as mt
import numpy as np
from streamlit_pills import pills

st.markdown(
    """
    <style>
    .stApp{
        background-color : #D1B15B;

    }
    </style>
    """,
    unsafe_allow_html=True
)

# Importing Allura font from Google Fonts
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Allura&display=swap" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

st.markdown("<style> .allura-text { font-family: 'Allura', cursive; font-size: 40px; color: white; } </style>",
            unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; font-size: 80px; font-weight: bold; color: blue;'>COSMOS MATRICIS🖥️</h1>",
            unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center;' class='allura-text'>The world is built on the power of numbers. —Pythagoras</p>",
    unsafe_allow_html=True)

st.write("-------")

# Input fields for matrix A
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; text-align: center; color: blue">
        Enter desired size of Matrix A:
        </h1>
    """, unsafe_allow_html=True)
with col2:
    row_a = st.number_input("ROW:", min_value=1, max_value=5, key='row_a')
with col3:
    column_a = st.number_input("COLUMN:", min_value=1, max_value=5, key='column_a')

col4, col5, col6 = st.columns(3)
with col4:
    st.markdown("""
        <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; text-align: center; color: blue">
        Enter desired size of Matrix B:
        </h1>
    """, unsafe_allow_html=True)
with col5:
    row_b = st.number_input("ROW:", min_value=1, max_value=5, key='row_b')
with col6:
    column_b = st.number_input("COLUMN:", min_value=1, max_value=5, key='column_b')

col7, col8 = st.columns(2)
with col7:
    st.markdown("""
            <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; color: blue">
            Matrix A:
            </h1>
        """, unsafe_allow_html=True)
    matA = []
    for row_index in range(row_a):
        columns = st.columns(column_a)
        row_values = []
        for col_index, col in enumerate(columns):
            with col:
                value = st.text_input("", key=f'Arow{row_index + 1}Acol{col_index + 1}')
                row_values.append(value.strip() if value else '0')  # Handle empty input
        matA.append(row_values)

with col8:
    st.markdown("""
            <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; color: blue">
            Matrix B:
            </h1>
        """, unsafe_allow_html=True)
    matB = []
    for row_index in range(row_b):
        columns = st.columns(column_b)
        row_values = []
        for col_index, col in enumerate(columns):
            with col:
                value = st.text_input("", key=f'Brow{row_index + 1}Bcol{col_index + 1}')
                row_values.append(value.strip() if value else '0')  # Handle empty input
        matB.append(row_values)

if all(value.isdigit() for row in matA + matB for value in row):
    matA = [[int(value) for value in row] for row in matA]
    matB = [[int(value) for value in row] for row in matB]

    if pills:
        selected = pills("SELECT A MATRIX OPERATION:",
                         ["Sum of Matrices", "Product of Matrices", "Determinant of a Matrix", "Inverse Matrix",
                          "Transpose of a Matrix"], ["➕", "❌", "📈", "A⁻¹", "🧩"])

        st.write(selected)
        if selected == 'Sum of Matrices':
            if len(matA) != len(matB) or len(matA[0]) != len(matB[0]):
                st.error("Matrices A and B must have the same size for the sum of matrices.")
            else:
                st.markdown("""
                                <h1 style="font-size: 34px; font-family: 'Arial, sans-serif'; align: 'Center'; color: blue">
                                Matrix Result:
                                </h1>
                            """, unsafe_allow_html=True)
                matrix_Result = ms.sum_matrices(matA, matB)
                col6, col7, col8 = st.columns(3)
                with col7:
                    for row_index in range(len(matrix_Result)):
                        columns = st.columns(len(matrix_Result[0]))
                        for col_index, col in enumerate(columns):
                            with col:
                                st.text_input("", value=matrix_Result[row_index][col_index],
                                              key=f'Rrow{row_index + 1}Rcol{col_index + 1}')

        elif selected == 'Product of Matrices':
            if len(matA[0]) != len(matB):
                st.error("Invalid matrix size! To perform, the numbers in Column-A & Row-B must be equal.")
            else:
                st.markdown("""
                                <h1 style="font-size: 34px; font-family: 'Arial, sans-serif'; align: 'Center'; color: blue">
                                Matrix Result:
                                </h1>
                            """, unsafe_allow_html=True)
                matrix_Result = mp.product_matrices(matA, matB)
                col6, col7, col8 = st.columns(3)
                with col7:
                    for row_index in range(len(matrix_Result)):
                        columns = st.columns(len(matrix_Result[0]))
                        for col_index, col in enumerate(columns):
                            with col:
                                st.text_input("", value=matrix_Result[row_index][col_index],
                                              key=f'Rrow{row_index + 1}Rcol{col_index + 1}')

        elif selected == 'Determinant of a Matrix':
            if len(matA[0]) != len(matB):
                st.error("Invalid size! To perform, number of rows & columns must be the same.")
            try:
                det_matA, det_matB = md.determinant_matrices(matA, matB)
                col9, col10 = st.columns(2)
                with col9:
                    st.markdown("""
                                <h1 style="font-size: 34px; font-family: 'Arial, sans-serif'; align: 'Center'; color: blue">
                                Matrix Result:
                                </h1>
                                """, unsafe_allow_html=True)
                    st.write(det_matA)
                with col10:
                    st.markdown("""
                                <h1 style="font-size: 34px; font-family: 'Arial, sans-serif'; align: 'Center'; color: blue">
                                Matrix Result:
                                </h1>
                                """, unsafe_allow_html=True)
                    st.write(det_matB)
            except np.linalg.LinAlgError as e:
                st.error(str(e))


        elif selected == 'Inverse Matrix':
            try:
                col9, col10 = st.columns(2)
                if matA:
                    if isinstance(matA, str):
                        matA = [int(x) for x in matA.split(',')]
                    matA = np.array(matA)
                    if matA.shape[0] != matA.shape[1]:
                        st.error("Error: Input matrix A must be square for inversion.")
                    else:
                        with col9:
                            inv_matA = np.linalg.inv(matA)
                            st.markdown("""<h1 style="font-size: 34px; font-family: 'Arial, sans-serif'; align: 'Center'; color: blue">
                                    Matrix Result:
                                    </h1> """, unsafe_allow_html=True)
                            st.write(inv_matA)
                else:
                    st.warning("Matrix A input is not provided. Cannot calculate its inverse.")

                if matB:
                    if isinstance(matB, str):
                        matB = [int(x) for x in matB.split(',')]
                    matB = np.array(matB)
                    if matB.shape[0] != matB.shape[1]:
                        st.error("Error: Input matrix B must be square for inversion.")
                    else:
                        with col10:
                            inv_matB = np.linalg.inv(matB)
                            st.markdown("""<h1 style="font-size: 34px; font-family: 'Arial, sans-serif'; align: 'Center'; color: blue">
                                    Matrix Result:
                                   </h1> """, unsafe_allow_html=True)
                            st.write(inv_matB)
                else:
                    st.warning("Matrix B input is not provided. Cannot calculate its inverse.")
            except ValueError as e:
                st.error("Error: Invalid input matrix. Please provide valid square matrices.")

            except np.linalg.LinAlgError as e:

                st.error("Error: {}.".format(e))

        elif selected == 'Transpose of a Matrix':
            w = np.array(matA).shape[0]
            x = np.array(matA).shape[1]
            mat_Id1 = np.zeros((x, w))

            for i in range(w):
                for j in range(x):
                    mat_Id1[j][i] = matA[i][j]

            col11, col12 = st.columns(2)

            with col11:
                st.markdown("""<h1 style="font-size: 34px; font-family: 'Arial, sans-serif'; align: 'Center'; color: blue">
                            Matrix Result:
                            </h1> """, unsafe_allow_html=True)
                st.write(mat_Id1)

            if matB:  # Check if matrix B exists
                y = np.array(matB).shape[0]
                z = np.array(matB).shape[1]
                mat_Id2 = np.zeros((z, y))

                for i in range(y):
                    for j in range(z):
                        mat_Id2[j][i] = matB[i][j]

                with col12:
                    st.markdown("""<h1 style="font-size: 34px; font-family: 'Arial, sans-serif'; align: 'Center'; color: blue">
                                Matrix Result:
                               </h1> """, unsafe_allow_html=True)
                    st.write(mat_Id2)


else:
    st.error("Please enter valid integer values for matrix elements.")
