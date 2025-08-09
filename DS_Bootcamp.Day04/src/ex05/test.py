import sys
import pytest
from ordinary import read_file_into_list, main as ordinary_main
from generator import read_file_generator, main as generator_main

def test_read_file_into_list(tmp_path):
    file = tmp_path / "test.txt"
    content = "line1\nline2\n"
    file.write_text(content)
    lines = read_file_into_list(str(file))
    assert lines == ["line1\n", "line2\n"]


def test_read_file_generator(tmp_path):
    file = tmp_path / "test.txt"
    content = "foo\nbar\nbaz\n"
    file.write_text(content)
    gen = read_file_generator(str(file))
    assert list(gen) == ["foo\n", "bar\n", "baz\n"]


def test_methods_return_identical(tmp_path):
    file = tmp_path / "test.txt"
    content = "a\nb\nc\n"
    file.write_text(content)
    lines_list = read_file_into_list(str(file))
    lines_gen = list(read_file_generator(str(file)))
    assert lines_list == lines_gen


def test_main_usage_message_ordinary(capsys, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['ordinary.py'])
    with pytest.raises(SystemExit):
        ordinary_main()
    captured = capsys.readouterr()
    assert "Usage: python ordinary.py <path_to_file>" in captured.out


def test_main_usage_message_generator(capsys, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['generator.py'])
    with pytest.raises(SystemExit):
        generator_main()
    captured = capsys.readouterr()
    assert "Usage: python generator.py <path_to_file>" in captured.out


def test_main_outputs_metrics(tmp_path, capsys, monkeypatch):
    file = tmp_path / "test.txt"
    lines = ["x\n", "y\n", "z\n"]
    file.write_text("".join(lines))

    # ordinary.py
    monkeypatch.setattr(sys, 'argv', ['ordinary.py', str(file)])
    ordinary_main()
    captured = capsys.readouterr().out
    assert "Peak Memory Usage" in captured
    assert "User Mode Time + System Mode Time" in captured

    # generator.py
    monkeypatch.setattr(sys, 'argv', ['generator.py', str(file)])
    generator_main()
    captured2 = capsys.readouterr().out
    assert "Peak Memory Usage" in captured2
    assert "User Mode Time + System Mode Time" in captured2
