import io
import sys
import builtins
from calculator import run_calculator


def run_with_inputs(inputs):
    """Helper to simulate multiple inputs and capture printed output."""
    input_iter = iter(inputs)

    def mock_input(prompt=""):
        try:
            return next(input_iter)
        except StopIteration:
            raise EOFError

    # Capture printed output
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Patch input()
    original_input = builtins.input
    builtins.input = mock_input

    try:
        run_calculator()
    except EOFError:
        pass
    finally:
        builtins.input = original_input
        sys.stdout = sys.__stdout__

    return captured_output.getvalue()


def test_addition(monkeypatch):
    output = run_with_inputs(["3+3"])
    assert "Result: 6.0" in output


def test_subtraction(monkeypatch):
    output = run_with_inputs(["10 - 4"])
    assert "Result: 6.0" in output


def test_multiplication(monkeypatch):
    output = run_with_inputs(["2*5"])
    assert "Result: 10.0" in output


def test_division(monkeypatch):
    output = run_with_inputs(["8 / 2"])
    assert "Result: 4.0" in output


def test_invalid_input(monkeypatch):
    output = run_with_inputs(["abc"])
    assert "Invalid format" in output


def test_division_by_zero(monkeypatch):
    output = run_with_inputs(["5 / 0"])
    assert "Division by zero" in output
