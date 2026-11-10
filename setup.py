# pip install cx_freeze
# para gerar o executavel: python setup.py build
import cx_Freeze

executaveis = [
    cx_Freeze.Executable(
        script="main.py",
        icon="bases/icone.ico",
        target_name="AstronautaPerdido"
    )
]

cx_Freeze.setup(
    name="Astronauta Perdido",
    version="1.0",
    description="Jogo Astronauta Perdido feito com Python e Pygame",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files": ["bases", "Recursos"]
        }
    },
    executables=executaveis
)
