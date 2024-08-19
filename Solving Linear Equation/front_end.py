import streamlit as st
import numpy as np

background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://wallpapercave.com/wp/wp10432106.jpg");
    background-size: 100vw 100vh;
    background-position: center;  
    background-repeat: repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)


def lu_decomposition(A):
    n = len(A)
    L = np.eye(n)
    U = A.copy()

    for i in range(n):
        for j in range(i + 1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j, i:] -= factor * U[i, i:]

    return L, U


def solve_lu_decomposition(L, U, B):
    n = len(B)
    y = np.zeros(n)
    x = np.zeros(n)

    # Solve Ly = B
    for i in range(n):
        y[i] = B[i] - np.dot(L[i, :i], y[:i])

    # Solve Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x


def main():
    st.markdown(
        "<h1 style='text-align: center; font-size: 46px; font-weight: bold; color: gold;'>SYSTEM OF EQUATIONS SOLVER📈</h1>",
        unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
                    <h1 style="font-size: 30px; font-family: 'Arial, sans-serif'; text-align: center; color: pink">
                    Enter number of equations:
                    </h1>
                """, unsafe_allow_html=True)
    with col2:
        num_equations = st.number_input("", min_value=2, step=1, max_value=5)

    A = []
    B = []

    # Input coefficients and constants
    for i in range(num_equations):
        st.markdown(f"<h2 style='color: magenta; font-size: 35px;'>EQUATION {i + 1}:</h2>", unsafe_allow_html=True)
        equation_cols = st.columns(2 * num_equations)
        for j in range(num_equations):
            with equation_cols[j]:
                st.markdown(f"<span style='color: gold;'>Coefficient {j + 1}:</span>", unsafe_allow_html=True)
                coeff = st.number_input("", key=f"coeff_{i}_{j}", format="%f")
                A.append(coeff)
            if j == num_equations - 1:
                with equation_cols[j + 1]:
                    st.markdown(f"<span style='color: gold;'>Constant:</span>", unsafe_allow_html=True)
                    const = st.number_input("", key=f"const_{i}")
                    B.append(const)

    A = np.array(A).reshape(num_equations, num_equations)
    B = np.array(B)

    if st.button("Solve"):
        L, U = lu_decomposition(A)
        roots = solve_lu_decomposition(L, U, B)

        st.markdown("""
                    <h1 style="font-size: 30px; font-family: 'Arial, sans-serif'; text-align: center; color: gold">
                    STEP-BY-STEP PROCESS:
                    </h1>
                    """, unsafe_allow_html=True)
        st.markdown("<div style='display:flex; justify-content:center;'>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
                                <h1 style="font-size: 30px; font-family: 'Arial, sans-serif'; text-align: center; color: pink">
                                LOWER TRIANGULAR MATRIX (L):
                                </h1>
                                """, unsafe_allow_html=True)
            st.write(np.round(L, 2))
        with col2:
            st.markdown("""
                                <h1 style="font-size: 30px; font-family: 'Arial, sans-serif'; text-align: center; color: pink">
                                UPPER TRIANGULAR MATRIX (U):
                                </h1>
                                """, unsafe_allow_html=True)
            st.write(np.round(U, 2))
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
                    <h1 style="font-size: 30px; font-family: 'Arial, sans-serif'; text-align: center; color: gold">
                    THE SOLUTION(s) / ROOT(s) OF AN EQUATION:
                    </h1>
                    """, unsafe_allow_html=True)
        for i, root in enumerate(roots):
            st.markdown(f"<h3 style='color: white;'>X<sub>{i + 1}</sub>: {root}</h3>", unsafe_allow_html=True)


main()
