# tests/test_cli_integration.py
import pytest
from src.cli import main_function


class TestCLIIntegration:

    def run_cli(self, *args):
        """Helper to call CLI function directly."""
        return main_function(list(args))

    def test_cli_add_integration(self):
        """Test CLI can perform addition"""
        result = self.run_cli("add", "5", "3")
        assert result == 8

    def test_cli_subtract_integration(self):
        """Test CLI can perform subtraction"""
        result = self.run_cli("subtract", "5", "3")
        assert result == 2

    def test_cli_multiply_integration(self):
        """Test CLI can perform multiplication"""
        result = self.run_cli("multiply", "5", "3")
        assert result == 15

    def test_cli_divide_integration(self):
        """Test CLI can perform division"""
        result = self.run_cli("divide", "5", "3")
        # round to 2 decimal places
        assert round(result, 2) == 1.67
