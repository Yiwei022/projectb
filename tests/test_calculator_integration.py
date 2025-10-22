from src.calculator import calculator
import builtins


def test_add(monkeypatch, capfd):
    inputs = iter(["2", "3", "4", "n"])  # addition
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    calculator()
    out, _ = capfd.readouterr()
    assert "Résultat : 5.0" in out


def test_sub(monkeypatch, capfd):
    inputs = iter(["5", "2", "2", "n"])  # soustraction
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    calculator()
    out, _ = capfd.readouterr()
    assert "Résultat : 3.0" in out


def test_mul(monkeypatch, capfd):
    inputs = iter(["4", "3", "1", "n"])  # multiplication
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    calculator()
    out, _ = capfd.readouterr()
    assert "Résultat : 12.0" in out


def test_div(monkeypatch, capfd):
    inputs = iter(["10", "2", "3", "n"])  # division
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    calculator()
    out, _ = capfd.readouterr()
    assert "Résultat : 5.0" in out


def test_div_zero(monkeypatch, capfd):
    inputs = iter(["10", "0", "3", "n"])  # division par zéro
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    calculator()
    out, _ = capfd.readouterr()
    assert "Erreur : Division par zéro interdite." in out


def test_invalid_choice(monkeypatch, capfd):
    inputs = iter(["1", "1", "9", "n"])  # choix invalide
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    calculator()
    out, _ = capfd.readouterr()
    assert "Choix invalide" in out
