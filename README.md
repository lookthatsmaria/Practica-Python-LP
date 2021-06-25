# Logo3D

This project is the second GEI-LP practice (2020-2021 Q2 edition). 
Logo3D implements an interpreter of a programming language called Logo3D to allow painting with a 3D turtle.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install vpython.

```bash
pip3 install vpython
```
## Invocation
The interpreter is invoked with the command ```python3 logo3d.py``` passing as a parameter the name of the file containing the source code (the extension of the files for programs in Logo3D is .l3d). For example:
```bash
python3 logo3d.py programa.l3d
```

## Usage
This program draws an helix. 
```
// Demo program in Logo3D.

PROC cercle(mida, costats) IS
    FOR i FROM 1 TO costats DO
        forward(mida)
        left(360 / costats)
    END
END

PROC espiral(cercles) IS
    IF cercles > 0 THEN
        cercle(1, 12)
        up(5)
        espiral(cercles - 1)
    END
END

PROC main() IS
    espiral(5)
END
```
This program draws a blue square
```
// Demo program in Logo3D.

PROC quadrat_blau(mida) IS
    color(0.2, 0.2, 1)
    FOR i FROM 1 TO 4 DO
        forward(mida)
        left(90)
    END
END
```
This program reads two numbers, computes the maximum common divisor and prints it.

```
// Demo program in Logo3D.

// Programa principal.

PROC main() IS
    >> valor1 >> valor2
    euclides(valor1, valor2)
END


// Escriu el mcd de a i de b.

PROC euclides(a, b) IS
    WHILE a != b DO
        IF a > b THEN
            a := a - b
        ELSE
            b := b - a
        END
    END
    << a
END
```
# References

- ANTLR en Python: https://gebakx.github.io/Python3/compiladors.html#1

- vpython: https://www.glowscript.org/docs/VPythonDocs/index.html

- documenting python code: https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings

- 3D rotation and Euler angles in Python: https://www.meccanismocomplesso.org/en/3d-rotations-and-euler-angles-in-python/
