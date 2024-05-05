from sympy import symbols, Not, Or, And, Implies, satisfiable  # Importa las funciones y clases necesarias de la biblioteca SymPy

class InferenciaLogicaProposicional:  # Define una clase para la Inferencia Lógica Proposicional
    def __init__(self):  # Constructor de la clase
        pass  # No hace nada en el constructor

    def inferir(self, clausulas, consulta):  # Método para realizar la inferencia
        clausulas.append(Not(consulta))  # Agrega la negación de la consulta a las clausulas
        expresion = And(*clausulas)  # Convierte las clausulas a una sola expresión
        if satisfiable(expresion) == False:  # Verifica si la expresión es insatisfacible
            return "Insatisfacible"  # Retorna "Insatisfacible" si la expresión es insatisfacible
        if satisfiable(And(*clausulas)) == True:  # Verifica si la consulta es satisfecha
            return "Verdadero"  # Retorna "Verdadero" si la consulta es satisfecha
        else:  # Si la consulta no es satisfecha
            return "Falso"  # Retorna "Falso"

if __name__ == "__main__":  # Verifica si el script está siendo ejecutado directamente
    inferencia = InferenciaLogicaProposicional()  # Crea una instancia de la clase InferenciaLogicaProposicional
    x, y, z = symbols('x y z')  # Define símbolos x, y, z
    clausulas = [Or(x, y), Or(Not(x), z), Or(Not(y), Not(z))]  # Define cláusulas (conjunto de expresiones lógicas)
    consulta = z  # Define la consulta (una expresión lógica que se desea verificar)
    resultado = inferencia.inferir(clausulas, consulta)  # Realiza la inferencia
    print("El resultado de la inferencia es:", resultado)  # Imprime el resultado de la inferencia
