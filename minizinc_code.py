def generate_minizinc(N, M, ciudades):
    nombres = [ciudad[0] for ciudad in ciudades]
    nombres_str = ', '.join(nombres)
    return f"""% Tamaño del valle
int: N = {N};

% Número de ciudades
int: M = {M};

% Conjunto de nombres de ciudades
enum CIUDADES = {{{nombres_str}}};

% Coordenadas de las ciudades
array[CIUDADES] of int: x = {[ciudad[1] for ciudad in ciudades]};
array[CIUDADES] of int: y = {[ciudad[2] for ciudad in ciudades]};

% Variables de decisión
var 1..N: x_concierto;
var 1..N: y_concierto;

% Función para calcular la distancia Manhattan
function var int: distancia_manhattan(var int: x1, var int: y1, var int: x2, var int: y2) =
    abs(x1 - x2) + abs(y1 - y2);

% RESTRICCIONES:
% El concierto no puede estar en la misma posición que las ciudades
constraint forall(i in CIUDADES)(
    x_concierto != x[i] \/ y_concierto != y[i]
);

% La diferencia de distancias entre cualquier par de ciudades no puede ser mayor a 2
constraint forall(i, j in CIUDADES where i < j)(
    abs(distancia_manhattan(x_concierto, y_concierto, x[i], y[i]) - 
        distancia_manhattan(x_concierto, y_concierto, x[j], y[j])) <= 2
);

% OBJETIVO: minimizar la suma de distancias
var int: objetivo = sum(i in CIUDADES)(
    distancia_manhattan(x_concierto, y_concierto, x[i], y[i])
);

solve minimize objetivo;

output ["Posición del concierto: (", show(x_concierto), ", ", show(y_concierto), ")\\n",
        "Distancia total: ", show(objetivo), "\\n",
        "Distancias individuales:\\n"] ++
       [show(i) ++ ": " ++ show(distancia_manhattan(
       x_concierto, y_concierto, x[i], y[i])) ++ "\\n" |
        i in CIUDADES];
"""
