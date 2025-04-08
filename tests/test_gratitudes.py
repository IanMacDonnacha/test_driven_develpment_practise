from lib.gratitudes import *

def test_for_empty_gratitude():
    gratitude = Gratitudes()
    gratitude.add("")
    result = gratitude.format()
    assert result == "Be grateful for: "

def test_for_add_a_single_gratitude():
    gratitude = Gratitudes()
    gratitude.add("Happiness")
    result = gratitude.format()
    assert result == "Be grateful for: Happiness"

def test_for_add_multiple_gratitudes():
    gratitude = Gratitudes()
    gratitude.add("Happiness")
    gratitude.add("Courage")
    gratitude.add("Kindness")
    result = gratitude.format()
    assert result == "Be grateful for: Happiness, Courage, Kindness"