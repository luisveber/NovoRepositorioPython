import sys
sys.path.append(".")
from src.models import pessoa

def test_concatenacao_nome_sobrenome():
    p1 = pessoa.Pessoa('Luis', 'Veber', 36, '05571962992')
    assert p1.nome_completo() == 'Luis Veber'