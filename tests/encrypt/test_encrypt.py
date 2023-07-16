from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(1, 2)
    with pytest.raises(TypeError):
        encrypt_message("hello", "2")

    assert encrypt_message("hello", -1) == "olleh"
    assert encrypt_message("hello", 3) == "leh_ol"
    # assert encrypt_message("hello", 4) == "olleh_"
    assert encrypt_message("", 4) == ""
    assert encrypt_message("hello", 5) == "olleh"
    assert encrypt_message("hello", 3) == "leh_ol"
    assert encrypt_message("example", 4) == "elp_maxe"
