orden=[
"Arithmetic",
"Basic geometry and measurement",
"Pre-algebra",
"Algebra basics",
"Get ready for Algebra 1",
"Algebra 1",
"High school geometry",
"Get ready for Algebra 2",
"Algebra 2",
"Statistics and probability",
"High school statistics",
"Get ready for Precalculus",
"College Algebra",
"Trigonometry",
"Precalculus",
"Get ready for AP® Statistics",
"AP®/College Statistics",
"Get ready for AP® Calculus",
"AP®/College Calculus AB",
"AP®/College Calculus BC",
"Differential Calculus",
"Integral Calculus",
"Multivariable calculus",
"Differential equations",
"Linear algebra"
]

def entregar_posicion(nombre):
    return orden.index(nombre)

print(entregar_posicion("Algebra 1"))