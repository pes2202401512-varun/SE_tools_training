import subprocess
import sys
import os
import pytest


class TestCLIIntegration:
    """Test CLI application integrating with calculator module"""

    def run_cli(self, *args):
        """Run CLI script under coverage tracking"""
        cmd = [
            sys.executable,
            "-m",
            "coverage",
            "run",
            "--parallel-mode",
            "src/cli.py",
        ] + list(args)

        env = os.environ.copy()
        env["PYTHONPATH"] = os.getcwd()  # ensure src/ is importable

        result = subprocess.run(cmd, capture_output=True, text=True, cwd=".", env=env)
        return result

    def test_cli_add_integration(self):
        result = self.run_cli("add", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "8"

    def test_cli_subtract_integration(self):
        result = self.run_cli("subtract", "5", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "2"

    def test_cli_subtract_missing_operand_error(self):
        result = self.run_cli("subtract", "5")
        assert result.returncode == 1
        assert result.stdout.strip().startswith("Unexpected error:")
