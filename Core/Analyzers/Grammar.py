# -*- coding: utf-8 -*-
"""
----------------------------------------------------------------------------------------------------
    
    @author Grupo #4 - Diseño de Compiladores - IS913 (0900)
    @date 02/11/2021
    @decription Gramatica libre de contexto
    @name_file Grammar.py
    @version 1.0

----------------------------------------------------------------------------------------------------
    
    ! Grámatica de un lenguaje propio
    ? Grámaticas libres de ambiguedad.

----------------------------------------------------------------------------------------------------
"""
grammar = """

    // El axioma inicial
    ?start: exp+

    //Definicion de una expresion
    ?exp: var "=" string "$" -> assignvariable
        | var "=" arithmeticoperation "$" -> assignvariable
        | var "=" repeat "$" -> assignvariable
        | var "=" concatenate "$" -> assignvariable
        | "pantalla" string "$" -> print
        | "pantalla" arithmeticoperation "$" -> print
        | "pantalla" var "$" -> printvariable


    // Definicion de operacion aritmetica
    ?arithmeticoperation: product
        | arithmeticoperation "+" product -> add
        | arithmeticoperation "-" product -> sub
    
    ?product: atom
        | product "*" atom -> mul
        | product "/" atom -> div

    ?repeat: "#" number "*" string -> repeat
    
    ?concatenate: var ":" var-> concatenate
    
    ?atom: var -> getvar
        | number
        | "-" atom
        | "(" atom ")"
        | "(" var ")"

    ?string: /'[^']*'/
        
    ?var: /[a-zA-Z]\w*/

    ?number: /\d+(\.\d+)?/

    %ignore /\s+/
"""
