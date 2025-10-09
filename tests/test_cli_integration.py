import subprocess
import sys
import pytest

class TestCLIIntegration:
    """Test CLI application integrating with calculator module"""
    
    def run_cli(self, *args):
        """Helper to run CLI and capture output"""
        cmd = [sys.executable, 'src/cli.py'] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True, cwd='.')
        return result

    def test_cli_add_integration(self):
        result = self.run_cli("add", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "8"

    def test_cli_subtract_integration(self):
        result = self.run_cli("subtract", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "2"

    # 👇 Paste your new tests here
    def test_cli_multiply_integration(self):
        """Test CLI can perform multiplication"""
        result = self.run_cli("multiply", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "15"
    
    def test_cli_divide_integration(self):
        """Test CLI can perform division"""
        result = self.run_cli("divide", "5", "3")
        assert result.returncode == 0
        # round output to 2 decimals for comparison
        assert result.stdout.strip().startswith("1.6") or result.stdout.strip() == "1.67"
